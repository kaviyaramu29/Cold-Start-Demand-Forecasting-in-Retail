import pandas as pd
import matplotlib.pyplot as plt
import os
from src.forecast import prepare_future_data, generate_forecast

# Always use project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # project root
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "scenarios")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_scenario_analysis(model, calendar_future, price_plan_future, promos_future, weather_future, market="Jaipur"):
    # Step 1: Build base future dataset
    future, features = prepare_future_data(calendar_future, price_plan_future, promos_future, weather_future, market)

    # ---- Scenario 1: Base Case ----
    base_file = os.path.join(OUTPUT_DIR, "forecast_base.csv")
    base = generate_forecast(model, future.copy(), features, output_file=base_file)

    # ---- Scenario 2: Price Cut (-10%) ----
    pricecut_file = os.path.join(OUTPUT_DIR, "forecast_pricecut.csv")
    future_pricecut = future.copy()
    future_pricecut["price"] = future_pricecut["price"] * 0.9
    pricecut = generate_forecast(model, future_pricecut, features, output_file=pricecut_file)

    # ---- Scenario 3: Promo Boost ----
    promoboost_file = os.path.join(OUTPUT_DIR, "forecast_promoboost.csv")
    future_promoboost = future.copy()
    future_promoboost["promo_flag"] = 1
    promoboost = generate_forecast(model, future_promoboost, features, output_file=promoboost_file)

    # Step 2: Compare total demand
    comp_file = os.path.join(OUTPUT_DIR, "scenario_comparison.csv")
    comp = pd.DataFrame({
        "Scenario": ["Base", "PriceCut (-10%)", "PromoBoost"],
        "Total Units": [
            base["forecast_units"].sum(),
            pricecut["forecast_units"].sum(),
            promoboost["forecast_units"].sum()
        ]
    })
    comp.to_csv(comp_file, index=False)
    print(f"✅ Scenario comparison saved to {comp_file}")

    # Step 3: Per-SKU comparison
    sku_file = os.path.join(OUTPUT_DIR, "sku_scenario_comparison.csv")
    sku_comp = base.groupby("sku_id")["forecast_units"].sum().reset_index().rename(columns={"forecast_units": "Base"})
    sku_comp["PriceCut"] = pricecut.groupby("sku_id")["forecast_units"].sum().values
    sku_comp["PromoBoost"] = promoboost.groupby("sku_id")["forecast_units"].sum().values
    sku_comp["PriceCut_%Change"] = ((sku_comp["PriceCut"] - sku_comp["Base"]) / sku_comp["Base"]) * 100
    sku_comp["PromoBoost_%Change"] = ((sku_comp["PromoBoost"] - sku_comp["Base"]) / sku_comp["Base"]) * 100
    sku_comp.to_csv(sku_file, index=False)
    print(f"✅ Per-SKU scenario comparison saved to {sku_file}")

    # Step 4: Weekly chart
    plot_file = os.path.join(OUTPUT_DIR, "scenario_analysis.png")
    base_weekly = base.groupby("week_start")["forecast_units"].sum()
    pricecut_weekly = pricecut.groupby("week_start")["forecast_units"].sum()
    promoboost_weekly = promoboost.groupby("week_start")["forecast_units"].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(base_weekly.index, base_weekly.values, label="Base", marker="o")
    plt.plot(pricecut_weekly.index, pricecut_weekly.values, label="Price Cut (-10%)", marker="x")
    plt.plot(promoboost_weekly.index, promoboost_weekly.values, label="Promo Boost", marker="^")

    plt.title(f"Scenario Analysis: {market} Demand Forecast (Total Units)")
    plt.xlabel("Week Start")
    plt.ylabel("Forecasted Units")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(plot_file)
    plt.show()
    print(f"✅ Scenario analysis plot saved to {plot_file}")

    # Debug: confirm files exist
    for f in [base_file, pricecut_file, promoboost_file, comp_file, sku_file, plot_file]:
        print(f, "Exists? ->", os.path.exists(f))

    return comp, sku_comp
