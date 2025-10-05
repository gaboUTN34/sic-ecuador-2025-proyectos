"""
Módulo: Adquisición de Datos
-----------------------------
Encargado de cargar y realizar una exploración inicial del dataset de  calidad del aire (PM2.5 y otros contaminantes)
"""

import os 
import pandas as pd
import warnings

warnings.filterwarnings('ignore')  # Ignorar advertencias para una salida más limpia

def list_data_files(path: str) -> list[str]:
    """
    Lista todos los archivos CSV en el directorio especificado.
    
    Params:
    path (str): Ruta al directorio que contiene los archivos de datos.
    
    Return:
    list: Lista de nombres de archivos CSV.
    """
    list_files = []  # Lista para almacenar los nombres de los archivos
    for dirname, _, filenames in os.walk(path): # os.walk itera sobre todos los directorios y archivos en la ruta dada
        for filename in filenames:  # Itera sobre cada archivo en el directorio actual
            if filename.endswith(".csv"):  # Verifica si el archivo es un CSV
                list_files.append(os.path.join(dirname, filename)) # Agrega la ruta completa del archivo a la lista
    return list_files

def load_data_csv(file_path: str) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame de pandas.
    
    Params:
    file_path (str): Ruta al archivo CSV.

    Return:
    pd.DataFrame: DataFrame que contiene los datos del archivo CSV.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Archivo '{file_path}' cargado exitosamente.")
        return df
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{file_path}' no fue encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print(f"❌ Error: El archivo '{file_path}' está vacío.")
        return None
    except Exception as e:
        print(f"❌ Error al cargar el archivo '{file_path}': {e}")
        return None


def preview_data(df: pd.DataFrame, num_rows: int = 5) -> None:
    """ Muestra iformación básica del DataFrame (estructura, columnas, tipos de datos, valores nulos)"""
    
    if df.empty:
        print("❌ El DataFrame está vacío.")
        return
    