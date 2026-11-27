# Results summary (REAL DATA)

## E1 data
| site    |   sessions_raw_file |   sessions_in_test_year |   days_with_sessions |   sessions_per_day_mean |   sessions_per_weekday_mean |   peak_concurrent_EVs |   energy_kwh_total |   energy_kwh_mean |   dwell_h_median |   share_energy_clipped_to_feasible_pct | first_arrival       | last_arrival        |
|:--------|--------------------:|------------------------:|---------------------:|------------------------:|----------------------------:|----------------------:|-------------------:|------------------:|-----------------:|---------------------------------------:|:--------------------|:--------------------|
| caltech |               20377 |                   19977 |                  365 |                    54.7 |                        64.2 |                    51 |             215238 |             10.77 |             4.81 |                                  15.72 | 2019-01-01 09:41:48 | 2019-12-31 14:28:08 |
| jpl     |               17076 |                   17045 |                  352 |                    48.4 |                        64.8 |                    52 |             252900 |             14.84 |             8.38 |                                   5.05 | 2019-01-01 17:00:51 | 2019-12-31 14:17:16 |

## E6 forecasting (test year)
| site    | target   | horizon   | model                   | eval_rows    |      RMSE |       MAE |      MBE |   nRMSE_pct |   skill_vs_persistence |       R2 |   coverage_pct |   mean_width |   winkler |
|:--------|:---------|:----------|:------------------------|:-------------|----------:|----------:|---------:|------------:|-----------------------:|---------:|---------------:|-------------:|----------:|
| caltech | pv       | 1h        | LightGBM                | daytime only |   79.4008 |   41.5338 |   8.9701 |     16.8659 |                 0.0431 |   0.9279 |       nan      |      nan     |   nan     |
| caltech | pv       | 1h        | smart persistence       | daytime only |   82.9746 |   46.2315 |   3.3009 |     17.625  |                 0      |   0.9213 |       nan      |      nan     |   nan     |
| caltech | pv       | 1h        | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        87.9149 |      173.566 |   341.774 |
| caltech | pv       | 1h        | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        93.5937 |      189.89  |   330.307 |
| caltech | pv       | day_ahead | LightGBM                | daytime only |  157.907  |   96.3708 |  11.9547 |     33.5417 |                 0.1319 |   0.7148 |       nan      |      nan     |   nan     |
| caltech | pv       | day_ahead | smart persistence       | daytime only |  181.895  |   96.6298 |  -1.9248 |     38.6371 |                 0      |   0.6216 |       nan      |      nan     |   nan     |
| caltech | pv       | day_ahead | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        80.5489 |      292.286 |   666.012 |
| caltech | pv       | day_ahead | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        95.8249 |      436.58  |   588.414 |
| caltech | load     | 1h        | LightGBM                | all          |  747.48   |  352.265  | 183      |      3.0575 |                 0.6422 |   0.9764 |       nan      |      nan     |   nan     |
| caltech | load     | 1h        | day persistence         | all          | 2089.31   | 1376.88   |   0.9662 |      8.5463 |                 0      |   0.8157 |       nan      |      nan     |   nan     |
| caltech | load     | 1h        | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        75.9218 |     1492.28  |  6162.42  |
| caltech | load     | 1h        | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        83.7643 |     1726.37  |  5472.48  |
| caltech | load     | day_ahead | LightGBM                | all          | 1557.41   | 1052.48   | 619.608  |      6.3705 |                 0.2546 |   0.8976 |       nan      |      nan     |   nan     |
| caltech | load     | day_ahead | day persistence         | all          | 2089.31   | 1376.88   |   0.9662 |      8.5463 |                 0      |   0.8157 |       nan      |      nan     |   nan     |
| caltech | load     | day_ahead | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        65.9275 |     2546.96  | 15056.4   |
| caltech | load     | day_ahead | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        82.9595 |     3702.43  | 10615.3   |
| jpl     | pv       | 1h        | LightGBM                | daytime only |   70.5593 |   38.0699 |   7.1806 |     15.1701 |                 0.0473 |   0.9442 |       nan      |      nan     |   nan     |
| jpl     | pv       | 1h        | smart persistence       | daytime only |   74.0596 |   42.5958 |   5.9269 |     15.9226 |                 0      |   0.9385 |       nan      |      nan     |   nan     |
| jpl     | pv       | 1h        | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        89.809  |      178.469 |   297.426 |
| jpl     | pv       | 1h        | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        94.2393 |      190.555 |   291.469 |
| jpl     | pv       | day_ahead | LightGBM                | daytime only |  164.708  |  104.834  |   7.5265 |     35.4118 |                 0.1158 |   0.6958 |       nan      |      nan     |   nan     |
| jpl     | pv       | day_ahead | smart persistence       | daytime only |  186.282  |   99.3995 |  -1.8333 |     40.0501 |                 0      |   0.6109 |       nan      |      nan     |   nan     |
| jpl     | pv       | day_ahead | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        80.9666 |      317.852 |   616.858 |
| jpl     | pv       | day_ahead | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        95.6185 |      417.004 |   556.859 |
| jpl     | load     | 1h        | LightGBM                | all          |  748.105  |  353.683  | 177.147  |      3.0601 |                 0.6419 |   0.9764 |       nan      |      nan     |   nan     |
| jpl     | load     | 1h        | day persistence         | all          | 2089.31   | 1376.88   |   0.9662 |      8.5463 |                 0      |   0.8157 |       nan      |      nan     |   nan     |
| jpl     | load     | 1h        | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        75.2169 |     1532.64  |  6342.29  |
| jpl     | load     | 1h        | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        82.7825 |     1749.97  |  5663.51  |
| jpl     | load     | day_ahead | LightGBM                | all          | 1558.61   | 1053.75   | 597.919  |      6.3755 |                 0.254  |   0.8974 |       nan      |      nan     |   nan     |
| jpl     | load     | day_ahead | day persistence         | all          | 2089.31   | 1376.88   |   0.9662 |      8.5463 |                 0      |   0.8157 |       nan      |      nan     |   nan     |
| jpl     | load     | day_ahead | interval: raw quantiles | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        66.0217 |     2500.39  | 14918.3   |
| jpl     | load     | day_ahead | interval: CQR           | nan          |  nan      |  nan      | nan      |    nan      |               nan      | nan      |        82.5314 |     3581.2   | 10698     |

## E2 network validation
| site    |   base_load_scale |   loss_margin_v2 |   linDistFlow_minus_AC_vmin_mean |   linDistFlow_minus_AC_vmin_p95 |   linDistFlow_minus_AC_vmin_max |   screen_margin | screen_is_safe   |   test_base_min_voltage |   test_steps_base_below_vmin |   garage_bus |   transformer_kw |   voltage_sensitivity_pu_per_100kW_at_garage |
|:--------|------------------:|-----------------:|---------------------------------:|--------------------------------:|--------------------------------:|----------------:|:-----------------|------------------------:|-----------------------------:|-------------:|-----------------:|---------------------------------------------:|
| caltech |           0.54621 |          0.00144 |                          0.00029 |                         0.00052 |                         0.00078 |            0.01 | True             |                 0.96057 |                            0 |           17 |              150 |                                       0.0069 |
| jpl     |           0.54621 |          0.00144 |                          0.00029 |                         0.00052 |                         0.00078 |            0.01 | True             |                 0.96057 |                            0 |           17 |              150 |                                       0.0069 |

