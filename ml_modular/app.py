from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo
modelo = joblib.load("modelo.pkl")

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "API de predicción Breast Cancer lista",
        "features_expected": "30 valores numéricos"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = modelo.predict(features)[0]
        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
