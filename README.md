**"# Cold-Start-Demand-Forecasting-in-Retail" **
This project implements a **Cold Start Demand Forecasting pipeline**.  
It predicts weekly sales for SKUs using features like price, promotions, holidays, and weather.  
The pipeline also includes **scenario analysis** (e.g., price cuts, promo boosts) and **explainability** (SHAP feature importance).

---

**## 📂 Project Structure**
<img width="869" height="570" alt="image" src="https://github.com/user-attachments/assets/42d8f549-a914-4ff9-bff2-c9914558c3fd" />




**Prepare Data**

Place the following input files in the data/ folder:

panel_train.csv

calendar_future.csv

price_plan_future.csv

promos_future.csv

weather_future.csv

metadata.json

**▶️ How to Run**

From the project root, run:

python run_pipeline.py

This will:

Load & preprocess data

Train or load the LightGBM model

Generate a baseline forecast (outputs/forecast_baseline.csv)

Create explainability plots (outputs/plots/)

Run scenario analysis (price cut, promo boost) → saves results in outputs/scenarios/

**📊 Outputs**
Forecast file

outputs/forecast_baseline.csv

Explainability

outputs/plots/shap_summary.png

outputs/plots/shap_feature_importance.png

Scenario Analysis

outputs/scenarios/forecast_base.csv

outputs/scenarios/forecast_pricecut.csv

outputs/scenarios/forecast_promoboost.csv

outputs/scenarios/scenario_comparison.csv

outputs/scenarios/sku_scenario_comparison.csv

outputs/scenarios/scenario_analysis.png

**RESULTS**
1. Forecast units for new city (Jaipur), all SKU ids for the next 13 weeks (weekly):
   <img width="1515" height="236" alt="image" src="https://github.com/user-attachments/assets/c673d5d5-555c-43da-a51c-e981e43dd143" />

2. SHAP Summary


    <img width="800" height="350" alt="shap_summary" src="https://github.com/user-attachments/assets/af85820c-7c33-4188-8da1-ec9b7dec9b0b" />

  
3. SHAP feature importance
   <img width="800" height="350" alt="shap_feature_importance" src="https://github.com/user-attachments/assets/f5f8215f-2199-44f2-9734-9bf4cea5e57c" />

4. Forecast trends
   <img width="1200" height="600" alt="forecast_trends" src="https://github.com/user-attachments/assets/8c124328-1c45-4897-9d51-32674adda90c" />

5. scenario analysis(extra deliverable)
   <img width="1200" height="600" alt="scenario_analysis" src="https://github.com/user-attachments/assets/3019d4cf-e75c-4291-ac5f-0fc9433243dc" />


