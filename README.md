# Decentralized, Network-Feasible Charging of Solar-Integrated EV Fleets with Online-Calibrated Forecast Margins

Code and results accompanying the manuscript

> G. Kumar, "Decentralized, Network-Feasible Charging of Solar-Integrated Electric Vehicle Fleets with Online-Calibrated Forecast Margins," submitted to *IEEE Transactions on Smart Grid*, 2026.

This repository reproduces every table and figure of the paper from public data with one Jupyter notebook.

---

## Overview

Workplace EV charging sites with on-site photovoltaics (PV) must schedule charging against uncertain day-ahead forecasts of solar output and feeder load while respecting transformer, branch and voltage limits. The framework combines:

1. **Day-ahead forecasting.** LightGBM point and quantile models for global horizontal irradiance (GHI) and system load at 1 h and day-ahead horizons. Every lagged input is at least one horizon old, and this is asserted in code.
2. **One-sided conformal margins.** Load upper and PV lower bounds, recalibrated every midnight with one of four rules: static, expanding, rolling (the main rule, fixed a priori) and adaptive conformal inference (ACI).
3. **Network limit.** LinDistFlow model of the IEEE 33-bus feeder (garage at bus 17) with voltage, branch and 150 kW transformer limits.
4. **Decentralized ADMM protocol.** EV agents keep their departure times and energy needs local; a coordinator broadcasts congestion prices.
5. **Evaluation.** Full year 2019, two sites (Caltech and JPL, 37,022 real sessions). Six benchmark methods: uncontrolled, EDF, LLF, MPC-point, MPC-conformal and an offline perfect-foresight optimum. Includes AC power-flow screening (pandapower), stress tests, a large-hub scenario, a smoothing ablation, day-paired statistics and 29 automated validation checks.

---

## Repository contents

```
.
├── README.md
├── LICENSE
├── requirements.txt
├── master.ipynb                     # runs all experiments (E1–E7, W9) and writes all tables and figures
├── download_inputs.py               # downloads/prepares NSRDB, EIA-930 load and the PWP tariff
├── acn_timeseries_to_sessions.py    # converts ACN-Data per-session time series into session tables
├── cells/
│   ├── smoothing_ablation_cell.py   # E8: explicit-smoothing ablation (Table V, smoothed-MPC rows)
│   └── paper_figs_cell.py           # optional: re-draws Figs. 2 and 4 in publication style
└── master_outputs/                  # results of the full run used in the paper
    ├── _combined/                   # CSV tables for both sites
    ├── caltech/                     # site-level figures
    └── jpl/
```

