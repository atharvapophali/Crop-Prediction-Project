from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('crop_model.pkl')  # Ensure this file is in the root

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        float(data['nitrogen']),
        float(data['phosphorus']),
        float(data['potassium']),
        float(data['temperature']),
        float(data['humidity']),
        float(data['ph']),
        float(data['rainfall'])
    ]
    prediction = model.predict([features])[0]
    return jsonify({'crop': prediction})

if __name__ == '__main__':
    app.run(debug=True)
