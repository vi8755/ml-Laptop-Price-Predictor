import pickle
from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

model = pickle.load(open('pipe.pkl', 'rb'))
laptop = pickle.load(open('laptop.pkl', 'rb'))

# ✅ Options API (correct column names)
@app.route('/options', methods=['GET'])
def options():
    return jsonify({
        "company": sorted(laptop['Company'].unique().tolist()),
        "type": sorted(laptop['TypeName'].unique().tolist()),
        "cpu": sorted(laptop['Cpu Brand'].unique().tolist()),
        "gpu": sorted(laptop['Gpu brand'].unique().tolist()),
        "os": sorted(laptop['os'].unique().tolist())
    })

# ✅ Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        features = pd.DataFrame([{
    'Company': data['company'],
    'TypeName': data['type'],
    'Ram': int(data['ram']),
    'Weight': float(data['weight']),
    'Touchscreen': int(data['touchscreen']),
    'IPS': int(data['ips']),
    'PPI': float(data['ppi']),
    'Cpu Brand': data['cpu'],
    'HDD': int(data['hdd']),
    'SSD': int(data['ssd']),
    'Gpu brand': data['gpu'],
    'os': data['os']
}])

        prediction = np.exp(model.predict(features)[0])

        return jsonify({"price": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)