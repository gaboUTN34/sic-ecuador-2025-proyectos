"""
Módulo: Adquisición de Datos
-----------------------------
Encargado de cargar y realizar una exploración inicial del dataset de  calidad del aire (PM2.5 y otros contaminantes)
"""

import os 
import pandas as pd
import warnings

warnings.filterwarnings('ignore')  # Ignorar advertencias para una salida más limpia

def list_data_files(path):
    """
    Lista todos los archivos CSV en el directorio de datos.
    
    Parámetros:
    path (str): Ruta al directorio que contiene los archivos de datos.
    
    Retorna:
    list: Lista de nombres de archivos CSV.
    """
    print("="*60)
    print("📂 Archivos disponibles en la carpeta")
    print("="*60)
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            print(os.path.join(dirname, filename))


