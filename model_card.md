# 📑 Model Card: Cold Start Demand Forecasting

## Model Details
- **Name**: Cold Start Demand Forecasting Model
- **Algorithm**: LightGBM Regressor
- **Task**: Predict weekly demand (units sold) for SKUs in a cold-start forecasting setup.

## Training Data
- **Source**: `panel_train.csv` (historical panel data).
- **Granularity**: Weekly sales.
- **Markets**: Includes Jaipur_NewCity and potentially others.
- **Features Used**:
  - `price` (planned selling price)
  - `promo_flag` (whether a promotion is active)
  - `holiday_flag` (holiday effect indicator)
  - `temp_c` (weekly average temperature)
  - `rain_mm` (weekly rainfall in mm)
- **Target**: `units` (number of units sold).

## Evaluation
- **Split Method**: 80/20 simple train-test split.
- **Metric**: RMSE (Root Mean Squared Error) on hold-out data.
- **Observed Performance**:  Model RMSE: 12.78


## Explainability
- **Method**: SHAP (SHapley Additive exPlanations).
- **Findings**:
  - **Temperature (temp_c)**: Strongest driver — higher temperatures generally increase demand.
  -**Price**: Major negative influence — lower prices lead to higher sales.
  -**Rainfall (rain_mm)**: Moderate impact, SKU-dependent — some products are sensitive to rain conditions.
  -**Promo Flag**: Strong positive effect — promotions consistently boost demand.
  -**Holiday Flag**: Positive but smaller spikes during holiday weeks.

Visual explainability plots are available in `outputs/plots/`.

## Limitations
- Cold start for completely new SKUs may not generalize well.
- Model assumes external data (weather, calendar, promos) is complete and accurate.
- Currently trained with simple validation; risk of overfitting.
- Only predicts short-term weekly demand.

## Ethical Considerations
- Should not be used for exploitative pricing strategies that harm consumers.
- Forecasts may reinforce existing biases in promotions or product availability.
- Should be monitored and used with human-in-the-loop decision-making.

## Intended Use
- Internal demand forecasting.
- Scenario simulation (e.g., price cut, promo boost).
- Strategic planning support.

**Not intended for**:  
- Direct deployment in automated dynamic pricing systems without oversight.  
- Critical safety-related applications.  