Raw datasets are **not** redistributed here (see [Data](#data)). The scripts download or prepare them.

---

## Data

All inputs are public. Each must be obtained from its provider under that provider's terms.

| Input | Source | Period / resolution | Used for | How to obtain |
|---|---|---|---|---|
| EV charging sessions (Caltech, JPL) | **ACN-Data**, Caltech Adaptive Charging Network — <https://ev.caltech.edu/dataset> | 2019, per-session time series | Arrivals, departures, energy, peak power | Register on the ACN-Data portal, download the per-session time-series files, then run `acn_timeseries_to_sessions.py` |
| Solar irradiance and temperature | **NREL National Solar Radiation Database (NSRDB)**, PSM v4 GOES aggregated — <https://nsrdb.nrel.gov/> | 2017–2019, 30 min | PV forecasting and PV power | `download_inputs.py --only nsrdb` (needs a free API key: <https://developer.nrel.gov/signup/>) |
| System load (CAISO balancing authority, `CISO`) | **U.S. EIA Hourly Electric Grid Monitor, Form EIA-930** — <https://www.eia.gov/electricity/gridmonitor/> | 2017–2019, hourly | Load forecasting; feeder load shape | `download_inputs.py --only load` |
| Energy price | **Pasadena Water and Power (PWP), Schedule M-1** time-of-use energy services charge, Ordinance No. 7305 (effective 1 July 2017). City Council agenda, 12 June 2017: <https://ww2.cityofpasadena.net/2017%20Agendas/Jun_12_17/AR%2016%20ORDINANCE.pdf> | 2019, hourly TOU | Energy cost of charging | `download_inputs.py --only pwp` (writes the published rates) |
| Distribution feeder | **IEEE 33-bus test system** (Baran and Wu, 1989), via pandapower | — | Network limits and AC power flow | Built into pandapower; no download |

Site coordinates used for NSRDB: Caltech (34.1377, −118.1253) and JPL (34.2013, −118.1714). All time series are converted to fixed UTC−8.

**Data citations**
- Z. J. Lee, T. Li, and S. H. Low, "ACN-Data: Analysis and applications of an open EV charging dataset," *Proc. ACM e-Energy*, 2019, pp. 139–149.
- M. Sengupta *et al.*, "The National Solar Radiation Data Base (NSRDB)," *Renew. Sustain. Energy Rev.*, vol. 89, pp. 51–60, 2018.
- U.S. Energy Information Administration, Hourly Electric Grid Monitor (Form EIA-930).
- M. E. Baran and F. F. Wu, "Network reconfiguration in distribution systems for loss reduction and load balancing," *IEEE Trans. Power Del.*, vol. 4, no. 2, pp. 1401–1407, 1989.

---

## Installation

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
python -m venv .venv
# Windows: .venv\Scripts\activate      Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`:

```
numpy
pandas
scipy
scikit-learn
matplotlib
lightgbm
pvlib
pandapower
numba
tabulate
requests
tqdm
jupyter
```

`numba` is optional but makes the AC power flow much faster.

---

## Reproducing the results

### 1. Prepare the EV sessions

Download the ACN-Data per-session time-series files for Caltech and JPL, then run:

```bash
python acn_timeseries_to_sessions.py --root "<path>/ACN-Data-Static" --out ./data/acn --year 2019
```

This writes `data/acn/<site>_2019.csv` and a data-quality report `data/acn/<site>_2019_CHECK.txt` for each site. Read the report before continuing.

### 2. Download weather, load and tariff

```bash
python download_inputs.py --only nsrdb --api-key YOUR_NREL_KEY --email you@example.com
python download_inputs.py --only load
python download_inputs.py --only pwp
```

Keep your NREL API key private. Pass it on the command line and never commit it to the repository.

Expected layout:

```
data/
├── acn/      caltech_2019.csv, jpl_2019.csv
├── nsrdb/    caltech_2017.csv … jpl_2019.csv
└── caiso/    load_2017_2019.csv, lmp_tou_tariff.csv
```

### 3. Run the experiments

Open `master.ipynb` and run all cells. Key settings in the configuration cell:

| Setting | Paper value | Meaning |
|---|---|---|
| `QUICK` | `False` | `True` runs 24 days (about 15 min) for a first test; `False` runs the full year |
| `SEED` | `42` | Random seed |
| `MAIN_CONFORMAL_MODE` | `"rolling"` | Margin rule for the main comparison (fixed a priori) |
| `CAISO_PRICE_FILTERS` | `{"NODE": "TOU_TARIFF"}` | Use the PWP time-of-use tariff |
| `EVSE_MAX_KW` | `19.2` | Charger hardware limit (kW) |

The full run takes about 1–3 h on a laptop, depending on the machine. Results are written to `master_outputs/`.

### 4. Smoothing ablation (Table V, smoothed-MPC rows)

In the same notebook session, paste `cells/smoothing_ablation_cell.py` as a new cell and run it. The default (JPL, two variants) takes about 10–30 min. It writes `E8_smoothing_ablation.csv` and `E8_smoothing_ablation.png`.

---

## Where each result comes from

| Paper item | File in `master_outputs/_combined/` |
|---|---|
| Table I — data and setup | `E1_dataset_statistics.csv` |
| Table II — forecast accuracy | `E6_forecast_metrics.csv` |
| Table III, Fig. 5 — full-year comparison | `E4_main_summary.csv`, `E4_main_daily.csv` |
| Table IV, Figs. 3 and 6 — margin rules and coverage | `E5_ablation_summary.csv`, `E5_monthly_coverage_by_mode.csv` |
| Table V — source of the safety edge | `E4b_fairness_tight_admm_vs_mpc.csv`, `E8_smoothing_ablation.csv` |
| Table VI, Fig. 8 — large hub | `E2b_large_hub.csv` |
| Table VII — stress tests | `E2_stress_tests.csv` |
| Table VIII — paired statistics | `E7_paired_statistics.csv` |
| Table IX — validation checks | `W9_red_team_checks.csv` |
| Fig. 7 — ADMM optimality and scalability | `E3_admm_vs_lp_gap.csv`, `E3_admm_residual_traces.csv`, `E3_scalability_synthetic_contexts.csv` |
| Network-model validation | `E2_network_validation.csv` |
| Leakage audit | `E6_leakage_audit.csv` |
| Run configuration and environment | `run_manifest.json` |

---

## Assumptions and limitations

- The distribution network is the IEEE 33-bus **test** feeder. The PV array (100 kWp) and the 150 kW transformer are assumed sizes.
- Drivers are assumed to declare their true departure time and energy need at plug-in. This assumption is the same for all methods.
- Cost includes the per-kWh energy services charge only; demand charges are not modelled.
- Both sites share the CAISO load and the tariff, so they represent two demand patterns rather than two climates.

See Section VII of the paper for the full list.

---

## Citation

If you use this code, please cite the paper (citation details will be updated on publication):

```bibtex
@article{kumar2026decentralized,
  author  = {Kumar, Golu},
  title   = {Decentralized, Network-Feasible Charging of Solar-Integrated Electric Vehicle Fleets
             with Online-Calibrated Forecast Margins},
  journal = {IEEE Transactions on Smart Grid},
  year    = {2026},
  note    = {Submitted}
}
```

---

## License

The code in this repository is released under the [MIT License](LICENSE). The datasets listed above are **not** covered by this license; they remain subject to the terms of their providers.

## Contact

Golu Kumar — Department of Computer Science, Jodhpur Institute of Engineering and Technology, Jodhpur, Rajasthan, India
golukumar.research01@gmail.com