## E4 main comparison
| site    | method         |   days |   energy_served_pct |   sessions_fully_served_pct |   cost_per_kwh_delivered |   pv_self_consumption_pct |   viol_hours |   voltage_viol_steps |   branch_viol_steps |   transformer_viol_steps |   min_voltage_pu |   peak_net_kw |
|:--------|:---------------|-------:|--------------------:|----------------------------:|-------------------------:|--------------------------:|-------------:|---------------------:|--------------------:|-------------------------:|-----------------:|--------------:|
| caltech | admm_conformal |    365 |            100      |                    100      |                   0.0293 |                   56.8899 |         0.5  |                    0 |                   0 |                        2 |           0.9562 |       155.013 |
| caltech | edf            |    365 |            100      |                    100      |                   0.0342 |                   49.0406 |         0.75 |                    0 |                   0 |                        3 |           0.9586 |       152.129 |
| caltech | llf            |    365 |            100      |                    100      |                   0.0343 |                   48.9958 |         1.25 |                    0 |                   0 |                        5 |           0.9586 |       152.129 |
| caltech | mpc_conformal  |    365 |            100      |                    100      |                   0.0314 |                   54.304  |         2.75 |                    0 |                   0 |                       11 |           0.9542 |       162.567 |
| caltech | mpc_point      |    365 |            100      |                    100      |                   0.0278 |                   59.5891 |        11.5  |                    0 |                   3 |                       46 |           0.9539 |       203.59  |
| caltech | offline_opt    |    365 |            100      |                    100      |                   0.0255 |                   61.9528 |         0    |                    0 |                   0 |                        0 |           0.959  |       150     |
| caltech | uncontrolled   |    365 |            100      |                    100      |                   0.0343 |                   48.97   |        11.5  |                    0 |                   1 |                       46 |           0.9586 |       212.005 |
| jpl     | admm_conformal |    352 |            100      |                    100      |                   0.038  |                   57.3626 |         2    |                    0 |                   4 |                        8 |           0.9543 |       197.356 |
| jpl     | edf            |    352 |             99.9604 |                     99.8723 |                   0.0394 |                   53.8737 |        21.25 |                    0 |                   0 |                       85 |           0.9574 |       171.352 |
| jpl     | llf            |    352 |            100      |                    100      |                   0.0402 |                   52.9789 |        29.5  |                    0 |                   0 |                      118 |           0.9574 |       178.163 |
| jpl     | mpc_conformal  |    352 |            100      |                    100      |                   0.0402 |                   55.2943 |        37    |                    0 |                   0 |                      148 |           0.9545 |       177.33  |
| jpl     | mpc_point      |    352 |            100      |                    100      |                   0.0389 |                   57.4896 |       195    |                    0 |                   0 |                      780 |           0.9535 |       197.977 |
| jpl     | offline_opt    |    352 |            100      |                    100      |                   0.0359 |                   59.1216 |         0    |                    0 |                   0 |                        0 |           0.9574 |       150     |
| jpl     | uncontrolled   |    352 |            100      |                    100      |                   0.0405 |                   52.5972 |       366.5  |                    0 |                 660 |                     1466 |           0.9541 |       264.34  |

## E3 protocol
| site    | method         |   steps |   binding_share_pct |   ms_per_decision |   admm_iters_per_decision |
|:--------|:---------------|--------:|--------------------:|------------------:|--------------------------:|
| caltech | uncontrolled   |   26922 |               0     |             0.314 |                     0     |
| caltech | edf            |   26923 |               0.643 |             0.275 |                     0     |
| caltech | llf            |   26922 |               0.743 |             0.289 |                     0     |
| caltech | mpc_point      |   36249 |               0.411 |            13.791 |                     0     |
| caltech | mpc_conformal  |   36571 |               1.105 |            13.909 |                     0     |
| caltech | admm_conformal |   39370 |               0.061 |            59.201 |                    23.3   |
| caltech | offline_opt    |       0 |               0     |         13413.8   |                     0     |
| jpl     | uncontrolled   |   20033 |               0     |             0.517 |                     0     |
| jpl     | edf            |   20033 |              10.313 |             0.689 |                     0     |
| jpl     | llf            |   20033 |              13.273 |             0.668 |                     0     |
| jpl     | mpc_point      |   22503 |               9.185 |            19.303 |                     0     |
| jpl     | mpc_conformal  |   22902 |              12.925 |            18.378 |                     0     |
| jpl     | admm_conformal |   25525 |               0.133 |            71.784 |                    23.211 |
| jpl     | offline_opt    |       0 |               0     |         17336.6   |                     0     |

## E5 closed-loop ablation
| site    | mode      |   energy_served_pct |   cost_per_kwh_delivered |   viol_hours |   min_voltage_pu |
|:--------|:----------|--------------------:|-------------------------:|-------------:|-----------------:|
| caltech | aci       |             99.9999 |                   0.0297 |         0.5  |           0.9562 |
| caltech | expanding |            100      |                   0.0294 |         0.75 |           0.9571 |
| caltech | point     |            100      |                   0.0274 |         0.25 |           0.9559 |
| caltech | quantile  |            100      |                   0.0285 |         1.5  |           0.9562 |
| caltech | rolling   |            100      |                   0.0293 |         0.5  |           0.9562 |
| caltech | static    |            100      |                   0.0295 |         0.75 |           0.9572 |
| jpl     | aci       |             99.9999 |                   0.0381 |         2    |           0.955  |
| jpl     | expanding |             99.9999 |                   0.0379 |         1.75 |           0.9549 |
| jpl     | point     |            100      |                   0.038  |         2.5  |           0.9537 |
| jpl     | quantile  |            100      |                   0.0381 |         2    |           0.9543 |
| jpl     | rolling   |            100      |                   0.038  |         2    |           0.9543 |
| jpl     | static    |            100      |                   0.0379 |         1.75 |           0.955  |

