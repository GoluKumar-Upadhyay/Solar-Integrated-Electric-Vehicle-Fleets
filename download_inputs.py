"""
Download the 2017-2019 inputs that master.ipynb needs, in the formats it reads.

    pip install pvlib requests pandas
    python download_inputs.py --api-key YOUR_NREL_KEY --email you@example.com

Get a free NREL API key (about 1 minute) at https://developer.nrel.gov/signup/
Output (relative to where you run it, i.e. the Project folder):
    data/nsrdb/caltech_2017.csv ... jpl_2019.csv   NSRDB PSM4 GOES aggregated, 30-min, local standard time
    data/caiso/load_2017_2019.csv                 EIA-930 hourly demand of the CAISO balancing area (CISO),
                                                  written in OASIS column format so master.ipynb reads it unchanged
    data/caiso/lmp_2019.csv                       2019 DAM LMP (only the test year is needed) - see below

PRICES: the OASIS API keeps only the last 39 months, so 2019 prices cannot be fetched from it any more.
Two options:
  (a) CAISO "Historical OASIS Data Downloader" (OASIS home page -> System Help; needs your own AWS account).
      Download PRC_LMP, DAM, node TH_SP15_GEN-APND, 2019, and save the CSV(s) as data/caiso/lmp_*.csv.
  (b) Time-of-use tariff of the site (what a garage actually pays):
      python download_inputs.py --only tou --tou "0-8:0.10,8-16:0.13,16-21:0.25,21-24:0.10" --tou-source "PWP tariff ..."
      ($/kWh by local hour; use the real values from the tariff sheet you cite) and then set
      CFG.CAISO_PRICE_FILTERS = {"NODE": "TOU_TARIFF"} in master.ipynb.
Run steps separately with --only nsrdb | load | price | tou | pwp.
  --only pwp writes the real PWP Schedule M-1 time-of-use tariff (Ordinance 7305, eff. July 2017).
"""
import argparse, io, sys, time, zipfile
from pathlib import Path
import numpy as np
import pandas as pd
import requests

SITES = {"caltech": (34.1377, -118.1253), "jpl": (34.2013, -118.1714)}
YEARS = [2017, 2018, 2019]
OASIS = "http://oasis.caiso.com/oasisapi/SingleZip"
OUT = Path("data")


# ----------------------------------------------------------------------------- NSRDB
def get_nsrdb(api_key, email):
    from pvlib import iotools
    (OUT / "nsrdb").mkdir(parents=True, exist_ok=True)
    for site, (lat, lon) in SITES.items():
        for yr in YEARS:
            f = OUT / "nsrdb" / f"{site}_{yr}.csv"
            if f.exists():
                print("exists:", f); continue
            print(f"NSRDB {site} {yr} ...", flush=True)
            data, meta = iotools.get_nsrdb_psm4_aggregated(
                lat, lon, api_key, email, year=yr, time_step=30,
                parameters=["ghi", "air_temperature"], utc=False, map_variables=True, timeout=120)
            tz = float(meta.get("Time Zone", -8))
            idx = data.index.tz_localize(None) if data.index.tz is not None else data.index
            body = pd.DataFrame({"Year": idx.year, "Month": idx.month, "Day": idx.day, "Hour": idx.hour,
                                 "Minute": idx.minute, "GHI": data["ghi"].values,
                                 "Temperature": data["temp_air"].values})
            hdr = pd.DataFrame([["NSRDB PSM4 GOES aggregated", meta.get("Location ID", ""), lat, lon, tz,
                                 meta.get("Elevation", "")]],
                               columns=["Source", "Location ID", "Latitude", "Longitude", "Time Zone", "Elevation"])
            with open(f, "w", newline="") as fh:
                hdr.to_csv(fh, index=False)
                fh.write(",".join(body.columns) + "\n")
                body.to_csv(fh, index=False, header=False)
            print(f"  -> {f} ({len(body)} rows, GHI max {body.GHI.max():.0f} W/m2, time zone {tz})")
            time.sleep(2)


