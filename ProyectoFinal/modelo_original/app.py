from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib, numpy as np, pandas as pd

app = Flask(__name__)
CORS(app)

knn_model = joblib.load('knn_modelo.pkl')
knn_scaler = joblib.load('knn_scaler.pkl')

mlp_model = joblib.load('mlp_modelo.pkl')
mlp_scaler = joblib.load('mlp_scaler.pkl')

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

    # KNN
    knn_features = knn_scaler.transform(features)
    knn_pred = int(knn_model.predict(knn_features)[0])
    knn_proba = knn_model.predict_proba(knn_features)[0]

    # MLP
    mlp_features = mlp_scaler.transform(features)
    mlp_pred = int(mlp_model.predict(mlp_features)[0])
    mlp_proba = mlp_model.predict_proba(mlp_features)[0]

    return jsonify({
        'knn': {
            'prediccion': CLASSES[knn_pred],
            'probabilidad': round(float(max(knn_proba)), 4)
        },
        'mlp': {
            'prediccion': CLASSES[mlp_pred],
            'probabilidad': round(float(max(mlp_proba)), 4)
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
