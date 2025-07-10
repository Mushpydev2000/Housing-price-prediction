# Housing Price Prediction

This project is a fullstack machine learning web app for predicting house prices using a trained XGBoost model, served with FastAPI and a modern HTML/JS frontend. It includes monitoring with Prometheus and Grafana.

---

## Project Structure

- `backend/` — FastAPI backend, model files, and utilities
- `frontend/` — HTML, CSS, JS for the web UI
- `infra/` — Dockerfile, docker-compose, Prometheus config
- `model-development/` — Notebooks and CSVs for model training (not needed in production)

---

## Prerequisites
- Docker and Docker Compose installed
- (Optional) Python 3.11+ if running locally without Docker

---

## Quick Start (Recommended: Docker Compose)

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Housing-price-prediction
   ```

2. **Build and run the backend (FastAPI) and monitoring stack:**
   ```sh
   cd infra
   docker-compose up -d
   ```
   - FastAPI backend: [http://localhost:8000](http://localhost:8000)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Grafana: [http://localhost:3000](http://localhost:3000) (login: admin/admin)

3. **Serve the frontend:**
   ```sh
   cd ../frontend
   python3 -m http.server 8080
   ```
   - Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## Making Predictions
- Fill in the form on the frontend and click "Predict" to get a house price prediction.
- The backend loads the trained model and preprocessing pipeline from `backend/app/model/`.

---

## Retraining the Model
- Use the notebook and CSVs in `model-development/` to retrain or improve the model.
- Export new model files (`xgb_model.pkl`, `scaler.pkl`, `encoder.pkl`) and replace the ones in `backend/app/model/`.
- Restart the backend container to use the new model.

---

## Production Files
See `production_files.py` for a list of essential files needed for deployment.

---

## License
MIT