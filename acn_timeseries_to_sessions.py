"""
Convert ACN-Data-Static per-session time-series files into the session CSV that master.ipynb reads.

Usage (from a terminal, not inside Jupyter, so it can use all CPU cores):
    python acn_timeseries_to_sessions.py --root "D:/RESEARCH PAPERS/EV-PLATFORM-OPTIMIZATION/Project/ACN-Data-Static" ^
                                         --out ./data/acn --year 2019

It writes, for each site folder found under "time series data/":
    <out>/<site>_<year>.csv          sessions with connectionTime, disconnectTime, kWhDelivered, peak_power_kw, ...
    <out>/<site>_<year>_CHECK.txt    timezone and data-quality report. READ IT before running master.ipynb.

Energy: the final "Energy Delivered (kWh)" value when it is logged. When it is missing or zero (common at JPL),
energy is integrated from Charging Current x Voltage (the measured voltage column, or 208 V if that is empty too).
The share of integrated sessions is reported so you can disclose it in the paper.
"""
import argparse, gzip, io, os, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import numpy as np
import pandas as pd

IDLE_KW = 0.15
DEFAULT_V = 208.0
_trap = getattr(np, "trapezoid", None) or np.trapz   # numpy 1.x and 2.x


def summarize(path):
    try:
        df = pd.read_csv(path, compression="gzip")
    except Exception as exc:
        return {"file": str(path), "error": f"read: {exc}"}
    if df.empty:
        return {"file": str(path), "error": "empty"}
    raw_ts = df.iloc[:, 0].astype(str)
    ts = pd.to_datetime(raw_ts, errors="coerce", utc=False, format="mixed")
    ok = ts.notna()
    if ok.sum() < 2:
        return {"file": str(path), "error": "timestamps"}
    df, ts, raw_ts = df[ok], ts[ok], raw_ts[ok]
    tz_aware = getattr(ts.dt, "tz", None) is not None
    if tz_aware:
        ts = ts.dt.tz_convert("UTC").dt.tz_localize(None)

    def col(name):
        for c in df.columns:
            if c.strip().lower().startswith(name.lower()):
                return pd.to_numeric(df[c], errors="coerce")
        return None

    energy, power, current, volt = col("Energy Delivered"), col("Power"), col("Charging Current"), col("Voltage")
    hrs = (ts - ts.iloc[0]).dt.total_seconds().values / 3600
    kwh_logged = float(energy.max()) if energy is not None and energy.notna().any() else np.nan
    v = volt.where(volt > 50) if volt is not None else None
    v_used = v.fillna(DEFAULT_V) if v is not None else pd.Series(DEFAULT_V, index=df.index)
    if power is not None and power.notna().any():
        p_kw = power.fillna(0).clip(lower=0)
    elif current is not None:
        p_kw = (current.fillna(0).clip(lower=0) * v_used / 1000)
    else:
        p_kw = None
    kwh_integrated = float(_trap(p_kw.values, hrs)) if p_kw is not None and len(hrs) > 1 else np.nan
    if np.isfinite(kwh_logged) and kwh_logged > 0.05:
        kwh, source = kwh_logged, "logged"
    elif np.isfinite(kwh_integrated) and kwh_integrated > 0:
        kwh, source = kwh_integrated, "integrated_current_x_voltage"
    else:
        kwh, source = np.nan, "none"
    active = (p_kw > IDLE_KW) if p_kw is not None else pd.Series(False, index=df.index)
    parts = Path(path).parts
    return {"file": str(path), "sessionID": Path(path).name.replace(".csv.gz", ""),
            "site": parts[-3], "location": parts[-2],
            "connectionTime": ts.iloc[0], "disconnectTime": ts.iloc[-1],
            "doneChargingTime": ts[active].iloc[-1] if active.any() else pd.NaT,
            "kWhDelivered": kwh, "energy_source": source,
            "kwh_logged": kwh_logged, "kwh_integrated": kwh_integrated,
            "peak_power_kw": float(p_kw.max()) if p_kw is not None else np.nan,
            "raw_first_timestamp": raw_ts.iloc[0], "tz_aware_in_file": tz_aware, "error": None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="ACN-Data-Static folder (contains 'time series data')")
    ap.add_argument("--out", default="./data/acn")
    ap.add_argument("--year", type=int, default=2019)
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    a = ap.parse_args()
    base = Path(a.root) / "time series data"
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    sites = sorted(p.name for p in base.iterdir() if p.is_dir())
    print("site folders found:", sites)
    for site in sites:
        files = sorted((base / site).rglob("*.csv.gz"))
        print(f"\n[{site}] {len(files):,} files, {a.workers} workers ...")
        t0 = time.time()
        with ProcessPoolExecutor(a.workers) as ex:
            rows = list(ex.map(summarize, files, chunksize=64))
        df = pd.DataFrame(rows)
        bad = df[df.error.notna()]
        df = df[df.error.isna()].copy()
        print(f"[{site}] parsed in {time.time() - t0:.0f}s, {len(bad):,} unreadable")
        tz_aware = bool(df.tz_aware_in_file.any())
        yr = df[(df.connectionTime.dt.year == a.year) & df.kWhDelivered.notna() & (df.kWhDelivered > 0.1)].copy()
        dwell = (yr.disconnectTime - yr.connectionTime).dt.total_seconds() / 3600
        yr = yr[(dwell >= 0.25) & (dwell <= 72)].sort_values("connectionTime")
        keep = ["sessionID", "site", "location", "connectionTime", "disconnectTime", "doneChargingTime",
                "kWhDelivered", "peak_power_kw", "energy_source"]
        f_out = out / f"{site}_{a.year}.csv"
        yr[keep].to_csv(f_out, index=False)
        # ---- timezone check: workplace arrivals should peak in the morning LOCAL time
        hrs = yr.connectionTime.dt.hour.value_counts().sort_index()
        peak_hr = int(hrs.idxmax()) if len(hrs) else -1
        if tz_aware:
            verdict = "Timestamps carry a UTC offset -> converted to UTC. Set CFG.ACN_CSV_TZ = 'UTC'."
        elif 6 <= peak_hr <= 10:
            verdict = ("Naive timestamps with arrivals peaking at %02d:00 -> they look LOCAL (Pacific). "
                       "Set CFG.ACN_CSV_TZ = 'America/Los_Angeles'." % peak_hr)
        elif 13 <= peak_hr <= 18:
            verdict = ("Naive timestamps with arrivals peaking at %02d:00 -> they look like UTC "
                       "(08:00 Pacific = 15/16:00 UTC). Set CFG.ACN_CSV_TZ = 'UTC'." % peak_hr)
        else:
            verdict = f"Arrival peak at {peak_hr:02d}:00 is unusual. Inspect the raw timestamps before continuing."
        rep = [f"site: {site} | year: {a.year}", f"files: {len(files):,} | unreadable: {len(bad):,}",
               f"sessions in {a.year} (kWh > 0.1, 15 min <= dwell <= 72 h): {len(yr):,}",
               f"sessions per day (mean): {len(yr) / max(yr.connectionTime.dt.normalize().nunique(), 1):.1f}",
               f"energy source: {yr.energy_source.value_counts().to_dict()}",
               f"logged vs integrated where both exist: median abs error "
               f"{(100 * (yr.kwh_integrated - yr.kwh_logged).abs() / yr.kwh_logged).where(yr.kwh_logged > 0.5).median():.2f}%",
               f"peak power kW: median {yr.peak_power_kw.median():.2f}, p99 {yr.peak_power_kw.quantile(0.99):.2f}",
               f"example raw timestamp: {df.raw_first_timestamp.iloc[0]!r}",
               f"arrival-hour histogram (as stored): {hrs.to_dict()}",
               "", "TIMEZONE VERDICT: " + verdict]
        (out / f"{site}_{a.year}_CHECK.txt").write_text("\n".join(rep))
        print("\n".join(rep))
        print("->", f_out)


if __name__ == "__main__":
    main()