## E2 stress tests
| site    | method         |   v_base_target |   transformer_kw |   penetration |   energy_served_pct |   cost_per_kwh_delivered |   viol_hours |   binding_share_pct |
|:--------|:---------------|----------------:|-----------------:|--------------:|--------------------:|-------------------------:|-------------:|--------------------:|
| caltech | edf            |           0.97  |              100 |           1   |              99.95  |                    0.036 |         3.5  |               7.257 |
| caltech | mpc_point      |           0.97  |              100 |           1   |             100     |                    0.03  |         6.25 |               2.608 |
| caltech | mpc_conformal  |           0.97  |              100 |           1   |             100     |                    0.034 |         3.25 |               6.684 |
| caltech | admm_conformal |           0.97  |              100 |           1   |             100     |                    0.033 |         0.25 |               0.08  |
| caltech | offline_opt    |           0.97  |              100 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.97  |              100 |           1.5 |              92.159 |                    0.04  |         8    |              13.618 |
| caltech | mpc_point      |           0.97  |              100 |           1.5 |              93.011 |                    0.039 |        19.75 |               6.982 |
| caltech | mpc_conformal  |           0.97  |              100 |           1.5 |              92.596 |                    0.04  |        12.25 |              13.927 |
| caltech | admm_conformal |           0.97  |              100 |           1.5 |              92.254 |                    0.04  |         2.5  |               1.128 |
| caltech | offline_opt    |           0.97  |              100 |           1.5 |              93.12  |                    0.037 |         0    |               0     |
| caltech | edf            |           0.97  |              100 |           2   |              83.631 |                    0.045 |        13.25 |              18.97  |
| caltech | mpc_point      |           0.97  |              100 |           2   |              85.337 |                    0.044 |        38.25 |              12.968 |
| caltech | mpc_conformal  |           0.97  |              100 |           2   |              84.603 |                    0.045 |        18    |              20.406 |
| caltech | admm_conformal |           0.97  |              100 |           2   |              83.673 |                    0.044 |         6.5  |               4.115 |
| caltech | offline_opt    |           0.97  |              100 |           2   |              85.909 |                    0.043 |         0    |               0     |
| caltech | edf            |           0.97  |              150 |           1   |             100     |                    0.037 |         0    |               1.108 |
| caltech | mpc_point      |           0.97  |              150 |           1   |             100     |                    0.03  |         1.25 |               0.585 |
| caltech | mpc_conformal  |           0.97  |              150 |           1   |             100     |                    0.035 |         0.25 |               1.417 |
| caltech | admm_conformal |           0.97  |              150 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.97  |              150 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.97  |              150 |           1.5 |              92.942 |                    0.041 |         0.25 |               3.941 |
| caltech | mpc_point      |           0.97  |              150 |           1.5 |              93.12  |                    0.039 |         6.25 |               1.873 |
| caltech | mpc_conformal  |           0.97  |              150 |           1.5 |              93.12  |                    0.041 |         2.75 |               4.514 |
| caltech | admm_conformal |           0.97  |              150 |           1.5 |              93.12  |                    0.04  |         1.25 |               0.117 |
| caltech | offline_opt    |           0.97  |              150 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.97  |              150 |           2   |              85.813 |                    0.045 |         1.5  |               5.749 |
| caltech | mpc_point      |           0.97  |              150 |           2   |              86.302 |                    0.043 |        14.5  |               3.623 |
| caltech | mpc_conformal  |           0.97  |              150 |           2   |              86.302 |                    0.044 |         4.75 |               7.492 |
| caltech | admm_conformal |           0.97  |              150 |           2   |              86.042 |                    0.044 |         2.5  |               0.692 |
| caltech | offline_opt    |           0.97  |              150 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.97  |              200 |           1   |             100     |                    0.037 |         0    |               0.062 |
| caltech | mpc_point      |           0.97  |              200 |           1   |             100     |                    0.03  |         0    |               0     |
| caltech | mpc_conformal  |           0.97  |              200 |           1   |             100     |                    0.035 |         0    |               0.133 |
| caltech | admm_conformal |           0.97  |              200 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.97  |              200 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.97  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.62  |
| caltech | mpc_point      |           0.97  |              200 |           1.5 |              93.12  |                    0.039 |         1    |               0.085 |
| caltech | mpc_conformal  |           0.97  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.681 |
| caltech | admm_conformal |           0.97  |              200 |           1.5 |              93.12  |                    0.04  |         0    |               0.078 |
| caltech | offline_opt    |           0.97  |              200 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.97  |              200 |           2   |              86.241 |                    0.045 |         0    |               1.372 |
| caltech | mpc_point      |           0.97  |              200 |           2   |              86.302 |                    0.043 |         1    |               0.535 |
| caltech | mpc_conformal  |           0.97  |              200 |           2   |              86.302 |                    0.044 |         0    |               1.325 |
| caltech | admm_conformal |           0.97  |              200 |           2   |              86.302 |                    0.044 |         0    |               0.115 |
| caltech | offline_opt    |           0.97  |              200 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.96  |              100 |           1   |              99.95  |                    0.036 |         3.5  |               7.257 |
| caltech | mpc_point      |           0.96  |              100 |           1   |             100     |                    0.03  |         6.25 |               2.608 |
| caltech | mpc_conformal  |           0.96  |              100 |           1   |             100     |                    0.034 |         3.25 |               6.684 |
| caltech | admm_conformal |           0.96  |              100 |           1   |             100     |                    0.033 |         0.25 |               0.08  |
| caltech | offline_opt    |           0.96  |              100 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.96  |              100 |           1.5 |              92.159 |                    0.04  |         8    |              13.618 |
| caltech | mpc_point      |           0.96  |              100 |           1.5 |              93.011 |                    0.039 |        19.75 |               6.982 |
| caltech | mpc_conformal  |           0.96  |              100 |           1.5 |              92.596 |                    0.04  |        12.25 |              13.927 |
| caltech | admm_conformal |           0.96  |              100 |           1.5 |              92.254 |                    0.04  |         2.5  |               1.128 |
| caltech | offline_opt    |           0.96  |              100 |           1.5 |              93.12  |                    0.037 |         0    |               0     |
| caltech | edf            |           0.96  |              100 |           2   |              83.631 |                    0.045 |        13.25 |              18.97  |
| caltech | mpc_point      |           0.96  |              100 |           2   |              85.337 |                    0.044 |        38.25 |              12.968 |
| caltech | mpc_conformal  |           0.96  |              100 |           2   |              84.603 |                    0.045 |        18    |              20.406 |
| caltech | admm_conformal |           0.96  |              100 |           2   |              83.673 |                    0.044 |         6.5  |               4.115 |
| caltech | offline_opt    |           0.96  |              100 |           2   |              85.909 |                    0.043 |         0    |               0     |
| caltech | edf            |           0.96  |              150 |           1   |             100     |                    0.037 |         0    |               1.108 |
| caltech | mpc_point      |           0.96  |              150 |           1   |             100     |                    0.03  |         1.25 |               0.585 |
| caltech | mpc_conformal  |           0.96  |              150 |           1   |             100     |                    0.035 |         0.25 |               1.417 |
| caltech | admm_conformal |           0.96  |              150 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.96  |              150 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.96  |              150 |           1.5 |              92.942 |                    0.041 |         0.25 |               3.941 |
| caltech | mpc_point      |           0.96  |              150 |           1.5 |              93.12  |                    0.039 |         6.25 |               1.873 |
| caltech | mpc_conformal  |           0.96  |              150 |           1.5 |              93.12  |                    0.041 |         2.75 |               4.514 |
| caltech | admm_conformal |           0.96  |              150 |           1.5 |              93.12  |                    0.04  |         1.25 |               0.117 |
| caltech | offline_opt    |           0.96  |              150 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.96  |              150 |           2   |              85.813 |                    0.045 |         1.5  |               5.749 |
| caltech | mpc_point      |           0.96  |              150 |           2   |              86.302 |                    0.043 |        14.5  |               3.623 |
| caltech | mpc_conformal  |           0.96  |              150 |           2   |              86.302 |                    0.044 |         4.75 |               7.492 |
| caltech | admm_conformal |           0.96  |              150 |           2   |              86.042 |                    0.044 |         2.5  |               0.692 |
| caltech | offline_opt    |           0.96  |              150 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.96  |              200 |           1   |             100     |                    0.037 |         0    |               0.062 |
| caltech | mpc_point      |           0.96  |              200 |           1   |             100     |                    0.03  |         0    |               0     |
| caltech | mpc_conformal  |           0.96  |              200 |           1   |             100     |                    0.035 |         0    |               0.133 |
| caltech | admm_conformal |           0.96  |              200 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.96  |              200 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.96  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.62  |
| caltech | mpc_point      |           0.96  |              200 |           1.5 |              93.12  |                    0.039 |         1    |               0.085 |
| caltech | mpc_conformal  |           0.96  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.681 |
| caltech | admm_conformal |           0.96  |              200 |           1.5 |              93.12  |                    0.04  |         0    |               0.078 |
| caltech | offline_opt    |           0.96  |              200 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.96  |              200 |           2   |              86.241 |                    0.045 |         0    |               1.372 |
| caltech | mpc_point      |           0.96  |              200 |           2   |              86.302 |                    0.043 |         1    |               0.535 |
| caltech | mpc_conformal  |           0.96  |              200 |           2   |              86.302 |                    0.044 |         0    |               1.325 |
| caltech | admm_conformal |           0.96  |              200 |           2   |              86.302 |                    0.044 |         0    |               0.115 |
| caltech | offline_opt    |           0.96  |              200 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.955 |              100 |           1   |              99.95  |                    0.036 |         3.5  |               7.257 |
| caltech | mpc_point      |           0.955 |              100 |           1   |             100     |                    0.03  |         6.25 |               2.608 |
| caltech | mpc_conformal  |           0.955 |              100 |           1   |             100     |                    0.034 |         3.25 |               6.684 |
| caltech | admm_conformal |           0.955 |              100 |           1   |             100     |                    0.033 |         0.25 |               0.08  |
| caltech | offline_opt    |           0.955 |              100 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.955 |              100 |           1.5 |              92.159 |                    0.04  |         8    |              13.618 |
| caltech | mpc_point      |           0.955 |              100 |           1.5 |              93.011 |                    0.039 |        19.75 |               6.982 |
| caltech | mpc_conformal  |           0.955 |              100 |           1.5 |              92.596 |                    0.04  |        12.25 |              13.927 |
| caltech | admm_conformal |           0.955 |              100 |           1.5 |              92.254 |                    0.04  |         2.5  |               1.128 |
| caltech | offline_opt    |           0.955 |              100 |           1.5 |              93.12  |                    0.037 |         0    |               0     |
| caltech | edf            |           0.955 |              100 |           2   |              83.631 |                    0.045 |        13.25 |              18.97  |
| caltech | mpc_point      |           0.955 |              100 |           2   |              85.337 |                    0.044 |        38.25 |              12.968 |
| caltech | mpc_conformal  |           0.955 |              100 |           2   |              84.603 |                    0.045 |        18    |              20.406 |
| caltech | admm_conformal |           0.955 |              100 |           2   |              83.673 |                    0.044 |         6.5  |               4.115 |
| caltech | offline_opt    |           0.955 |              100 |           2   |              85.909 |                    0.043 |         0    |               0     |
| caltech | edf            |           0.955 |              150 |           1   |             100     |                    0.037 |         0    |               1.108 |
| caltech | mpc_point      |           0.955 |              150 |           1   |             100     |                    0.03  |         1.25 |               0.585 |
| caltech | mpc_conformal  |           0.955 |              150 |           1   |             100     |                    0.035 |         0.25 |               1.417 |
| caltech | admm_conformal |           0.955 |              150 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.955 |              150 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.955 |              150 |           1.5 |              92.942 |                    0.041 |         0.25 |               3.941 |
| caltech | mpc_point      |           0.955 |              150 |           1.5 |              93.12  |                    0.039 |         6.25 |               1.873 |
| caltech | mpc_conformal  |           0.955 |              150 |           1.5 |              93.12  |                    0.041 |         2.75 |               4.514 |
| caltech | admm_conformal |           0.955 |              150 |           1.5 |              93.12  |                    0.04  |         1.25 |               0.117 |
| caltech | offline_opt    |           0.955 |              150 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.955 |              150 |           2   |              85.813 |                    0.045 |         1.5  |               5.749 |
| caltech | mpc_point      |           0.955 |              150 |           2   |              86.302 |                    0.043 |        14.5  |               3.623 |
| caltech | mpc_conformal  |           0.955 |              150 |           2   |              86.302 |                    0.044 |         4.75 |               7.492 |
| caltech | admm_conformal |           0.955 |              150 |           2   |              86.042 |                    0.044 |         2.5  |               0.692 |
| caltech | offline_opt    |           0.955 |              150 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.955 |              200 |           1   |             100     |                    0.037 |         0    |               0.062 |
| caltech | mpc_point      |           0.955 |              200 |           1   |             100     |                    0.03  |         0    |               0     |
| caltech | mpc_conformal  |           0.955 |              200 |           1   |             100     |                    0.035 |         0    |               0.133 |
| caltech | admm_conformal |           0.955 |              200 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.955 |              200 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.955 |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.62  |
| caltech | mpc_point      |           0.955 |              200 |           1.5 |              93.12  |                    0.039 |         1    |               0.085 |
| caltech | mpc_conformal  |           0.955 |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.681 |
| caltech | admm_conformal |           0.955 |              200 |           1.5 |              93.12  |                    0.04  |         0    |               0.078 |
| caltech | offline_opt    |           0.955 |              200 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.955 |              200 |           2   |              86.241 |                    0.045 |         0    |               1.372 |
| caltech | mpc_point      |           0.955 |              200 |           2   |              86.302 |                    0.043 |         1    |               0.535 |
| caltech | mpc_conformal  |           0.955 |              200 |           2   |              86.302 |                    0.044 |         0    |               1.325 |
| caltech | admm_conformal |           0.955 |              200 |           2   |              86.302 |                    0.044 |         0    |               0.115 |
| caltech | offline_opt    |           0.955 |              200 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.95  |              100 |           1   |              99.95  |                    0.036 |         3.5  |               7.257 |
| caltech | mpc_point      |           0.95  |              100 |           1   |             100     |                    0.03  |         6.25 |               2.608 |
| caltech | mpc_conformal  |           0.95  |              100 |           1   |             100     |                    0.034 |         3.25 |               6.684 |
| caltech | admm_conformal |           0.95  |              100 |           1   |             100     |                    0.033 |         0.25 |               0.08  |
| caltech | offline_opt    |           0.95  |              100 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.95  |              100 |           1.5 |              92.159 |                    0.04  |         8    |              13.618 |
| caltech | mpc_point      |           0.95  |              100 |           1.5 |              93.011 |                    0.039 |        19.75 |               6.982 |
| caltech | mpc_conformal  |           0.95  |              100 |           1.5 |              92.596 |                    0.04  |        12.25 |              13.884 |
| caltech | admm_conformal |           0.95  |              100 |           1.5 |              92.254 |                    0.04  |         2.5  |               1.128 |
| caltech | offline_opt    |           0.95  |              100 |           1.5 |              93.12  |                    0.037 |         0    |               0     |
| caltech | edf            |           0.95  |              100 |           2   |              83.631 |                    0.045 |        13.25 |              18.97  |
| caltech | mpc_point      |           0.95  |              100 |           2   |              85.337 |                    0.044 |        38.25 |              12.968 |
| caltech | mpc_conformal  |           0.95  |              100 |           2   |              84.603 |                    0.045 |        18    |              20.406 |
| caltech | admm_conformal |           0.95  |              100 |           2   |              83.673 |                    0.044 |         6.5  |               4.115 |
| caltech | offline_opt    |           0.95  |              100 |           2   |              85.909 |                    0.043 |         0    |               0     |
| caltech | edf            |           0.95  |              150 |           1   |             100     |                    0.037 |         0    |               1.108 |
| caltech | mpc_point      |           0.95  |              150 |           1   |             100     |                    0.03  |         1.25 |               0.585 |
| caltech | mpc_conformal  |           0.95  |              150 |           1   |             100     |                    0.035 |         0.25 |               1.417 |
| caltech | admm_conformal |           0.95  |              150 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.95  |              150 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.95  |              150 |           1.5 |              92.942 |                    0.041 |         0.25 |               3.941 |
| caltech | mpc_point      |           0.95  |              150 |           1.5 |              93.12  |                    0.039 |         6.25 |               1.873 |
| caltech | mpc_conformal  |           0.95  |              150 |           1.5 |              93.12  |                    0.041 |         2.75 |               4.514 |
| caltech | admm_conformal |           0.95  |              150 |           1.5 |              93.12  |                    0.04  |         1.25 |               0.117 |
| caltech | offline_opt    |           0.95  |              150 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.95  |              150 |           2   |              85.813 |                    0.045 |         1.5  |               5.749 |
| caltech | mpc_point      |           0.95  |              150 |           2   |              86.302 |                    0.043 |        14.5  |               3.623 |
| caltech | mpc_conformal  |           0.95  |              150 |           2   |              86.302 |                    0.044 |         4.75 |               7.492 |
| caltech | admm_conformal |           0.95  |              150 |           2   |              86.042 |                    0.044 |         2.5  |               0.692 |
| caltech | offline_opt    |           0.95  |              150 |           2   |              86.302 |                    0.042 |         0    |               0     |
| caltech | edf            |           0.95  |              200 |           1   |             100     |                    0.037 |         0    |               0.062 |
| caltech | mpc_point      |           0.95  |              200 |           1   |             100     |                    0.03  |         0    |               0     |
| caltech | mpc_conformal  |           0.95  |              200 |           1   |             100     |                    0.035 |         0    |               0.133 |
| caltech | admm_conformal |           0.95  |              200 |           1   |             100     |                    0.033 |         0    |               0     |
| caltech | offline_opt    |           0.95  |              200 |           1   |             100     |                    0.027 |         0    |               0     |
| caltech | edf            |           0.95  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.62  |
| caltech | mpc_point      |           0.95  |              200 |           1.5 |              93.12  |                    0.039 |         1    |               0.085 |
| caltech | mpc_conformal  |           0.95  |              200 |           1.5 |              93.12  |                    0.041 |         0    |               0.681 |
| caltech | admm_conformal |           0.95  |              200 |           1.5 |              93.12  |                    0.04  |         0    |               0.078 |
| caltech | offline_opt    |           0.95  |              200 |           1.5 |              93.12  |                    0.036 |         0    |               0     |
| caltech | edf            |           0.95  |              200 |           2   |              86.241 |                    0.045 |         0    |               1.372 |
| caltech | mpc_point      |           0.95  |              200 |           2   |              86.302 |                    0.043 |         1    |               0.535 |
| caltech | mpc_conformal  |           0.95  |              200 |           2   |              86.302 |                    0.044 |         0    |               1.325 |
| caltech | admm_conformal |           0.95  |              200 |           2   |              86.302 |                    0.044 |         0    |               0.115 |
| caltech | offline_opt    |           0.95  |              200 |           2   |              86.302 |                    0.042 |         0    |               0     |
| jpl     | edf            |           0.97  |              100 |           1   |              99.218 |                    0.038 |        12.25 |              24.939 |
| jpl     | mpc_point      |           0.97  |              100 |           1   |             100     |                    0.039 |        40.75 |              18.544 |
| jpl     | mpc_conformal  |           0.97  |              100 |           1   |              99.951 |                    0.039 |        15    |              27.305 |
| jpl     | admm_conformal |           0.97  |              100 |           1   |              99.473 |                    0.038 |         1.25 |               3.313 |
| jpl     | offline_opt    |           0.97  |              100 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.97  |              100 |           1.5 |              84.286 |                    0.045 |        17.75 |              34.835 |
| jpl     | mpc_point      |           0.97  |              100 |           1.5 |              91.993 |                    0.047 |        77.5  |              35.042 |
| jpl     | mpc_conformal  |           0.97  |              100 |           1.5 |              86.171 |                    0.046 |        22.25 |              39.441 |
| jpl     | admm_conformal |           0.97  |              100 |           1.5 |              84.183 |                    0.045 |        17    |              17.801 |
| jpl     | offline_opt    |           0.97  |              100 |           1.5 |              90.948 |                    0.046 |         0    |               0     |
| jpl     | edf            |           0.97  |              100 |           2   |              67.565 |                    0.047 |        22    |              40.804 |
| jpl     | mpc_point      |           0.97  |              100 |           2   |              75.717 |                    0.049 |        88.25 |              39.026 |
| jpl     | mpc_conformal  |           0.97  |              100 |           2   |              67.922 |                    0.047 |        22.75 |              40.182 |
| jpl     | admm_conformal |           0.97  |              100 |           2   |              66.502 |                    0.047 |        21.25 |              31.232 |
| jpl     | offline_opt    |           0.97  |              100 |           2   |              75.685 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.97  |              150 |           1   |              99.972 |                    0.04  |         5.5  |              11.779 |
| jpl     | mpc_point      |           0.97  |              150 |           1   |             100     |                    0.039 |        17.5  |               9.606 |
| jpl     | mpc_conformal  |           0.97  |              150 |           1   |             100     |                    0.04  |         6.25 |              14.271 |
| jpl     | admm_conformal |           0.97  |              150 |           1   |             100     |                    0.038 |         0.25 |               0.24  |
| jpl     | offline_opt    |           0.97  |              150 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.97  |              150 |           1.5 |              91.813 |                    0.045 |         9    |              16.951 |
| jpl     | mpc_point      |           0.97  |              150 |           1.5 |              93.299 |                    0.046 |        45.5  |              18.318 |
| jpl     | mpc_conformal  |           0.97  |              150 |           1.5 |              93.293 |                    0.046 |        15.75 |              24.351 |
| jpl     | admm_conformal |           0.97  |              150 |           1.5 |              93.054 |                    0.046 |         4.25 |               2.285 |
| jpl     | offline_opt    |           0.97  |              150 |           1.5 |              93.299 |                    0.045 |         0    |               0     |
| jpl     | edf            |           0.97  |              150 |           2   |              79.334 |                    0.049 |        13.75 |              22.798 |
| jpl     | mpc_point      |           0.97  |              150 |           2   |              83.76  |                    0.05  |        65.25 |              25.531 |
| jpl     | mpc_conformal  |           0.97  |              150 |           2   |              82.13  |                    0.05  |        19.25 |              31.337 |
| jpl     | admm_conformal |           0.97  |              150 |           2   |              81.341 |                    0.05  |        12.25 |              12.464 |
| jpl     | offline_opt    |           0.97  |              150 |           2   |              83.627 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.97  |              200 |           1   |             100     |                    0.041 |         2.25 |               5.647 |
| jpl     | mpc_point      |           0.97  |              200 |           1   |             100     |                    0.039 |         9.5  |               5.663 |
| jpl     | mpc_conformal  |           0.97  |              200 |           1   |             100     |                    0.041 |         3.5  |               7.85  |
| jpl     | admm_conformal |           0.97  |              200 |           1   |             100     |                    0.038 |         0    |               0     |
| jpl     | offline_opt    |           0.97  |              200 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.97  |              200 |           1.5 |              92.98  |                    0.045 |         5.25 |               9.171 |
| jpl     | mpc_point      |           0.97  |              200 |           1.5 |              93.299 |                    0.046 |        22    |              10.304 |
| jpl     | mpc_conformal  |           0.97  |              200 |           1.5 |              93.299 |                    0.046 |         7.25 |              13.278 |
| jpl     | admm_conformal |           0.97  |              200 |           1.5 |              93.299 |                    0.046 |         1    |               0.143 |
| jpl     | offline_opt    |           0.97  |              200 |           1.5 |              93.299 |                    0.044 |         0    |               0     |
| jpl     | edf            |           0.97  |              200 |           2   |              82.758 |                    0.049 |         7.25 |              11.969 |
| jpl     | mpc_point      |           0.97  |              200 |           2   |              83.76  |                    0.049 |        31.75 |              12.983 |
| jpl     | mpc_conformal  |           0.97  |              200 |           2   |              83.76  |                    0.049 |        10.5  |              17.681 |
| jpl     | admm_conformal |           0.97  |              200 |           2   |              83.758 |                    0.049 |         5    |               2.322 |
| jpl     | offline_opt    |           0.97  |              200 |           2   |              83.76  |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.96  |              100 |           1   |              99.218 |                    0.038 |        12.25 |              24.939 |
| jpl     | mpc_point      |           0.96  |              100 |           1   |             100     |                    0.039 |        40.75 |              18.544 |
| jpl     | mpc_conformal  |           0.96  |              100 |           1   |              99.951 |                    0.039 |        15    |              27.305 |
| jpl     | admm_conformal |           0.96  |              100 |           1   |              99.473 |                    0.038 |         1.25 |               3.313 |
| jpl     | offline_opt    |           0.96  |              100 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.96  |              100 |           1.5 |              84.286 |                    0.045 |        17.75 |              34.835 |
| jpl     | mpc_point      |           0.96  |              100 |           1.5 |              91.993 |                    0.047 |        77.5  |              35.042 |
| jpl     | mpc_conformal  |           0.96  |              100 |           1.5 |              86.171 |                    0.046 |        22.25 |              39.441 |
| jpl     | admm_conformal |           0.96  |              100 |           1.5 |              84.183 |                    0.045 |        17    |              17.801 |
| jpl     | offline_opt    |           0.96  |              100 |           1.5 |              90.948 |                    0.046 |         0    |               0     |
| jpl     | edf            |           0.96  |              100 |           2   |              67.565 |                    0.047 |        22    |              40.804 |
| jpl     | mpc_point      |           0.96  |              100 |           2   |              75.717 |                    0.049 |        88.25 |              39.026 |
| jpl     | mpc_conformal  |           0.96  |              100 |           2   |              67.922 |                    0.047 |        22.75 |              40.182 |
| jpl     | admm_conformal |           0.96  |              100 |           2   |              66.502 |                    0.047 |        21.25 |              31.232 |
| jpl     | offline_opt    |           0.96  |              100 |           2   |              75.685 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.96  |              150 |           1   |              99.972 |                    0.04  |         5.5  |              11.779 |
| jpl     | mpc_point      |           0.96  |              150 |           1   |             100     |                    0.039 |        17.5  |               9.606 |
| jpl     | mpc_conformal  |           0.96  |              150 |           1   |             100     |                    0.04  |         6.25 |              14.271 |
| jpl     | admm_conformal |           0.96  |              150 |           1   |             100     |                    0.038 |         0.25 |               0.24  |
| jpl     | offline_opt    |           0.96  |              150 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.96  |              150 |           1.5 |              91.813 |                    0.045 |         9    |              16.951 |
| jpl     | mpc_point      |           0.96  |              150 |           1.5 |              93.299 |                    0.046 |        45.5  |              18.318 |
| jpl     | mpc_conformal  |           0.96  |              150 |           1.5 |              93.293 |                    0.046 |        15.75 |              24.351 |
| jpl     | admm_conformal |           0.96  |              150 |           1.5 |              93.054 |                    0.046 |         4.25 |               2.285 |
| jpl     | offline_opt    |           0.96  |              150 |           1.5 |              93.299 |                    0.045 |         0    |               0     |
| jpl     | edf            |           0.96  |              150 |           2   |              79.334 |                    0.049 |        13.75 |              22.798 |
| jpl     | mpc_point      |           0.96  |              150 |           2   |              83.76  |                    0.05  |        65.25 |              25.531 |
| jpl     | mpc_conformal  |           0.96  |              150 |           2   |              82.13  |                    0.05  |        19.25 |              31.337 |
| jpl     | admm_conformal |           0.96  |              150 |           2   |              81.341 |                    0.05  |        12.25 |              12.464 |
| jpl     | offline_opt    |           0.96  |              150 |           2   |              83.627 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.96  |              200 |           1   |             100     |                    0.041 |         2.25 |               5.647 |
| jpl     | mpc_point      |           0.96  |              200 |           1   |             100     |                    0.039 |         9.5  |               5.663 |
| jpl     | mpc_conformal  |           0.96  |              200 |           1   |             100     |                    0.041 |         3.5  |               7.85  |
| jpl     | admm_conformal |           0.96  |              200 |           1   |             100     |                    0.038 |         0    |               0     |
| jpl     | offline_opt    |           0.96  |              200 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.96  |              200 |           1.5 |              92.98  |                    0.045 |         5.25 |               9.171 |
| jpl     | mpc_point      |           0.96  |              200 |           1.5 |              93.299 |                    0.046 |        22    |              10.304 |
| jpl     | mpc_conformal  |           0.96  |              200 |           1.5 |              93.299 |                    0.046 |         7.25 |              13.278 |
| jpl     | admm_conformal |           0.96  |              200 |           1.5 |              93.299 |                    0.046 |         1    |               0.143 |
| jpl     | offline_opt    |           0.96  |              200 |           1.5 |              93.299 |                    0.044 |         0    |               0     |
| jpl     | edf            |           0.96  |              200 |           2   |              82.758 |                    0.049 |         7.25 |              11.969 |
| jpl     | mpc_point      |           0.96  |              200 |           2   |              83.76  |                    0.049 |        31.75 |              12.983 |
| jpl     | mpc_conformal  |           0.96  |              200 |           2   |              83.76  |                    0.049 |        10.5  |              17.681 |
| jpl     | admm_conformal |           0.96  |              200 |           2   |              83.758 |                    0.049 |         5    |               2.322 |
| jpl     | offline_opt    |           0.96  |              200 |           2   |              83.76  |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.955 |              100 |           1   |              99.218 |                    0.038 |        12.25 |              24.939 |
| jpl     | mpc_point      |           0.955 |              100 |           1   |             100     |                    0.039 |        40.75 |              18.544 |
| jpl     | mpc_conformal  |           0.955 |              100 |           1   |              99.951 |                    0.039 |        15    |              27.305 |
| jpl     | admm_conformal |           0.955 |              100 |           1   |              99.473 |                    0.038 |         1.25 |               3.313 |
| jpl     | offline_opt    |           0.955 |              100 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.955 |              100 |           1.5 |              84.286 |                    0.045 |        17.75 |              34.835 |
| jpl     | mpc_point      |           0.955 |              100 |           1.5 |              91.993 |                    0.047 |        77.5  |              35.042 |
| jpl     | mpc_conformal  |           0.955 |              100 |           1.5 |              86.171 |                    0.046 |        22.25 |              39.441 |
| jpl     | admm_conformal |           0.955 |              100 |           1.5 |              84.183 |                    0.045 |        17    |              17.801 |
| jpl     | offline_opt    |           0.955 |              100 |           1.5 |              90.948 |                    0.046 |         0    |               0     |
| jpl     | edf            |           0.955 |              100 |           2   |              67.565 |                    0.047 |        22    |              40.804 |
| jpl     | mpc_point      |           0.955 |              100 |           2   |              75.717 |                    0.049 |        88.25 |              39.026 |
| jpl     | mpc_conformal  |           0.955 |              100 |           2   |              67.922 |                    0.047 |        22.75 |              40.182 |
| jpl     | admm_conformal |           0.955 |              100 |           2   |              66.502 |                    0.047 |        21.25 |              31.232 |
| jpl     | offline_opt    |           0.955 |              100 |           2   |              75.685 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.955 |              150 |           1   |              99.972 |                    0.04  |         5.5  |              11.779 |
| jpl     | mpc_point      |           0.955 |              150 |           1   |             100     |                    0.039 |        17.5  |               9.606 |
| jpl     | mpc_conformal  |           0.955 |              150 |           1   |             100     |                    0.04  |         6.25 |              14.271 |
| jpl     | admm_conformal |           0.955 |              150 |           1   |             100     |                    0.038 |         0.25 |               0.24  |
| jpl     | offline_opt    |           0.955 |              150 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.955 |              150 |           1.5 |              91.813 |                    0.045 |         9    |              16.951 |
| jpl     | mpc_point      |           0.955 |              150 |           1.5 |              93.299 |                    0.046 |        45.5  |              18.318 |
| jpl     | mpc_conformal  |           0.955 |              150 |           1.5 |              93.293 |                    0.046 |        15.75 |              24.351 |
| jpl     | admm_conformal |           0.955 |              150 |           1.5 |              93.054 |                    0.046 |         4.25 |               2.285 |
| jpl     | offline_opt    |           0.955 |              150 |           1.5 |              93.299 |                    0.045 |         0    |               0     |
| jpl     | edf            |           0.955 |              150 |           2   |              79.334 |                    0.049 |        13.75 |              22.798 |
| jpl     | mpc_point      |           0.955 |              150 |           2   |              83.76  |                    0.05  |        65.25 |              25.531 |
| jpl     | mpc_conformal  |           0.955 |              150 |           2   |              82.13  |                    0.05  |        19.25 |              31.337 |
| jpl     | admm_conformal |           0.955 |              150 |           2   |              81.341 |                    0.05  |        12.25 |              12.464 |
| jpl     | offline_opt    |           0.955 |              150 |           2   |              83.627 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.955 |              200 |           1   |             100     |                    0.041 |         2.25 |               5.647 |
| jpl     | mpc_point      |           0.955 |              200 |           1   |             100     |                    0.039 |         9.5  |               5.663 |
| jpl     | mpc_conformal  |           0.955 |              200 |           1   |             100     |                    0.041 |         3.5  |               7.85  |
| jpl     | admm_conformal |           0.955 |              200 |           1   |             100     |                    0.038 |         0    |               0     |
| jpl     | offline_opt    |           0.955 |              200 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.955 |              200 |           1.5 |              92.98  |                    0.045 |         5.25 |               9.171 |
| jpl     | mpc_point      |           0.955 |              200 |           1.5 |              93.299 |                    0.046 |        22    |              10.304 |
| jpl     | mpc_conformal  |           0.955 |              200 |           1.5 |              93.299 |                    0.046 |         7.25 |              13.278 |
| jpl     | admm_conformal |           0.955 |              200 |           1.5 |              93.299 |                    0.046 |         1    |               0.143 |
| jpl     | offline_opt    |           0.955 |              200 |           1.5 |              93.299 |                    0.044 |         0    |               0     |
| jpl     | edf            |           0.955 |              200 |           2   |              82.758 |                    0.049 |         7.25 |              11.969 |
| jpl     | mpc_point      |           0.955 |              200 |           2   |              83.76  |                    0.049 |        31.75 |              12.983 |
| jpl     | mpc_conformal  |           0.955 |              200 |           2   |              83.76  |                    0.049 |        10.5  |              17.681 |
| jpl     | admm_conformal |           0.955 |              200 |           2   |              83.758 |                    0.049 |         5    |               2.322 |
| jpl     | offline_opt    |           0.955 |              200 |           2   |              83.76  |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.95  |              100 |           1   |              99.218 |                    0.038 |        12.25 |              24.939 |
| jpl     | mpc_point      |           0.95  |              100 |           1   |             100     |                    0.039 |        40.75 |              18.596 |
| jpl     | mpc_conformal  |           0.95  |              100 |           1   |              99.951 |                    0.039 |        15    |              27.305 |
| jpl     | admm_conformal |           0.95  |              100 |           1   |              99.473 |                    0.038 |         1.25 |               3.313 |
| jpl     | offline_opt    |           0.95  |              100 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.95  |              100 |           1.5 |              84.286 |                    0.045 |        17.75 |              34.835 |
| jpl     | mpc_point      |           0.95  |              100 |           1.5 |              91.993 |                    0.047 |        77.5  |              35.092 |
| jpl     | mpc_conformal  |           0.95  |              100 |           1.5 |              86.171 |                    0.046 |        22    |              39.637 |
| jpl     | admm_conformal |           0.95  |              100 |           1.5 |              84.086 |                    0.045 |        17    |              17.944 |
| jpl     | offline_opt    |           0.95  |              100 |           1.5 |              90.948 |                    0.046 |         0    |               0     |
| jpl     | edf            |           0.95  |              100 |           2   |              67.52  |                    0.047 |        22    |              41.11  |
| jpl     | mpc_point      |           0.95  |              100 |           2   |              75.693 |                    0.049 |        88.25 |              39.026 |
| jpl     | mpc_conformal  |           0.95  |              100 |           2   |              67.792 |                    0.047 |        22.5  |              40.182 |
| jpl     | admm_conformal |           0.95  |              100 |           2   |              66.35  |                    0.046 |        21    |              31.564 |
| jpl     | offline_opt    |           0.95  |              100 |           2   |              75.685 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.95  |              150 |           1   |              99.972 |                    0.04  |         5.5  |              11.779 |
| jpl     | mpc_point      |           0.95  |              150 |           1   |             100     |                    0.039 |        17.5  |               9.606 |
| jpl     | mpc_conformal  |           0.95  |              150 |           1   |             100     |                    0.04  |         6.25 |              14.374 |
| jpl     | admm_conformal |           0.95  |              150 |           1   |             100     |                    0.038 |         0.25 |               0.24  |
| jpl     | offline_opt    |           0.95  |              150 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.95  |              150 |           1.5 |              91.813 |                    0.045 |         9    |              16.951 |
| jpl     | mpc_point      |           0.95  |              150 |           1.5 |              93.299 |                    0.046 |        45.5  |              18.318 |
| jpl     | mpc_conformal  |           0.95  |              150 |           1.5 |              93.293 |                    0.046 |        15.75 |              24.253 |
| jpl     | admm_conformal |           0.95  |              150 |           1.5 |              93.054 |                    0.046 |         4.25 |               2.285 |
| jpl     | offline_opt    |           0.95  |              150 |           1.5 |              93.299 |                    0.045 |         0    |               0     |
| jpl     | edf            |           0.95  |              150 |           2   |              79.33  |                    0.049 |        13.75 |              22.953 |
| jpl     | mpc_point      |           0.95  |              150 |           2   |              83.76  |                    0.05  |        65.25 |              25.579 |
| jpl     | mpc_conformal  |           0.95  |              150 |           2   |              82.13  |                    0.05  |        18.75 |              31.72  |
| jpl     | admm_conformal |           0.95  |              150 |           2   |              81.252 |                    0.05  |        12.75 |              13.033 |
| jpl     | offline_opt    |           0.95  |              150 |           2   |              83.627 |                    0.049 |         0    |               0     |
| jpl     | edf            |           0.95  |              200 |           1   |             100     |                    0.041 |         2.25 |               5.647 |
| jpl     | mpc_point      |           0.95  |              200 |           1   |             100     |                    0.039 |         9.5  |               5.768 |
| jpl     | mpc_conformal  |           0.95  |              200 |           1   |             100     |                    0.041 |         3.5  |               8.158 |
| jpl     | admm_conformal |           0.95  |              200 |           1   |             100     |                    0.038 |         0    |               0.096 |
| jpl     | offline_opt    |           0.95  |              200 |           1   |             100     |                    0.036 |         0    |               0     |
| jpl     | edf            |           0.95  |              200 |           1.5 |              92.98  |                    0.045 |         5.25 |               9.171 |
| jpl     | mpc_point      |           0.95  |              200 |           1.5 |              93.299 |                    0.046 |        22    |              10.304 |
| jpl     | mpc_conformal  |           0.95  |              200 |           1.5 |              93.299 |                    0.046 |         7.25 |              13.278 |
| jpl     | admm_conformal |           0.95  |              200 |           1.5 |              93.299 |                    0.046 |         1    |               0.143 |
| jpl     | offline_opt    |           0.95  |              200 |           1.5 |              93.299 |                    0.044 |         0    |               0     |
| jpl     | edf            |           0.95  |              200 |           2   |              82.758 |                    0.049 |         7.25 |              11.969 |
| jpl     | mpc_point      |           0.95  |              200 |           2   |              83.76  |                    0.049 |        31.75 |              12.983 |
| jpl     | mpc_conformal  |           0.95  |              200 |           2   |              83.76  |                    0.049 |        10.5  |              17.777 |
| jpl     | admm_conformal |           0.95  |              200 |           2   |              83.742 |                    0.049 |         5    |               2.701 |
| jpl     | offline_opt    |           0.95  |              200 |           2   |              83.76  |                    0.049 |         0    |               0     |
## Additional evidence (fairness check, large hub, corrected statistics)

