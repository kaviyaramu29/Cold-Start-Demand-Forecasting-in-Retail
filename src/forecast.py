# src/forecast.py
import pandas as pd
import os

def prepare_future_data(calendar_future, price_plan_future, promos_future, weather_future, market="Jaipur_NewCity"):
    # Filter future data for Jaipur
    price_plan_future = price_plan_future[price_plan_future["market"] == market].copy()
    promos_future = promos_future[promos_future["market"] == market].copy()
    weather_future = weather_future[weather_future["market"] == market].copy()

    # Rename planned_price → price to match training data
    price_plan_future = price_plan_future.rename(columns={"planned_price": "price"})

    # Merge future datasets
    future = calendar_future.copy()
    future = future.merge(price_plan_future, on=["week_start"], how="left")
    future = future.merge(weather_future, on=["week_start"], how="left")
    
    # Promo handling
    promos_future = promos_future.copy()
    promos_future.loc[:, "promo_flag"] = 1
    future = future.merge(promos_future[["sku_id", "week_start", "promo_flag"]], 
                          on=["week_start", "sku_id"], how="left")
    future["promo_flag"] = future["promo_flag"].fillna(0)

    # Ensure correct feature set
    features = ["price", "promo_flag", "holiday_flag", "temp_c", "rain_mm"]

    # Fill any missing values
    for col in features:
        if col not in future.columns:
            future[col] = 0

    future = future.fillna(0)
    return future, features



def generate_forecast(model, future, features, output_file="outputs/forecast.csv"):
    # Make sure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Predict units
    future["forecast_units"] = model.predict(future[features])
    
    # Save forecast file
    forecast = future[["week_start", "sku_id", "forecast_units"]]
    forecast.to_csv(output_file, index=False)
    print(f"✅ Forecast saved to {output_file}")
    return forecast