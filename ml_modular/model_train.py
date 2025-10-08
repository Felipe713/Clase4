import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar dataset
data = load_breast_cancer()
X, y = data.data, data.target

# Separar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluar
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Precisión del modelo: {acc:.4f}")

# Guardar modelo
joblib.dump(model, "modelo.pkl")
print("💾 Modelo guardado correctamente en modelo.pkl")