# ----------------------------------------------------------------------------- CAISO OASIS
def oasis_month(params, start, end, tries=6):
    q = dict(params, startdatetime=start.strftime("%Y%m%dT%H:%M-0000"),
             enddatetime=end.strftime("%Y%m%dT%H:%M-0000"), resultformat=6)
    for k in range(tries):
        r = requests.get(OASIS, params=q, timeout=120)
        if r.status_code == 429:
            time.sleep(20 * (k + 1)); continue
        r.raise_for_status()
        z = zipfile.ZipFile(io.BytesIO(r.content))
        name = z.namelist()[0]
        raw = z.read(name)
        if name.lower().endswith(".xml") or b"INVALID_REQUEST" in raw[:2000] or b"ERR_CODE" in raw[:2000]:
            msg = raw[:600].decode(errors="ignore")
            if "1015" in msg or "too many" in msg.lower():
                time.sleep(20 * (k + 1)); continue
            raise RuntimeError(f"OASIS error for {params.get('queryname')} {start:%Y-%m}: {msg}")
        return pd.read_csv(io.BytesIO(raw))
    raise RuntimeError(f"OASIS kept rate-limiting {params.get('queryname')} {start:%Y-%m}")


def get_price_2019():
    """Tries the OASIS API for 2019 DAM prices. Expected to fail (39-month retention); kept so the error is explicit."""
    (OUT / "caiso").mkdir(parents=True, exist_ok=True)
    f = OUT / "caiso" / "lmp_2019.csv"
    if f.exists():
        print("exists:", f); return
    p = dict(queryname="PRC_LMP", market_run_id="DAM", node="TH_SP15_GEN-APND", version=12)
    a = pd.Timestamp("2019-01-01 08:00", tz="UTC")
    try:
        df = oasis_month(p, a, a + pd.Timedelta(days=1))
        print("OASIS still serves 2019; downloading the full year ...")
    except Exception as exc:
        print("\nOASIS has no 2019 prices (it keeps only the last 39 months).\n"
              "Use option (a) CAISO Historical OASIS Data Downloader, or option (b) --only tou. See the top of this file.\n"
              f"OASIS said: {str(exc)[:300]}")
        return
    months = [pd.Timestamp(f"2019-{m:02d}-01 08:00", tz="UTC") for m in range(1, 13)] + [pd.Timestamp("2020-01-01 08:00", tz="UTC")]
    frames = []
    for s_, e_ in zip(months[:-1], months[1:]):
        frames.append(oasis_month(p, s_, e_)); print(f"price {s_:%Y-%m} ok", flush=True); time.sleep(6)
    pd.concat(frames, ignore_index=True).to_csv(f, index=False)
    print("  ->", f)


def get_load_eia930():
    """EIA-930 hourly demand for the CAISO balancing authority (CISO), 2017-2019, saved in OASIS column format."""
    (OUT / "caiso").mkdir(parents=True, exist_ok=True)
    f = OUT / "caiso" / "load_2017_2019.csv"
    if f.exists():
        print("exists:", f); return
    frames = []
    for yr in YEARS:
        for half, tag in [(1, "Jan_Jun"), (2, "Jul_Dec")]:
            df = None
            urls = [f"https://www.eia.gov/electricity/gridmonitor/sixMonthFiles/EIA930_BALANCE_{yr}_{tag}.csv",
                    f"https://zenodo.org/records/17119802/files/eia930-{yr}half{half}.zip"]
            for url in urls:
                try:
                    r = requests.get(url, timeout=300)
                    r.raise_for_status()
                    if url.endswith(".zip"):
                        z = zipfile.ZipFile(io.BytesIO(r.content))
                        name = next(n for n in z.namelist() if "BALANCE" in n.upper() and n.lower().endswith(".csv"))
                        raw = z.read(name)
                    else:
                        raw = r.content
                    df = parse_eia930(raw)
                    print(f"EIA-930 {yr} H{half}: {len(df)} hours from {url.split('/')[2]}", flush=True)
                    break
                except Exception as exc:
                    print(f"  {url} failed: {str(exc)[:150]}")
            if df is None:
                raise RuntimeError(f"EIA-930 {yr} H{half} could not be downloaded. Get the 'Balance' six-month file "
                                   "from https://www.eia.gov/electricity/gridmonitor/ and rerun with --eia-dir.")
            frames.append(df)
    write_load(pd.concat(frames), f)


