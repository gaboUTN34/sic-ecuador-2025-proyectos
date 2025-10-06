"""
Módulo: Adquisición de Datos
Encargado de cargar y realizar una exploración inicial del dataset. Incluye utilidades para listar archivos de datos, cargar
archivos CSV en DataFrames de pandas, verificar la validez de los datos cargados y mostrar información relevante sobre el
contenido y estructura de los DataFrames.
"""

import os 
import pandas as pd
import warnings
import IPython.display as d  # Mostrar DataFrames de manera interactiva en notebooks

warnings.filterwarnings('ignore')  # Ignorar advertencias para una salida más limpia

def verify_dataframe(df: pd.DataFrame) -> bool:
    """ 
    Verifica si el DataFrame está vacío o no fue cargado correctamente.

    Params:
    df (pd.DataFrame): El DataFrame a verificar.
    Return:
    bool: True si el DataFrame es válido, False si está vacío o no fue cargado.
    """
    if df is None or df.empty:
        print("❌ El DataFrame está vacío o no fue cargado correctamente.")
        return False
    return True

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



def preview_data(df: pd.DataFrame, num_rows: int = 5):
    """ Muestra las filas del DataFrame """
    if verify_dataframe(df):
        print(f"\n🔍 Primeras {num_rows} filas del DataFrame:")
        d.display(df.head(num_rows))

def get_dataframe_info(df: pd.DataFrame):
    """ Muestra información general del DataFrame (columnas, tipos de datos)"""
    if verify_dataframe(df):
        print("\n🧱 Columnas del Dataframe:")
        print(list(df.columns))
    
        print("\n📊 Información del DataFrame:")
        df.info()

def get_dataframe_shape(df: pd.DataFrame):
    """ Muestra las dimensiones (número de filas y columnas) del DataFrame """
    if verify_dataframe(df):
        print(f"\n📐 Dimensiones del DataFrame: {df.shape[0]} filas y {df.shape[1]} columnas")

def get_missing_values(df: pd.DataFrame):
    """ Muestra el número de valores faltantes por columna en el DataFrame """
    if verify_dataframe(df):
        print("\n❗ Valores faltantes por columna:")
        missing_values = df.isnull().sum()
        print(missing_values)


