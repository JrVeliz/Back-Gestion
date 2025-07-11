import pandas as pd
import joblib

modelo = joblib.load("modelo_maquinaria.pkl")
label_encoders = joblib.load("codificadores.pkl")

def predecir(datos_dict):
    nuevo_df = pd.DataFrame([datos_dict])

    for col in nuevo_df.select_dtypes(include='object').columns:
        if col in label_encoders:
            nuevo_df[col] = label_encoders[col].transform(nuevo_df[col])
        else:
            return {"error": f"Columna {col} no reconocida o no entrenada."}

    pred = modelo.predict(nuevo_df)[0]
    prob = modelo.predict_proba(nuevo_df)[0]
    clases = modelo.classes_

    falla = label_encoders['falla_reportada'].inverse_transform([pred])[0]
    top_3 = sorted(zip(clases, prob), key=lambda x: -x[1])[:3]
    top_3 = [
        {
            "falla": label_encoders['falla_reportada'].inverse_transform([clase])[0],
            "probabilidad": round(p * 100, 2)
        }
        for clase, p in top_3
    ]

    return {
        "falla_predicha": falla,
        "top_3_probabilidades": top_3
    }