def parse_eia930(raw):
    df = pd.read_csv(io.BytesIO(raw), thousands=",", low_memory=False)
    df.columns = [c.strip() for c in df.columns]
    ba = next(c for c in df.columns if c.lower().startswith("balancing authority"))
    tcol = next(c for c in df.columns if "utc time at end of hour" in c.lower())
    dcols = [c for c in df.columns if c.lower().startswith("demand (mw)")]
    dcol = next((c for c in dcols if "adjusted" in c.lower()), dcols[0])      # prefer EIA's cleaned series
    df = df[df[ba].astype(str).str.strip() == "CISO"]
    t_end = pd.to_datetime(df[tcol], format="mixed", utc=True)
    out = pd.DataFrame({"t_start_utc": t_end - pd.Timedelta(hours=1),
                        "MW": pd.to_numeric(df[dcol], errors="coerce").values,
                        "source_column": dcol})
    return out.dropna(subset=["MW"])


def write_load(df, f):
    df = df.sort_values("t_start_utc").drop_duplicates("t_start_utc")
    out = pd.DataFrame({"INTERVALSTARTTIME_GMT": df.t_start_utc.dt.strftime("%Y-%m-%dT%H:%M:%S-00:00"),
                        "TAC_AREA_NAME": "CA ISO-TAC", "XML_DATA_ITEM": "SYS_FCST_ACT_MW",
                        "SOURCE": "EIA-930 CISO " + df.source_column.astype(str), "MW": df.MW.round(1)})
    out.to_csv(f, index=False)
    mw = df.MW
    print(f"  -> {f}: {len(out)} hours, {df.t_start_utc.min():%Y-%m-%d} .. {df.t_start_utc.max():%Y-%m-%d}, "
          f"mean {mw.mean():,.0f} MW, max {mw.max():,.0f} MW (CAISO is ~20-50 GW; ~100 GW would mean double counting)")


def write_tou(spec, source):
    """spec like '0-8:0.10,8-16:0.13,16-21:0.25,21-24:0.10' in $/kWh by LOCAL hour (Pacific standard time)."""
    (OUT / "caiso").mkdir(parents=True, exist_ok=True)
    rate = np.full(24, np.nan)
    for part in spec.split(","):
        hrs, val = part.split(":")
        h0, h1 = (int(x) for x in hrs.split("-"))
        rate[h0:h1] = float(val)
    if np.isnan(rate).any():
        sys.exit(f"--tou does not cover all 24 hours: {rate}")
    t = pd.date_range("2017-01-01", "2019-12-31 23:00", freq="h", tz="Etc/GMT+8")
    out = pd.DataFrame({"INTERVALSTARTTIME_GMT": t.tz_convert("UTC").strftime("%Y-%m-%dT%H:%M:%S-00:00"),
                        "NODE": "TOU_TARIFF", "LMP_TYPE": "LMP", "MARKET_RUN_ID": "DAM",
                        "SOURCE": source, "MW": rate[t.hour] * 1000})           # $/kWh -> $/MWh, OASIS column name
    f = OUT / "caiso" / "lmp_tou_tariff.csv"
    out.to_csv(f, index=False)
    print(f"  -> {f}  ($/MWh by hour: { {h: float(v) for h, v in enumerate((rate * 1000).round(1))} })\n"
          "  Now set CFG.CAISO_PRICE_FILTERS = {'NODE': 'TOU_TARIFF'} in master.ipynb, and cite the tariff in the paper.")


# PWP Schedule M-1 (Medium Commercial & Industrial, 30-299 kW), Energy Services Charge, Time-of-Use option.
# Source: City of Pasadena Ordinance No. 7305 (June 19, 2017), Sec. 13.04.060, "Effective July 2017";
# no further rate steps are scheduled in that ordinance for 2018-2019.
PWP_M1_2017 = {"summer_on": 0.10218, "summer_off": 0.06063, "winter_on": 0.06578, "winter_off": 0.05785}


