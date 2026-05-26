from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, numpy as np, pandas as pd

app = Flask(__name__)
CORS(app)
knn_model = joblib.load('modelo_smote_knn.pkl')
knn_scaler = joblib.load('scaler_smote_knn.pkl')

mlp_model = joblib.load('modelo_smote_mlp.pkl')
mlp_scaler = joblib.load('scaler_smote_mlp.pkl')

CLASSES = ['Sin depresión', 'Con depresión']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    metodo = data['metodo']

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
    if metodo == "knn":

    features_scaled = knn_scaler.transform(features)

    pred = int(knn_model.predict(features_scaled)[0])

    proba = knn_model.predict_proba(features_scaled)[0]

elif metodo == "mlp":

    features_scaled = mlp_scaler.transform(features)

    pred = int(mlp_model.predict(features_scaled)[0])

    proba = mlp_model.predict_proba(features_scaled)[0]

else:

    return jsonify({
        'error': 'Método no válido'
    }), 400
    return jsonify({
        'prediccion': CLASSES[pred],
        'probabilidad': round(float(max(proba)), 4)
    })
if __name__== '__main__':
    app.run(debug=True, port=5000)
