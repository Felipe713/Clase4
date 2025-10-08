FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto (incluye app.py, model_train.py y modelo.pkl si ya existe)
COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
