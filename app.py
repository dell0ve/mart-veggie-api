from flask import Flask, request, jsonify
import joblib

model = joblib.load("smart_veggie_model.pkl")

app = Flask(__name__)

@app.route('/')
def index():
    return "Smart Veggie Scan API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        voltage = float(request.json['voltage'])
        result = model.predict([[voltage]])
        risk = "เสี่ยง" if result[0] == 1 else "ปลอดภัย"
        return jsonify({'voltage': voltage, 'result': risk})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
