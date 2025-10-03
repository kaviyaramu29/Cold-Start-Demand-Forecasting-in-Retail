# Cold-Start Demand Forecasting

**Task**: Forecast next 13 weeks of units for **Jaipur_NewCity** (all SKUs), using transfer from other markets.  

## Files 
- `panel_train.csv` — weekly panel up to T0. 
Columns:
  `week_start, market, sku_id, units, price, promo_flag, holiday_flag, temp_c, rain_mm`
- `calendar_future.csv`, `weather_future.csv`, `promos_future.csv`, `price_plan_future.csv`
- `metadata.json` — forecast origin and metadata.

**Primary key**: `(week_start, market, sku_id)`
