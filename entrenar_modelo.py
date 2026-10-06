# Alex Pascual Perez y Javier Adrian Bejan - P1

import sys
import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ej5"))
from datos_california import cargar_dataframe, dividir_datos


def main():
    df = cargar_dataframe()
    X_train, X_test, y_train, y_test = dividir_datos(df)

    modelo = RandomForestRegressor(n_estimators=200, max_depth=12, random_state=42, n_jobs=-1)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"MAE (error absoluto medio) en el conjunto de prueba: {mae:.2f} $")

    ruta_modelo = "modelo_california.pkl"
    joblib.dump(modelo, ruta_modelo)
    print(f"Modelo guardado en '{ruta_modelo}'")

    with open("mae_resultado.txt", "w") as f:
        f.write(f"MAE (error absoluto medio) en el conjunto de prueba: {mae:.2f} $\n")


if __name__ == "__main__":
    main()
