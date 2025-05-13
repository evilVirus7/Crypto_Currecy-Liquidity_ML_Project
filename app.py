from flask import Flask, render_template, request
import pandas as pd
import pickle
from datetime import datetime
import pytz

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("models/liquidity_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

def get_theme_mode():
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_tz = pytz.timezone('Asia/Kolkata')
    local_time = utc_now.astimezone(local_tz)
    light_start = local_time.replace(hour=6, minute=0, second=0, microsecond=0)
    light_end = local_time.replace(hour=18, minute=0, second=0, microsecond=0)
    return "light" if light_start <= local_time <= light_end else "dark"

@app.route('/')
def home():
    theme = get_theme_mode()
    return render_template('index.html', theme=theme)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = ['Price', '1 hr', '24 hr', '7 days', '24 hr volume', 'Market Cap', 'Date']
        inputs = [float(request.form[feature]) for feature in features]
        scaled_inputs = scaler.transform([inputs])
        prediction = model.predict(scaled_inputs)[0]
        theme = get_theme_mode()
        return render_template('result.html', prediction=round(prediction, 2), theme=theme)
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}", theme=get_theme_mode())

if __name__ == '__main__':
    app.run(debug=True)