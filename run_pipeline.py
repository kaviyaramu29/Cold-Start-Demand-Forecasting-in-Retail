import os
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error

from src.data_preprocess import load_data, preprocess
from src.model_train import train_baseline

# -----------------------------
# 1. Load and preprocess data
# -----------------------------
DATA_PATH = r"C:/Users/Kaviy/OneDrive/Desktop/coldstart-forecasting/data"
panel_train, calendar_future, price_plan_future, promos_future, weather_future, metadata = load_data(DATA_PATH)
panel_train = preprocess(panel_train)

# -----------------------------
# 2. Train or load model
# -----------------------------
MODEL_PATH = os.path.join("outputs", "model.pkl")   # ✅ define it
os.makedirs("outputs", exist_ok=True)

features = ["price", "promo_flag", "holiday_flag", "temp_c", "rain_mm"]

if os.path.exists(MODEL_PATH):
    print("📂 Loading existing model...")
    model = joblib.load(MODEL_PATH)

    # ✅ Re-evaluate RMSE
    X = panel_train[features]
    y = panel_train["units"]
    preds = model.predict(X)
    rmse = np.sqrt(mean_squared_error(y, preds))
    print(f"Loaded Model RMSE (on full data): {rmse:.2f}")

else:
    print("🚀 Training model...")
    model, rmse = train_baseline(panel_train)   # update train_baseline to return both
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model trained and saved to {MODEL_PATH} (RMSE: {rmse:.2f})")
