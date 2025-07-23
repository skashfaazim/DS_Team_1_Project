# Linear Regression Results (Daily & Hourly)

## 1. Objective

Predict total bike rentals (`cnt`) using weather and calendar/time features at **daily** and **hourly** resolutions, then translate insights into operational recommendations.

---

## 2. Data & Method (brief)

- Datasets: `day.csv`, `hour.csv` (UCI Bike Sharing).
- Target: `cnt` (total rentals).
- Dropped leakage/ID cols: `instant`, `dteday`, `casual`, `registered`, `cnt`.
- Pipeline: OneHotEncode categorical codes (season, mnth, hr, etc.) + StandardScale numeric vars (temp, atemp, hum, windspeed) → LinearRegression.
- Split: 80/20 train-test.

---

## 3. Performance

| Model  | R²    | RMSE  | MAE   |
| ------ | ----- | ----- | ----- |
| Daily  | 0.842 | 796.5 | 583.0 |
| Hourly | 0.681 | 100.4 | 74.1  |

_(RMSE/MAE are in rental counts.)_

---

## 4. Key Drivers (|coef| top contributors)

### Daily Model

- **− weathersit_3** (light snow / heavy rain): −1048 → sharp drop in demand
- **+ yr_1** (2012 vs 2011): +991 → demand grew year-over-year
- **− yr_0** (2011 baseline): −991 (mirror of above dummy)
- **− season_1** (winter): −856; **+ season_4** (fall): +798
- **+ weathersit_1** (clear weather): +778
- **+ temp**: +686 (warmer days = more rides)
- **mnth effects:** + mnth_9 (Sep) +639; − mnth_7 (Jul) −484; etc.
- **+ weekday_6** (Sunday): +286 (higher weekend usage)

### Hourly Model

- **+ hr_17 (+257), hr_18 (+217), hr_8 (+191)** → commute peaks
- **− hr_0 ~ hr_6** (e.g., hr_4 −165) → off-hours low demand
- **− weathersit_4** (worst weather): −77

**Takeaways:**

- Weather & temperature strongly influence demand (bad weather ↓, warmth ↑).
- Clear temporal patterns: year-over-year growth, fall > winter, commute-hour spikes.

---

## 5. Residual Diagnostics

- (Insert short note after reviewing plots) e.g.:
  - Daily residuals: fairly homoscedastic, mild non-linearity at extremes.
  - Hourly residuals: variance increases at higher fitted values (heteroscedasticity); suggests non-linear/interaction effects.

---

## 6. Recommendations

1. **Operational Rebalancing:** Ensure bike/dock availability around 08:00 and 17:00–18:00; schedule maintenance in low-demand windows (late night/early morning).
2. **Weather-Aware Planning:** Use forecasts to adjust truck routes and staffing; push in-app promos on clear/warm days.
3. **Seasonal Campaigns:** Launch membership/marketing before demand spikes (spring/fall).
4. **Segmentation Next:** Model **casual vs registered** separately for tailored marketing and retention strategies.
5. **Model Improvements:** Try Ridge/Lasso or tree-based models (RF/XGB) for non-linearity; add lag features and event data; consider time-series CV.

---

## 7. Risks / Unknowns

- **Data leakage:** Using `casual`/`registered` would inflate scores (we excluded).
- **External events missing:** Concerts, strikes, policy changes not in data.
- **Model assumptions:** Linearity & constant variance not guaranteed.
- **Temporal drift:** Usage patterns may shift across years.
- **System-wide vs station-level:** Aggregation hides local shortages/excess.

---

## 8. Next Steps

- Add non-linear models & compare.
- Incorporate external/event features.
- Time-series validation (rolling splits).
- Produce stakeholder-specific dashboards.

---

## Appendix: Notebook Outline (`notebooks/linear_models.ipynb`)

1. Objective & Data Sources
2. Imports & Paths
3. Load & Quick Check
4. Prep Features/Targets (Daily & Hourly)
5. Pipeline + Train/Test Split
6. Fit & Evaluate (R², RMSE, MAE)
7. Diagnostics Plots (Pred vs Actual, Residuals)
8. Top Coefficients / Feature Importance
9. Save Figures & Outputs
10. Key Findings (summarized here)
