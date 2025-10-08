# 🚀 API de Predicción (Breast Cancer) con Flask + Docker

Implementación de una **API REST** que expone un modelo de **clasificación** entrenado con el dataset **Breast Cancer** de scikit-learn.  
⚠️ Este modelo **espera exactamente 30 features numéricas** en un orden específico (ver lista).

---

## 🗂️ Estructura del proyecto

ml_modular/
├── app.py              # API Flask  
├── model_train.py      # Entrenamiento y guardado del modelo  
├── modelo.pkl          # Modelo serializado (joblib) + metadatos  
├── requirements.txt    # Dependencias  
├── test_api.py         # Script de prueba local  
├── Dockerfile          # Construcción de imagen Docker  
└── README.md           # Este documento  

---

## 🧪 Dataset y orden de features (30)

Orden **exacto** que debes enviar en `features` para `POST /predict`:

1. mean radius  
2. mean texture  
3. mean perimeter  
4. mean area  
5. mean smoothness  
6. mean compactness  
7. mean concavity  
8. mean concave points  
9. mean symmetry  
10. mean fractal dimension  
11. radius error  
12. texture error  
13. perimeter error  
14. area error  
15. smoothness error  
16. compactness error  
17. concavity error  
18. concave points error  
19. symmetry error  
20. fractal dimension error  
21. worst radius  
22. worst texture  
23. worst perimeter  
24. worst area  
25. worst smoothness  
26. worst compactness  
27. worst concavity  
28. worst concave points  
29. worst symmetry  
30. worst fractal dimension  

---

## 🔧 Requisitos

- Python 3.8+  
- (Opcional) virtualenv  
- Docker (para la sección de contenedores)

requirements.txt:

flask  
scikit-learn  
joblib  
numpy  
requests  

---

## 🏗️ Entrenamiento del modelo

`model_train.py`:
- Carga `load_breast_cancer()`  
- Entrena `RandomForestClassifier`  
- Calcula exactitud en validación  
- Serializa modelo y metadatos a `modelo.pkl`

Ejecutar:

python model_train.py  

Salida esperada (ejemplo):

Accuracy de validación: 0.98  
Modelo guardado en modelo.pkl  

---

## ▶️ Ejecutar la API (local)

(Opcional) crear entorno virtual:

python -m venv .venv  
source .venv/bin/activate  

Instalar dependencias:

pip install -r requirements.txt  

Iniciar API:

python app.py  

La API quedará disponible en:  
http://127.0.0.1:5000/

---

## 📡 Endpoints

GET /  
Salud del servicio + pista de features:

{
  "status": "ok",
  "message": "API de predicción Breast Cancer lista",
  "features_expected": "30 valores numéricos"
}

POST /predict  
Body (JSON): {"features": [ ... 30 floats ... ]} en el orden indicado arriba.

Respuesta (ejemplo):

{
  "prediction": 1,
  "label": "malignant",
  "proba": [0.08, 0.92]
}

---

## 🧪 Ejemplo de prueba (30 features)

Importante: los valores son solo de ejemplo y respetan el orden del dataset.

curl -s -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[
    14.5,13.8,92.1,655.0,0.095,0.120,0.100,0.075,0.190,0.060,
    0.450,1.050,3.200,45.0,0.0080,0.0300,0.0350,0.0120,0.0220,0.0035,
    16.3,23.1,110.2,820.0,0.125,0.450,0.520,0.200,0.280,0.085
  ]}'

test_api.py (local):

import requests

url = "http://127.0.0.1:5000/predict"  
sample = {
  "features": [
    14.5,13.8,92.1,655.0,0.095,0.120,0.100,0.075,0.190,0.060,
    0.450,1.050,3.200,45.0,0.0080,0.0300,0.0350,0.0120,0.0220,0.0035,
    16.3,23.1,110.2,820.0,0.125,0.450,0.520,0.200,0.280,0.085
  ]
}
print(requests.post(url, json=sample).json())

---

## 🐳 Docker

Dockerfile:

FROM python:3.12-slim  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . /app  
EXPOSE 5000  
CMD ["python", "app.py"]

Construir imagen:

docker build -t api-ml .  

Ejecutar contenedor (mapeando puerto 5001 → 5000):

docker run -d --name api-ml-c1 -p 5001:5000 api-ml  

Ver estado:

docker ps  

Probar:

curl -s http://127.0.0.1:5001/  
curl -s -X POST http://127.0.0.1:5001/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[
    14.5,13.8,92.1,655.0,0.095,0.120,0.100,0.075,0.190,0.060,
    0.450,1.050,3.200,45.0,0.0080,0.0300,0.0350,0.0120,0.0220,0.0035,
    16.3,23.1,110.2,820.0,0.125,0.450,0.520,0.200,0.280,0.085
  ]}'

Parar y eliminar contenedor:

docker stop api-ml-c1 && docker rm api-ml-c1  

---

## 🧰 Manejo de errores (API)

Caso | Código | Ejemplo de mensaje  
------|--------|--------------------  
Falta la clave `features` | 400 | {"error":"Falta la clave 'features' en el JSON."}  
`features` no es lista | 400 | {"error":"La clave 'features' debe ser una lista."}  
Cantidad != 30 | 400 | {"error":"Se esperan 30 valores en 'features' (Breast Cancer)."}  
Valores no numéricos | 400 | {"error":"Todos los valores de 'features' deben ser numéricos."}  
Error interno inesperado | 500 | {"error":"Error interno: <detalle>"}  

---

## ✅ Checklist de la rúbrica

- [x] Proyecto con estructura clara  
- [x] Entrenamiento reproducible (`model_train.py`)  
- [x] Serialización del modelo (`modelo.pkl`)  
- [x] API REST con Flask (`app.py`) y validaciones  
- [x] Pruebas locales (`test_api.py` y `curl`)  
- [x] Dockerfile funcional y documentado  
- [x] README con orden de 30 features y ejemplos  
- [x] Manejo de errores y códigos HTTP  

---

## ✨ Autor

**Felipe Valenzuela P.**  
Bootcamp Machine Learning – Kibernum  
Módulo 10 | Clase 4 – Evaluación modular
