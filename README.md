# 💹 Cryptocurrency Liquidity Prediction ML Project

This project aims to predict the **liquidity score** of cryptocurrencies using multiple regression models and hyperparameter tuning. It includes a web-based API using **Flask** with a responsive Bootstrap UI that dynamically switches between light and dark mode based on **sunrise and sunset times (6 AM to 6 PM)**.



## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning with GridSearchCV (XGBoost, Random Forest, etc.)
- 🔬 Hyperparameter Tuning
- 🌞🌜 Auto Light/Dark Mode Detection using Timezone
- 📈 Evaluation Metrics (R², RMSE, MAE)
- 🧪 Pickle Model & Scaler
- 🌐 Flask Web App with Bootstrap Styling



## 🏗️ Project Structure


.
├── app.py                     # Flask application (sunrise/sunset theme logic)
├── models/
│   ├── liquidity_model.pkl    # Trained ML model
│   └── scaler.pkl             # Scaler for input preprocessing
├── templates/
│   ├── index.html             # Homepage input form
│   └── result.html            # Result display page
└── README.md                  # Project documentation



## 🛠️ How to Run

### 🧷 Step-by-Step Guide

1. **Local Host**  

   -url → http://127.0.0.1:5000/

   **🚀 Render Link**

    - Go to → https://crypto-currecy-liquidity-ml-project.onrender.com


2. **Install dependencies**  

pip install -r requirements.txt


3. **Run the Flask app**  

python app.py


4. **Optional: Run with Gunicorn (Render/Production)**  

gunicorn app:app --bind 0.0.0.0:5000



## 🌗 Dynamic Light/Dark Theme

The interface automatically switches:
- 🌞 **Light Mode** → 6 AM to 6 PM IST
- 🌜 **Dark Mode** → Otherwise



## 🧠 Model Insights

- Models Tried: RandomForest, GradientBoosting, XGBoost
- Best Model: ✅ RandomForest (based on R², MAE, RMSE)
- Auto-scaled features for better prediction



## 🧪 Input Features

- `Price`, `1 hr`, `24 hr`, `7 days`, `24 hr volume`, `Market Cap`, `Date`



## 📌 Author

Created by `evilVirus7` with 💙 and Machine Learning."# -Crypto_Currency_Liquidity_Project" 
"# -Crypto_Currency_Liquidity_Project" "# Crypto_Currecy-Liquidity_ML_Project" 
