from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import scale

app = Flask(__name__)

model = joblib.load('model.joblib')

@app.route('/')
def home():
    return "API is working"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    input_data = np.array([
        data['TotalCharges'],
        data['MonthlyCharges'],  
        data['tenure'],
        data['Contract'],
        data['PaymentMethod'],
        data['OnlineSecurity'],
        data['TechSupport'],
        data['gender'],
        data['OnlineBackup'],
        data['InternetService'],
        data['PaperlessBilling']
    ]).reshape(1, -1)  
   
    input_data = scale.transform(input_data)

    prediction = model.predict(input_data)
    
    return jsonify(prediction=prediction[0])

# @app.route('/health', methods=['GET'])
# def health():
#     return jsonify(status="healthy")

if __name__ == '__main__':
    app.run(debug=True)
