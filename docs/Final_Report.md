# 📘 Final Project Summary Report

## 🧠 Project Title
**Cryptocurrency Liquidity Prediction for Market Stability**

## 🎯 Objective
To predict liquidity levels of cryptocurrencies using market indicators such as price changes, trading volume, and volatility. This helps traders and institutions anticipate potential liquidity crises.

## 📁 Dataset Overview
- Sources: CoinGecko datasets for March 16 & 17, 2022
- Records: 1000 entries, 506 unique coins
- Features: Price, 1h/24h/7d % changes, 24h volume, market cap

## 🔧 Data Preprocessing
- Handled missing values via median imputation
- Log-transformed volume and market cap for normalization
- Engineered features:
  - `liquidity_score = (volume / market_cap) * volatility`
  - 2-day moving average (price)

## 📊 Exploratory Data Analysis (EDA)
- Most coins have low liquidity; a few dominate
- High correlation between market cap and volume
- Volatility positively affects liquidity in small-cap coins

## 🤖 Model Training
- Model: **Random Forest Regressor**
- Tuning: GridSearchCV over 12 hyperparameter combinations
- Metrics: RMSE, MAE, R²

## 📦 Deployment
- **Flask-based API** with `/predict` endpoint
- Accepts JSON or form input and returns predicted liquidity
- Web UI with `index.html` and `result.html`

## 📄 Deliverables
- Trained Model: `liquidity_model.pkl`
- Scaler: `scaler.pkl`
- Flask App: `app.py`, HTML templates
- EDA, HLD, and LLD Documentation
- `requirements.txt` for environment setup

## ✅ Key Insights
- Liquidity is largely driven by volume and volatility
- Major coins act as stabilizers for overall market liquidity
- Predicting liquidity helps mitigate potential trading risks
