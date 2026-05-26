# Proyecto-CD-2026-1

Aplicación web para realizar predicciones sobre la depresión en estudiantes universitarios, utilizando modelos de aprendizaje supervisado entrenados con el dataset *Student Lifestyle 100k*.

**Integrantes:**

* Santiago Cardona
* María José Vargas

\---

## Descripción

La aplicación recibe información académica y de hábitos de vida de un estudiante a través de un formulario web y retorna la predicción de dos modelos distintos:

* **MLP (Multilayer Perceptron):** Red neuronal entrenada con los datos originales.
* **KNN (K-Nearest Neighbors):** Modelo de vecinos más cercanos entrenado con los datos balanceados mediante SMOTE.

Cada modelo devuelve si el estudiante presenta o no indicios de depresión, junto con la probabilidad asociada.

\---

## Estructura del repositorio

```
ProyectoFinal/
├── modelo\_original/        # MLP y KNN sin balanceo
│   ├── app.py
│   ├── index.html
│   ├── resultado.html
│   ├── script.js
│   ├── style.css
│   └── modelo\_original.ipynb
│
├── modelo\_smote/           # MLP y KNN con balanceo SMOTE
│   ├── app.py
│   ├── index.html
│   ├── resultado.html
│   ├── script.js
│   ├── style.css
│   └── modelo\_smote.ipynb

│

├── student\_lifestyle\_100k.csv 

│
└── README.md
```

\---

## Requisitos

* Python 3.10+
* Las siguientes librerías (instalables con pip):

```
flask
flask-cors
scikit-learn
imbalanced-learn
pandas
numpy
joblib
```

Instalar con:

```bash
pip install flask flask-cors scikit-learn imbalanced-learn pandas numpy joblib
```

\---

## Cómo generar los modelos

Los archivos `.pkl` no están incluidos en el repositorio por su tamaño. Para generarlos:

1. Abrir el notebook correspondiente en Google Colab:

   * `modelo\_original.ipynb` para el modelo sin balanceo
   * `modelo\_smote.ipynb` para el modelo con SMOTE
2. Subir el archivo `student\_lifestyle\_100k.csv` a Colab cuando se solicite.
3. Ejecutar todas las celdas.
4. Descargar los `.pkl` generados y colocarlos en la carpeta correspondiente:

|Archivo|Carpeta|
|-|-|
|`knn\_modelo.pkl`, `knn\_scaler.pkl`, `mlp\_modelo.pkl`, `mlp\_scaler.pkl`|`modelo\_original/`|
|`modelo\_smote\_knn.pkl`, `scaler\_smote\_knn.pkl`, `modelo\_smote\_mlp.pkl`, `scaler\_smote\_mlp.pkl`|`modelo\_smote/`|

\---

## Cómo correr la aplicación

1. Abrir una terminal y entrar a la carpeta del modelo que se quiere usar:

```bash
cd ProyectoFinal/modelo\_original
# o
cd ProyectoFinal/modelo\_smote
```

2. Correr Flask:

```bash
flask run
```

3. Abrir `index.html` en el navegador, diligenciar el formulario y hacer clic en **Predecir**.

\---

