# Main production files for the Housing Price Prediction app
# This file lists the essential files required for running the app in production.

production_files = [
    "backend/app/main.py",           # FastAPI backend entrypoint
    "backend/app/model/xgb_model.pkl",   # Trained XGBoost model
    "backend/app/model/scaler.pkl",      # Scaler for preprocessing
    "backend/app/model/encoder.pkl",     # Encoder for categorical features
    "backend/app/requirements.txt",      # Backend dependencies
    "infra/Dockerfile",                  # Dockerfile for backend
    "infra/docker-compose.yml",          # Docker Compose for infra
    "infra/prometheus.yml",              # Prometheus config
    "frontend/index.html",               # Frontend HTML
    "frontend/style.css",                # Frontend CSS
    "frontend/script.js",                # Frontend JS
]

if __name__ == "__main__":
    print("Production files for deployment:")
    for f in production_files:
        print(f)
