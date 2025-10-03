# src/model_train.py
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

def train_baseline(panel_train):
    # Feature set
    features = ["price", "promo_flag", "holiday_flag", "temp_c", "rain_mm"]
    target = "units"

    X = panel_train[features]
    y = panel_train[target]

    # Simple train-test split (not time-aware yet, just to check pipeline)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train LightGBM model
    model = lgb.LGBMRegressor(
        n_estimators=200,
        learning_rate=0.05,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"Baseline RMSE: {rmse:.2f}")

    return model, rmse
