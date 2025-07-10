import pickle
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
import numpy as np
from xgboost import XGBRegressor

# Load your cleaned training data and features (adjust as needed)
df_train = pd.read_csv('train.csv')
# ... apply the same cleaning and feature engineering as in your notebook ...
# For demonstration, here is a minimal placeholder:
# (You should copy the feature engineering code from your notebook)
def feature_engineering(df):
    features = ['LotArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'GarageCars', 'YearBuilt', 'YearRemodAdd']
    cat_features = ['HouseStyle', 'SaleCondition', 'Neighborhood']
    df_cat = df[cat_features].astype(str)
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    df_cat_encoded = encoder.fit_transform(df_cat)
    cat_feature_names = encoder.get_feature_names_out(cat_features)
    df_cat_encoded = pd.DataFrame(df_cat_encoded, columns=cat_feature_names, index=df.index)
    X = pd.concat([df[features].reset_index(drop=True), df_cat_encoded.reset_index(drop=True)], axis=1)
    X['GrLivArea_x_OverallQual'] = df['GrLivArea'] * df['OverallQual']
    y = df['SalePrice'].reset_index(drop=True)
    y_log = np.log1p(y)
    return X, y, y_log, encoder

X, y, y_log, encoder = feature_engineering(df_train)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train XGBoost model (use best params from notebook)
model = XGBRegressor(n_estimators=300, max_depth=8, learning_rate=0.1, subsample=1.0, random_state=42)
model.fit(X_scaled, y_log)

# Save model, scaler, and encoder
with open('xgb_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)
