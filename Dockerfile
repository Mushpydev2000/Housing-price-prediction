# Dockerfile for serving the trained model with FastAPI
FROM python:3.11-slim-bullseye

# Update system packages to reduce vulnerabilities
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy model and code
COPY serve_model.py ./
COPY xgb_model.pkl ./
COPY scaler.pkl ./
COPY encoder.pkl ./

EXPOSE 8000

CMD ["uvicorn", "serve_model:app", "--host", "0.0.0.0", "--port", "8000"]
