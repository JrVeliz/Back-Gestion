import pandas as pd
import joblib

modelo = joblib.load("modelo_maquinaria.pkl")
label_encoders = joblib.load("codificadores.pkl")

# Columnas usadas
columnas_esperadas = [
    "tipo_maquinaria", "tiempo_uso_horas", "temperatura_motor", "vibracion_general",
    "presion_hidraulica", "nivel_aceite_motor", "nivel_combustible", "rpm_motor",
    "velocidad_avance", "carga_trabajo", "sensor_fugas", "sensor_ruido",
    "codigo_error", "modo_operacion", "tiempo_operacion_sesion",
    "ultima_mantencion_dias", "condiciones_terreno"
]


def predecir(datos_dict):
    datos_limpios = {k: v for k, v in datos_dict.dict().items() if k in columnas_esperadas}

    print("hola 3")
    nuevo_df = pd.DataFrame([datos_limpios])

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
        # Probabilidades completas con etiquetas
    todas_probabilidades = [
        {
            "falla": label_encoders['falla_reportada'].inverse_transform([clase])[0],
            "probabilidad": round(p * 100, 2)
        }
        for clase, p in zip(clases, prob)
    ]

    # Valores transformados usados en la predicción
    entrada_transformada = nuevo_df.to_dict(orient="records")[0]

    # Importancia de cada característica (si aplica)
    try:
        importancias = modelo.feature_importances_
        importancia_variables = dict(zip(nuevo_df.columns, importancias.round(4)))
    except AttributeError:
        importancia_variables = "No disponible para este modelo"


    return {
        "falla_predicha": falla,
        "top_3_probabilidades": top_3,
        "todas_las_probabilidades": todas_probabilidades,
        "entrada_transformada": entrada_transformada,
        "importancia_variables": importancia_variables
    }
