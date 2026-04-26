from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    #Validación básica
    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        # 📥 Datos numéricos
        edad = int(data['edad'])
        cgpa = float(data['cgpa'])
        sueno = float(data['sueno'])
        estudio = float(data['estudio'])
        redes = float(data['redes'])
        actividad = float(data['actividad'])
        estres = float(data['estres']) / 10

        # 🔤 Categóricos
        genero = data['genero']          # Male / Female
        departamento = data['departamento']  # Engineering, etc.

        # 🔧 Preprocesamiento categórico (simple)
        genero_bin = 1 if genero == "Female" else 0

        # Departamento (one-hot manual básico)
        dept_engineering = 1 if departamento == "Engineering" else 0
        dept_science = 1 if departamento == "Science" else 0
        dept_arts = 1 if departamento == "Arts" else 0
        dept_business = 1 if departamento == "Business" else 0

        # Lógica temporal (simulando modelo)
        depresion = False

        if estres > 0.7 and sueno < 6:
            depresion = True

        if actividad < 2 and estres > 0.6:
            depresion = True

        if redes > 5 and estres > 0.5:
            depresion = True

        if cgpa < 2.5 and estres > 0.6:
            depresion = True

        return jsonify({
            "prediccion": depresion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)