# Despliegue de Modelo de IA - Precios de Viviendas en California

Autores: Alex Pascual y Javier Adrián Beján  
Asignatura: Inteligencia Artificial y computación en la nube (2º DAM)  

## Pasos del Despliegue

1. **Creación de cuenta:** Registro y configuración de una cuenta gratuita en la plataforma de despliegue en la nube **Render**.
2. **Configuración del repositorio:** Subida del código fuente de la aplicación (`app.py`, el modelo entrenado `modelo_california.pkl` y el archivo de dependencias `requirements.txt`) a un repositorio público en **GitHub**.
3. **Configuración del servicio web:** Conexión del repositorio de GitHub con Render indicando el entorno de Python.
4. **Comando de despliegue (Start Command):**  
   `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. **URL final del servicio:** [https://prediccion-california.onrender.com](https://prediccion-california.onrender.com)
