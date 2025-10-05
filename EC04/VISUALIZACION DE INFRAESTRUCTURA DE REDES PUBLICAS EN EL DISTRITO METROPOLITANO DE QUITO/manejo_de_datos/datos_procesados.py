import pandas as pd
import os

RUTA_ENTRADA = os.path.join(os.path.dirname(__file__), 'zonas_puntos_wifi.csv')
RUTA_SALIDA_DATOS_PROCESADOS = os.path.join(os.path.dirname(__file__), 'zonas_puntos_wifi_procesados.csv')

def cargar_datos_no_procesdos(ruta):
    """
    Esta función carga el CSV sin procesar
    en un DataFrame de Pandas.
    """
    try:
        df = pd.read_csv(ruta)
        print("Se a cargado el registro para es procesamiento de los datos.\n")
        return df
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta}. Asegúrese de ejecutar extraccion_datos.py primero.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None