def _pwp_holidays(years):
    """Holidays named in Ordinance 7305 (all hours off-peak)."""
    from pandas.tseries.holiday import (AbstractHolidayCalendar, Holiday, USMartinLutherKingJr,
                                        USPresidentsDay, USMemorialDay, USLaborDay, USThanksgivingDay)
    class PWP(AbstractHolidayCalendar):
        rules = [Holiday("New Year", month=1, day=1), USMartinLutherKingJr,
                 Holiday("Lincoln", month=2, day=12), USPresidentsDay, USMemorialDay,
                 Holiday("Independence", month=7, day=4), USLaborDay, Holiday("Veterans", month=11, day=11),
                 USThanksgivingDay, Holiday("Christmas", month=12, day=25)]
    days = PWP().holidays(f"{min(years)}-01-01", f"{max(years)}-12-31")
    tg = [d for d in days if d.month == 11 and d.dayofweek == 3 and 22 <= d.day <= 28]
    return set(days.date) | {(d + pd.Timedelta(days=1)).date() for d in tg}


def write_pwp_m1():
    """Hourly PWP M-1 TOU energy charge, 2017-2019, using LOCAL clock time (PST/PDT) as the tariff does."""
    (OUT / "caiso").mkdir(parents=True, exist_ok=True)
    t_utc = pd.date_range("2017-01-01 08:00", "2020-01-01 07:00", freq="h", tz="UTC")
    loc = t_utc.tz_convert("America/Los_Angeles")
    hol = _pwp_holidays(YEARS)
    summer = loc.month.isin([6, 7, 8, 9])
    weekday = (loc.dayofweek < 5) & ~pd.Index(loc.date).isin(hol)
    h = loc.hour
    on = weekday & np.where(summer, (h >= 12) & (h < 20), (h >= 6) & (h < 22))
    r = PWP_M1_2017
    rate = np.where(summer, np.where(on, r["summer_on"], r["summer_off"]), np.where(on, r["winter_on"], r["winter_off"]))
    out = pd.DataFrame({"INTERVALSTARTTIME_GMT": t_utc.strftime("%Y-%m-%dT%H:%M:%S-00:00"),
                        "NODE": "TOU_TARIFF", "LMP_TYPE": "LMP", "MARKET_RUN_ID": "DAM",
                        "SOURCE": "PWP Schedule M-1 TOU energy services charge, Ordinance 7305 (eff. July 2017)",
                        "MW": rate * 1000})
    f = OUT / "caiso" / "lmp_tou_tariff.csv"
    out.to_csv(f, index=False)
    chk = pd.DataFrame({"local": loc, "rate": rate})
    print(f"  -> {f}: {len(out)} hours")
    for label, ts in [("summer weekday (2019-07-17)", "2019-07-17"), ("winter weekday (2019-01-16)", "2019-01-16"),
                      ("summer Saturday (2019-07-20)", "2019-07-20"), ("Thanksgiving (2019-11-28)", "2019-11-28")]:
        d = chk[chk.local.dt.strftime("%Y-%m-%d") == ts]
        print(f"  {label}: " + " ".join(f"{t:%H}h={v:.5f}" for t, v in zip(d.local, d.rate) if t.hour in (5, 6, 11, 12, 19, 20, 21, 22)))
    print("  Now set CFG.CAISO_PRICE_FILTERS = {'NODE': 'TOU_TARIFF'} in master.ipynb (already set in the new version).")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--api-key", help="free NREL developer key (needed for NSRDB)")
    ap.add_argument("--email", help="email registered with the NREL key")
    ap.add_argument("--only", choices=["nsrdb", "load", "price", "tou", "pwp"])
    ap.add_argument("--tou", help="time-of-use $/kWh by local hour, e.g. '0-8:0.10,8-16:0.13,16-21:0.25,21-24:0.10'")
    ap.add_argument("--tou-source", default="site TOU tariff (cite in paper)")
    a = ap.parse_args()
    if a.only == "pwp":
        write_pwp_m1(); sys.exit(0)
    if a.only == "tou":
        if not a.tou:
            sys.exit("--only tou needs --tou with the real tariff values")
        write_tou(a.tou, a.tou_source); sys.exit(0)
    if a.only in (None, "nsrdb"):
        if not (a.api_key and a.email):
            sys.exit("NSRDB needs --api-key and --email (free key: https://developer.nrel.gov/signup/)")
        get_nsrdb(a.api_key, a.email)
    if a.only in (None, "load"):
        get_load_eia930()
    if a.only in (None, "price"):
        get_price_2019()
    print("\nDone. Next: open master.ipynb and Run All (QUICK = True first).")