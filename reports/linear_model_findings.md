# Linear Regression Results (Daily & Hourly)

## 1. Objective

Predict total bike rentals (`cnt`) using weather and calendar/time features at **daily** and **hourly** resolutions, then translate insights into operational recommendations.

---

## 2. Data & Method (brief)

- **Datasets:** `day.csv`, `hour.csv` (UCI Bike Sharing)
- **Target:** `cnt` (total rentals)
- **Dropped columns:** `instant`, `dteday`, `casual`, `registered`, `cnt` (IDs & leakage)
- **Pipeline:** One-hot encode categorical (season, mnth, hr, etc.) + standard-scale numeric (temp, atemp, hum, windspeed) → LinearRegression
- **Split:** 80% train / 20% test

---

## 3. Performance

| Model  | R²    | RMSE  | MAE   |
| ------ | ----- | ----- | ----- |
| Daily  | 0.842 | 796.5 | 583.0 |
| Hourly | 0.681 | 100.4 | 74.1  |

---

## 4. Key Drivers

### Daily Model

- **− Weather (weathersit_3):** −1,048 rentals
- **+ Year (yr_1):** +991 rentals (2012 vs 2011)
- **− Winter (season_1):** −856 rentals; **+ Fall (season_4):** +798
- **+ Clear weather (weathersit_1):** +778 rentals
- **+ Temperature:** +686 rentals per 1 SD increase
- **Month effects:** Sep (+639), Jul (−484), etc.
- **+ Sunday (weekday_6):** +286 rentals

### Hourly Model

- **+ Hour 17 (5 PM):** +257; **Hour 18:** +217; **Hour 8:** +191
- **− Hours 0–6:** −125 to −165 rentals (overnight)
- **− Worst weather (weathersit_4):** −77 rentals

**Takeaways:**  
Bad weather and winter sharply reduce demand; warmth, fall and clear days boost it. Commute‐hour spikes dominate hourly patterns.

---

## 5. Residual Diagnostics

- **Daily:** residuals evenly scattered around zero; slight non-linearity at extremes
- **Hourly:** residual variance grows with predicted values (heteroscedasticity), suggesting non-linear effects

---

## 6. Segment Analyses

### 6.1 Casual vs Registered

- **Predictive Power:** Daily R²—Registered 0.846 vs Casual 0.707; Hourly R²—Registered 0.676 vs Casual 0.585
- **Patterns:** Registered riders peak at commute hours; casual riders have a flatter late-day profile and spike on weekends

**Daily Drivers (Casual):** Temperature +336; Sunday +270; Fall (Oct) +210; Working day −297  
**Daily Drivers (Registered):** Bad weather −851; Year +851; Fall +817; Winter −772

**Hourly Drivers (Casual):** Hour 17 +32; Hours 13–16 +29–31  
**Hourly Drivers (Registered):** Hour 17 +225; Hour 8 +199; Hour 18 +197; Overnight (hr 2–4) −135 to −137

### 6.2 Working vs Non-Working

- **Predictive Power:** Daily R²—Working 0.822 vs Non-Working 0.811; Hourly R²—Working 0.838 vs Non-Working 0.778
- **Patterns:** Working days show sharp 8 AM/5 PM peaks; non-working days have a broad midday plateau and strong Sunday surge

**Daily Drivers (Working):** Feels-like temp +1,061; Year ±1,037; Bad weather −995  
**Daily Drivers (Non-Working):** Sunday +1,275; December −1,615; Bad weather −1,516

**Hourly Drivers (Working):** Hour 17 +317; Hour 8 +301; Hour 18 +289; Overnight troughs (hr 3–4) −172 to −178  
**Hourly Drivers (Non-Working):** Hours 12–15 +166–167; Early-morning trough (hr 4) −151

---

## 7. Recommendations

1. **Rebalancing:** Focus on 8 AM & 5–6 PM; perform maintenance overnight/low-demand hours.
2. **Weather-aware ops:** Adjust routes & staffing on bad-weather days; promote riding on clear/warm days.
3. **Seasonal campaigns:** Launch before spring/fall demand spikes.
4. **Segmentation:** Build separate models for casual vs registered riders.
5. **Model improvements:** Experiment with non-linear models and time-series validation.

---

## 8. Risks / Unknowns

- Data leakage if `casual`/`registered` are used as predictors
- External events (concerts, strikes) not captured
- Linear assumptions (linearity, constant variance) may be violated
- Usage patterns may shift across years or cities
- System-level aggregation hides station-level issues

---

## Appendix

See `notebooks/linear_models.ipynb` for full code and workflow outline.
