import joblib
import pandas as pd

MODEL_PATH = "/models/failure_predictor.joblib"

def load_model():
    model = joblib.load(MODEL_PATH)
    return model

def predict_failure(df: pd.DataFrame):
    model = load_model()
    features = df[["temp_mean_3h", "vib_max_3h"]]
    predictions = model.predict(features)
    df["failure_prediction"] = predictions
    return df
