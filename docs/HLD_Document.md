# 🧩 High-Level Design (HLD) Document

## 🧠 Project Title
**Cryptocurrency Liquidity Prediction for Market Stability**

## 🎯 Objective
Build a machine learning system that predicts cryptocurrency liquidity scores based on market factors to support risk management and stability insights.

## 📦 System Components

### 1. **Data Layer**
- **Input Files**: Historical crypto data (CSV: 2022-03-16 and 2022-03-17)
- **Format**: Price, volume, market cap, short-term percentage changes

### 2. **Preprocessing Module**
- Handle missing values (median imputation)
- Log transformation for skewed features
- Feature engineering:
  - Liquidity score
  - Rolling averages
  - Volatility estimates

### 3. **Exploratory Data Analysis (EDA)**
- Visualize distributions, correlations, and liquidity trends
- Identify top-performing coins by liquidity

### 4. **Model Training Module**
- ML algorithm: **Random Forest Regressor**
- Hyperparameter tuning with **GridSearchCV**
- Evaluation metrics: **RMSE**, **MAE**, **R²**

### 5. **Model Serialization**
- Save trained model using `pickle`
- Also save scaler object for consistent input formatting

### 6. **API Layer (FastAPI/Flask)**
- REST endpoint `/predict`
- Accepts JSON input with coin parameters
- Returns predicted liquidity score

### 7. **Frontend Layer**
- HTML templates served via Flask/FastAPI
- User form for entering market values
- Displays prediction result and confidence range

## 🔄 Data Flow
```
CSV Files --> Preprocessing --> Feature Engineering --> Model Training --> Pickle Model
User Input --> API (/predict) --> Model Inference --> Result Displayed via Template
```

## ✅ Output
- Trained model file: `liquidity_model.pkl`
- Web service: `app.py` with `templates/` UI
