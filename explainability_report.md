# Explainability Report: Cold Start Forecasting

The model’s predictions were explained using **SHAP values**, which measure each feature’s contribution to predicted demand.

## Key Findings
SHAP Summary Plot (violin plot):

-Shows how each feature affects predictions at the individual level.

-Example: Higher temperature (temp_c) increases demand for certain SKUs.

-Price has strong negative SHAP values — higher prices reduce sales.

-Promo Flag and Holiday Flag positively influence demand spikes.

SHAP Feature Importance Plot (bar chart):

-Ranks features by average impact on predictions.

Top Drivers:

-temp_c (strongest seasonal/weather driver)

-price (second most important factor)

-rain_mm, promo_flag, and holiday_flag also contribute.

## Visuals
See `outputs/plots/`:
- `shap_summary.png` – shows feature impact distribution across all predictions.
- `shap_feature_importance.png` – shows overall importance ranking.

## Conclusion
The model relies most heavily on **price** and **temp_C**, aligning with business intuition. External features (promotions, holidays) provide secondary signals.
