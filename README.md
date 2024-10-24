### Install Python

- **Windows**: Download and install Python from the [official website](https://www.python.org/downloads/windows/). Make sure to check the box to add Python to your PATH during installation.
- **macOS**: You can install Python using Homebrew:
```bash
brew install python
```

### install dependencies
```
pip install -r requirements.txt
```

### Run Application
```
python3 app.py
```

### Testing

```
  curl -X POST http://127.0.0.1:5000/receipts/process -H "Content-Type: application/json" -d '{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
      {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
      {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
      {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
      {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
      {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
    ],
    "total": "35.35"
  }'
```

```
curl -X GET http://127.0.0.1:5000/receipts/{id}/points
```