### Fairness: tight-tolerance ADMM vs centralized MPC (same bounds)
| site    | method                      |   cost_per_kwh_delivered |   energy_served_pct |   viol_hours |   pv_self_consumption_pct |   saturation_share_pct |   transformer_viol_steps |   viol_with_pv_below_bound_pct |   ms_per_decision |   admm_iters_per_decision |
|:--------|:----------------------------|-------------------------:|--------------------:|-------------:|--------------------------:|-----------------------:|-------------------------:|-------------------------------:|------------------:|--------------------------:|
| caltech | mpc_conformal               |                   0.0314 |                 100 |         2.75 |                   54.304  |                 1.678  |                       11 |                            100 |           13.9089 |                    0      |
| caltech | admm_conformal (eps=0.001)  |                   0.0293 |                 100 |         0.5  |                   56.8899 |                 0.1531 |                        2 |                            100 |           59.2006 |                   23.3001 |
| caltech | admm_conformal (eps=0.0001) |                   0.0294 |                 100 |         0.5  |                   56.8331 |                 0.222  |                        2 |                            100 |           79.5795 |                   73.061  |
| jpl     | mpc_conformal               |                   0.0402 |                 100 |        37    |                   55.2943 |                16.4516 |                      148 |                            100 |           18.3778 |                    0      |
| jpl     | admm_conformal (eps=0.001)  |                   0.038  |                 100 |         2    |                   57.3626 |                 0.6686 |                        8 |                            100 |           71.7839 |                   23.2109 |
| jpl     | admm_conformal (eps=0.0001) |                   0.0385 |                 100 |        20    |                   57.1455 |                 8.6727 |                       80 |                            100 |           77.5389 |                   83.8526 |

