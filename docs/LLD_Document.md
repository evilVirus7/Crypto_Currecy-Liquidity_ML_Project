# 🛠️ Low-Level Design (LLD) Document

## 📂 Module 1: Data Preprocessing
**File**: `preprocess.py`

### Functions:
- `load_data(file_path)`: Load CSV files
- `handle_missing(df)`: Median imputation for missing `1h`, `24h`, `7d`, `volume`
- `add_features(df)`: Create `liquidity_score`, log transforms, moving averages

## 📊 Module 2: Exploratory Data Analysis (EDA)
**File**: `eda.py`

### Functions:
- `plot_distribution(column)`: Plot histogram with KDE
- `plot_correlation_matrix(df)`: Seaborn heatmap of numeric features
- `top_liquidity_coins(df)`: Bar chart of top coins by average liquidity

## 🤖 Module 3: Model Training
**File**: `train_model.py`

### Functions:
- `prepare_features(df)`: Select and scale input features
- `train_rf_model(X, y)`: GridSearchCV over RandomForestRegressor
- `evaluate_model(y_true, y_pred)`: Print RMSE, MAE, R²
- `save_model(model, scaler)`: Save `liquidity_model.pkl`, `scaler.pkl`

## 🚀 Module 4: API Deployment (Flask/FastAPI)
**File**: `app.py`

### Routes:
- `/`: Renders input form (HTML)
- `/predict` (POST):
  - Accepts input from form or JSON
  - Loads `liquidity_model.pkl` & `scaler.pkl`
  - Transforms input, predicts liquidity, returns result

## 🖼️ Templates
**Folder**: `templates/`
- `index.html`: Input form (price, % changes, volume, market cap)
- `result.html`: Displays predicted liquidity score and model confidence

## 🧪 Testing
**File**: `test_model.py`
- Test model predictions on sample data
- Validate API responses using `requests` or `pytest`
