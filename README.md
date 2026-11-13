# Predicción de Precios de Viviendas en California (Práctica 3)

**Autores:** Javier Adrian Bejan y Alex Pascual Perez  
**Asignatura:** Inteligencia Artificial - 2º DAM Diurno  

Aplicación web desarrollada en **Streamlit** conectada a una API REST en **FastAPI** que estima el precio medio de las viviendas en California mediante un modelo de Machine Learning.

## Enlaces desplegados (Render)
* **Aplicación Web (Streamlit):** https://interfaz-california.onrender.com
* **Servicio API (FastAPI):** https://prediccion-california.onrender.com
* **Documentación interactiva (Swagger):** https://prediccion-california.onrender.com/docs

---

## Documentación de la API

### Endpoint de predicción
* **Método:** `POST`
* **Ruta:** `/predict`
* **Content-Type:** `application/json`

### Variables de entrada (JSON)
El cuerpo de la petición debe incluir las siguientes 8 variables numéricas:

| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| `MedInc` | `float` | Ingreso medio de la zona (en decenas de miles de dólares) |
| `HouseAge` | `float` | Antigüedad media de las viviendas (años) |
| `AveRooms` | `float` | Número medio de habitaciones por vivienda |
| `AveBedrms` | `float` | Número medio de dormitorios por vivienda |
| `Population` | `float` | Población total del bloque |
| `AveOccup` | `float` | Ocupación media por vivienda |
| `Latitude` | `float` | Latitud geográfica |
| `Longitude` | `float` | Longitud geográfica |

### Ejemplo de petición (`POST /predict`)
```json
{
  "MedInc": 3.5,
  "HouseAge": 29.0,
  "AveRooms": 5.2,
  "AveBedrms": 1.05,
  "Population": 1166.0,
  "AveOccup": 2.8,
  "Latitude": 34.26,
  "Longitude": -118.49
}
