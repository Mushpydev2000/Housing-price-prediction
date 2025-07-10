from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any
import numpy as np

# Load the model and scaler
with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Define the FastAPI app
app = FastAPI()

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected input schema
class HouseFeatures(BaseModel):
    LotArea: float
    GrLivArea: float
    OverallQual: int
    TotalBsmtSF: float
    GarageCars: int
    YearBuilt: int
    YearRemodAdd: int
    HouseStyle: str
    SaleCondition: str
    Neighborhood: str

@app.post('/predict')
def predict(features: List[HouseFeatures]):
    # Convert input to DataFrame
    df = pd.DataFrame([f.dict() for f in features])
    # One-hot encode categorical features
    cat_features = ['HouseStyle', 'SaleCondition', 'Neighborhood']
    df_cat = df[cat_features].astype(str)
    df_cat_encoded = encoder.transform(df_cat)
    cat_feature_names = encoder.get_feature_names_out(cat_features)
    df_cat_encoded = pd.DataFrame(df_cat_encoded, columns=cat_feature_names, index=df.index)
    # Combine all features
    X = pd.concat([
        df[['LotArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'GarageCars', 'YearBuilt', 'YearRemodAdd']].reset_index(drop=True),
        df_cat_encoded.reset_index(drop=True)
    ], axis=1)
    X['GrLivArea_x_OverallQual'] = df['GrLivArea'] * df['OverallQual']
    # Scale features
    X_scaled = scaler.transform(X)
    # Predict log SalePrice and convert back
    y_pred_log = model.predict(X_scaled)
    y_pred = np.expm1(y_pred_log)
    return {'predictions': y_pred.tolist()}