### Large hub (voltage-binding scenario)
| site    | method         |   hub_multiplier |   energy_served_pct |   cost_per_kwh_delivered |   viol_hours |   voltage_viol_steps |   transformer_viol_steps |   min_voltage_pu |
|:--------|:---------------|-----------------:|--------------------:|-------------------------:|-------------:|---------------------:|-------------------------:|-----------------:|
| caltech | edf            |                2 |            100      |                   0.0486 |         0    |                    0 |                        0 |           0.9532 |
| caltech | mpc_point      |                2 |            100      |                   0.0463 |         2.75 |                   11 |                        0 |           0.9486 |
| caltech | mpc_conformal  |                2 |            100      |                   0.0481 |         0    |                    0 |                        0 |           0.952  |
| caltech | admm_conformal |                2 |            100      |                   0.0468 |         0    |                    0 |                        0 |           0.952  |
| caltech | offline_opt    |                2 |            100      |                   0.0439 |         0    |                    0 |                        0 |           0.9509 |
| caltech | edf            |                3 |             99.9464 |                   0.0546 |         0    |                    0 |                        0 |           0.9515 |
| caltech | mpc_point      |                3 |            100      |                   0.0525 |         9    |                   36 |                        0 |           0.9475 |
| caltech | mpc_conformal  |                3 |            100      |                   0.054  |         0    |                    0 |                        0 |           0.9506 |
| caltech | admm_conformal |                3 |             99.806  |                   0.0537 |         0    |                    0 |                        0 |           0.9512 |
| caltech | offline_opt    |                3 |            100      |                   0.0514 |         0    |                    0 |                        0 |           0.9508 |
| caltech | edf            |                4 |             99.5363 |                   0.0591 |         0    |                    0 |                        0 |           0.9505 |
| caltech | mpc_point      |                4 |            100      |                   0.0571 |        17.5  |                   70 |                        0 |           0.9467 |
| caltech | mpc_conformal  |                4 |             99.9929 |                   0.0585 |         0    |                    0 |                        0 |           0.9505 |
| caltech | admm_conformal |                4 |             98.2177 |                   0.0578 |         0    |                    0 |                        0 |           0.9512 |
| caltech | offline_opt    |                4 |            100      |                   0.0565 |         0    |                    0 |                        0 |           0.9508 |
| jpl     | edf            |                2 |             99.9994 |                   0.0516 |         0.75 |                    3 |                        0 |           0.9496 |
| jpl     | mpc_point      |                2 |            100      |                   0.0517 |         6.25 |                   25 |                        0 |           0.9477 |
| jpl     | mpc_conformal  |                2 |            100      |                   0.0517 |         1.25 |                    5 |                        0 |           0.9493 |
| jpl     | admm_conformal |                2 |             99.9931 |                   0.0518 |         0    |                    0 |                        0 |           0.95   |
| jpl     | offline_opt    |                2 |            100      |                   0.0503 |         0    |                    0 |                        0 |           0.9507 |
| jpl     | edf            |                3 |             98.9219 |                   0.0578 |         3.75 |                   15 |                        0 |           0.9488 |
| jpl     | mpc_point      |                3 |             99.7408 |                   0.0572 |        19.5  |                   78 |                        0 |           0.946  |
| jpl     | mpc_conformal  |                3 |             99.3649 |                   0.0577 |         8.5  |                   34 |                        0 |           0.9484 |
| jpl     | admm_conformal |                3 |             97.6509 |                   0.0578 |         4.75 |                   19 |                        0 |           0.9484 |
| jpl     | offline_opt    |                3 |             99.9835 |                   0.0568 |         0    |                    0 |                        0 |           0.9507 |
| jpl     | edf            |                4 |             91.7207 |                   0.0603 |         9.5  |                   38 |                        0 |           0.9484 |
| jpl     | mpc_point      |                4 |             96.355  |                   0.0603 |        31.5  |                  126 |                        0 |           0.946  |
| jpl     | mpc_conformal  |                4 |             92.2255 |                   0.0598 |         9.5  |                   38 |                        0 |           0.9484 |
| jpl     | admm_conformal |                4 |             88.0237 |                   0.0597 |         7.25 |                   29 |                        0 |           0.9484 |
| jpl     | offline_opt    |                4 |             96.999  |                   0.0602 |         0    |                    0 |                        0 |           0.9507 |

