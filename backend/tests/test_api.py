import requests

url = "http://localhost:8000/predict"

# Example: two houses
payload = [
    {
        "LotArea": 8450,
        "GrLivArea": 1710,
        "OverallQual": 7,
        "TotalBsmtSF": 856,
        "GarageCars": 2,
        "YearBuilt": 2003,
        "YearRemodAdd": 2003,
        "HouseStyle": "2Story",
        "SaleCondition": "Normal",
        "Neighborhood": "CollgCr"
    },
    {
        "LotArea": 9600,
        "GrLivArea": 1262,
        "OverallQual": 6,
        "TotalBsmtSF": 1262,
        "GarageCars": 2,
        "YearBuilt": 1976,
        "YearRemodAdd": 1976,
        "HouseStyle": "1Story",
        "SaleCondition": "Abnorml",
        "Neighborhood": "Veenker"
    }
]

response = requests.post(url, json=payload)
print("Status code:", response.status_code)
print("Response:", response.json())
