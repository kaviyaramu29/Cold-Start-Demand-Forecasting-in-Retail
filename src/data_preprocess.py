import pandas as pd
import json
import os

def load_data(data_dir="data"):  # ✅ now accepts a folder path
    panel_train = pd.read_csv(os.path.join(data_dir, "panel_train.csv"), parse_dates=["week_start"])
    calendar_future = pd.read_csv(os.path.join(data_dir, "calendar_future.csv"), parse_dates=["week_start"])
    price_plan_future = pd.read_csv(os.path.join(data_dir, "price_plan_future.csv"), parse_dates=["week_start"])
    promos_future = pd.read_csv(os.path.join(data_dir, "promos_future.csv"), parse_dates=["week_start", "week_end"])
    weather_future = pd.read_csv(os.path.join(data_dir, "weather_future.csv"), parse_dates=["week_start"])
    
    with open(os.path.join(data_dir, "metadata.json"), "r") as f:
        metadata = json.load(f)

    return panel_train, calendar_future, price_plan_future, promos_future, weather_future, metadata


def preprocess(panel_train):
    panel_train["market"] = panel_train["market"].astype(str)
    panel_train["sku_id"] = panel_train["sku_id"].astype(str)

    panel_train = panel_train.fillna(method="ffill").fillna(method="bfill")
    panel_train = panel_train.sort_values(["market", "sku_id", "week_start"])
    return panel_train