### Statistics (permutation test, equivalence tolerance)
| site    | baseline      | metric                  |   n_days |   mean_diff |   ci95_lo |   ci95_hi |   p_holm | verdict                             |
|:--------|:--------------|:------------------------|---------:|------------:|----------:|----------:|---------:|:------------------------------------|
| caltech | uncontrolled  | cost_per_kwh_delivered  |      365 |     -0.0045 |   -0.0055 |   -0.0037 |   0.0006 | proposed better                     |
| caltech | uncontrolled  | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | uncontrolled  | any_viol_steps          |      365 |     -0.1205 |   -0.2027 |   -0.0575 |   0.0051 | proposed better                     |
| caltech | uncontrolled  | pv_self_consumption_pct |      365 |      7.92   |    6.6499 |    9.5575 |   0.0006 | proposed better                     |
| caltech | uncontrolled  | peak_net_kw             |      365 |    -26.6091 |  -29.9658 |  -23.5856 |   0.0006 | proposed better                     |
| caltech | edf           | cost_per_kwh_delivered  |      365 |     -0.0045 |   -0.0055 |   -0.0037 |   0.0006 | proposed better                     |
| caltech | edf           | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | edf           | any_viol_steps          |      365 |     -0.0027 |   -0.0247 |    0.0164 |   1      | equivalent (|diff| below tolerance) |
| caltech | edf           | pv_self_consumption_pct |      365 |      7.8494 |    6.5888 |    9.4675 |   0.0006 | proposed better                     |
| caltech | edf           | peak_net_kw             |      365 |    -24.3397 |  -27.4559 |  -21.4784 |   0.0006 | proposed better                     |
| caltech | llf           | cost_per_kwh_delivered  |      365 |     -0.0045 |   -0.0055 |   -0.0037 |   0.0006 | proposed better                     |
| caltech | llf           | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | llf           | any_viol_steps          |      365 |     -0.0082 |   -0.0329 |    0.011  |   1      | equivalent (|diff| below tolerance) |
| caltech | llf           | pv_self_consumption_pct |      365 |      7.8941 |    6.6297 |    9.5227 |   0.0006 | proposed better                     |
| caltech | llf           | peak_net_kw             |      365 |    -24.3591 |  -27.4872 |  -21.4959 |   0.0006 | proposed better                     |
| caltech | mpc_point     | cost_per_kwh_delivered  |      365 |      0.0016 |    0.0011 |    0.0021 |   0.0006 | proposed worse                      |
| caltech | mpc_point     | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | mpc_point     | any_viol_steps          |      365 |     -0.1205 |   -0.2    |   -0.0603 |   0.0009 | proposed better                     |
| caltech | mpc_point     | pv_self_consumption_pct |      365 |     -2.6991 |   -3.3226 |   -1.9873 |   0.0006 | proposed worse                      |
| caltech | mpc_point     | peak_net_kw             |      365 |    -21.7227 |  -27.9008 |  -15.3379 |   0.0006 | proposed better                     |
| caltech | mpc_conformal | cost_per_kwh_delivered  |      365 |     -0.0017 |   -0.0023 |   -0.0012 |   0.0006 | proposed better                     |
| caltech | mpc_conformal | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | mpc_conformal | any_viol_steps          |      365 |     -0.0247 |   -0.0712 |    0.0082 |   1      | no significant difference           |
| caltech | mpc_conformal | pv_self_consumption_pct |      365 |      2.586  |    1.9015 |    3.5432 |   0.0006 | proposed better                     |
| caltech | mpc_conformal | peak_net_kw             |      365 |    -28.6269 |  -32.1178 |  -25.4977 |   0.0006 | proposed better                     |
| caltech | offline_opt   | cost_per_kwh_delivered  |      365 |      0.0037 |    0.0031 |    0.0043 |   0.0006 | proposed worse                      |
| caltech | offline_opt   | energy_served_pct       |      365 |     -0      |   -0      |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| caltech | offline_opt   | any_viol_steps          |      365 |      0.0055 |    0      |    0.0164 |   1      | equivalent (|diff| below tolerance) |
| caltech | offline_opt   | pv_self_consumption_pct |      365 |     -5.0628 |   -5.8829 |   -4.1699 |   0.0006 | proposed worse                      |
| caltech | offline_opt   | peak_net_kw             |      365 |    -13.2247 |  -17.7767 |   -8.5922 |   0.0006 | proposed better                     |
| jpl     | uncontrolled  | cost_per_kwh_delivered  |      352 |     -0.0021 |   -0.0027 |   -0.0016 |   0.0006 | proposed better                     |
| jpl     | uncontrolled  | energy_served_pct       |      352 |     -0      |   -0.0001 |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| jpl     | uncontrolled  | any_viol_steps          |      352 |     -4.142  |   -4.4489 |   -3.9289 |   0.0006 | proposed better                     |
| jpl     | uncontrolled  | pv_self_consumption_pct |      352 |      4.7654 |    3.7096 |    6.0316 |   0.0006 | proposed better                     |
| jpl     | uncontrolled  | peak_net_kw             |      352 |    -75.248  |  -80.7795 |  -70.8233 |   0.0006 | proposed better                     |
| jpl     | edf           | cost_per_kwh_delivered  |      352 |     -0.0013 |   -0.0018 |   -0.0009 |   0.0006 | proposed better                     |
| jpl     | edf           | energy_served_pct       |      352 |      0.0245 |    0.014  |    0.0373 |   0.0006 | proposed better                     |
| jpl     | edf           | any_viol_steps          |      352 |     -0.2188 |   -0.4063 |   -0.0852 |   0.0028 | proposed better                     |
| jpl     | edf           | pv_self_consumption_pct |      352 |      3.4889 |    2.5742 |    4.5817 |   0.0006 | proposed better                     |
| jpl     | edf           | peak_net_kw             |      352 |    -26.0972 |  -29.3337 |  -23.0085 |   0.0006 | proposed better                     |
| jpl     | llf           | cost_per_kwh_delivered  |      352 |     -0.0019 |   -0.0024 |   -0.0014 |   0.0006 | proposed better                     |
| jpl     | llf           | energy_served_pct       |      352 |     -0      |   -0.0001 |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| jpl     | llf           | any_viol_steps          |      352 |     -0.3125 |   -0.5398 |   -0.1448 |   0.0012 | proposed better                     |
| jpl     | llf           | pv_self_consumption_pct |      352 |      4.3838 |    3.379  |    5.6085 |   0.0006 | proposed better                     |
| jpl     | llf           | peak_net_kw             |      352 |    -26.3518 |  -29.6    |  -23.2759 |   0.0006 | proposed better                     |
| jpl     | mpc_point     | cost_per_kwh_delivered  |      352 |     -0.0004 |   -0.0007 |   -0.0002 |   0.0008 | proposed better                     |
| jpl     | mpc_point     | energy_served_pct       |      352 |     -0      |   -0.0001 |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| jpl     | mpc_point     | any_viol_steps          |      352 |     -2.1932 |   -2.7443 |   -1.6676 |   0.0006 | proposed better                     |
| jpl     | mpc_point     | pv_self_consumption_pct |      352 |     -0.127  |   -0.5807 |    0.3454 |   0.5447 | no significant difference           |
| jpl     | mpc_point     | peak_net_kw             |      352 |    -33.5894 |  -37.2838 |  -29.834  |   0.0006 | proposed better                     |
| jpl     | mpc_conformal | cost_per_kwh_delivered  |      352 |     -0.0014 |   -0.0018 |   -0.001  |   0.0006 | proposed better                     |
| jpl     | mpc_conformal | energy_served_pct       |      352 |     -0      |   -0.0001 |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| jpl     | mpc_conformal | any_viol_steps          |      352 |     -0.3977 |   -0.6364 |   -0.2045 |   0.0006 | proposed better                     |
| jpl     | mpc_conformal | pv_self_consumption_pct |      352 |      2.0683 |    1.4746 |    2.7548 |   0.0006 | proposed better                     |
| jpl     | mpc_conformal | peak_net_kw             |      352 |    -26.0155 |  -29.3085 |  -22.7147 |   0.0006 | proposed better                     |
| jpl     | offline_opt   | cost_per_kwh_delivered  |      352 |      0.002  |    0.0015 |    0.0025 |   0.0006 | proposed worse                      |
| jpl     | offline_opt   | energy_served_pct       |      352 |     -0      |   -0.0001 |   -0      |   0.0006 | equivalent (|diff| below tolerance) |
| jpl     | offline_opt   | any_viol_steps          |      352 |      0.0227 |    0      |    0.0483 |   0.6297 | no significant difference           |
| jpl     | offline_opt   | pv_self_consumption_pct |      352 |     -1.759  |   -2.2283 |   -1.3188 |   0.0006 | proposed worse                      |
| jpl     | offline_opt   | peak_net_kw             |      352 |    -28.8795 |  -32.1704 |  -25.6993 |   0.0006 | proposed better                     |