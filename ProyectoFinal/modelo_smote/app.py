from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, numpy as np, pandas as pd

app = Flask(__name__)
CORS(app)
model = joblib.load('modelo_smote.pkl')
scaler = joblib.load('scaler_smote.pkl')

CLASSES = ['Sin depresión', 'Con depresión']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    departamento = data['departamento']
    if isinstance(departamento, str):
        departamento = departamento.lower()

    features = pd.DataFrame([[
        data['edad'],
        data['genero'],
        data['cgpa'],
        data['sueno'],
        data['estudio'],
        data['redes'],
        data['actividad'],
        data['estres'],
        1 if departamento == 'arts' else 0,
        1 if departamento == 'business' else 0,
        1 if departamento == 'engineering' else 0,
        1 if departamento == 'medical' else 0,
        1 if departamento == 'science' else 0,
    ]], columns=['Age', 'Gender', 'CGPA', 'Sleep_Duration', 'Study_Hours',
                 'Social_Media_Hours', 'Physical_Activity', 'Stress_Level',
                 'Department_arts', 'Department_business', 'Department_engineering',
                 'Department_medical', 'Department_science'])

    features = scaler.transform(features)
    pred = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]

    return jsonify({
        'prediccion': CLASSES[pred],
        'probabilidad': round(float(max(proba)), 4)
    })
if __name__== '__main__':
    app.run(debug=True, port=5000)