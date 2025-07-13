import pandas as pd
import joblib
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from app.config import DATABASE_URL
from datetime import datetime

def entrenar_modelo():
    try:
        print(f"[{datetime.now()}] Iniciando entrenamiento...")

        engine = create_engine(DATABASE_URL)

        df = pd.read_sql("SELECT * FROM casos_entrenamiento", engine)
        df = df.drop(columns=['fecha_creado'], errors='ignore')
        df = df.drop(columns=['id'], errors='ignore')

        print(f"[{datetime.now()}] Datos cargados correctamente. Registros: {len(df)}")

        label_encoders = {}
        for col in df.select_dtypes(include='object').columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

        if "falla_reportada" not in df.columns:
            raise Exception("Columna 'falla_reportada' no encontrada")

        X = df.drop("falla_reportada", axis=1)
        y = df["falla_reportada"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        modelo = RandomForestClassifier(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)

        score = modelo.score(X_test, y_test)
        print(f"[{datetime.now()}] Precisión en test: {score * 100:.2f}%")

        joblib.dump(modelo, "modelo_maquinaria.pkl")
        joblib.dump(label_encoders, "codificadores.pkl")

        print(f"[{datetime.now()}] Modelo entrenado y guardado correctamente.")

    except Exception as e:
        print(f"[{datetime.now()}] ERROR durante entrenamiento: {e}")

if __name__ == "__main__":
    entrenar_modelo()
