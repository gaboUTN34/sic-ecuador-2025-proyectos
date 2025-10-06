import pandas as pd
import os
import numpy as np

RUTA_BASE = os.path.dirname(os.path.dirname(__file__))
RUTA_DATOS_PROCESADOS = os.path.join(
    RUTA_BASE, 'manejo_de_datos', 'zonas_puntos_wifi_procesados.csv')
RUTA_SALIDA_COBERTURA = os.path.join(os.path.dirname(
    __file__), 'resultados', 'cobertura_prioritaria.csv')


def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta)
        print("Datos procesados cargados para análisis de cobertura.\n")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return None


def calcular_densidad(df):
    """
    Calcula densidad aproximada de puntos WiFi por parroquia.

    """
    print("Calculando densidad aproximada de cobertura...\n")

    densidad = df.groupby('parroquia').agg(
        total_puntos=('nombre', 'count'),
        lat_min=('latitud', 'min'),
        lat_max=('latitud', 'max'),
        lon_min=('longitud', 'min'),
        lon_max=('longitud', 'max')
    ).reset_index()

    densidad['area_aprox'] = (densidad['lat_max'] - densidad['lat_min']) * \
        (densidad['lon_max'] - densidad['lon_min'])
    densidad['densidad_puntos'] = densidad['total_puntos'] / \
        densidad['area_aprox'].replace(0, np.nan)

    zonas_prioritarias = densidad.nsmallest(5, 'densidad_puntos')[
        ['parroquia', 'densidad_puntos']]
    print("Zonas prioritarias detectadas:\n", zonas_prioritarias)
    return densidad, zonas_prioritarias


def guardar_resultados(densidad, zonas_prioritarias, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    try:
        densidad.to_csv(ruta_salida, index=False)
        print(f"Resultados de cobertura guardados en: {ruta_salida}\n")
        print("Zonas prioritarias exportadas correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo de cobertura: {e}")


if __name__ == "__main__":
    df = cargar_datos(RUTA_DATOS_PROCESADOS)
    if df is not None:
        densidad, zonas_prioritarias = calcular_densidad(df)
        guardar_resultados(densidad, zonas_prioritarias, RUTA_SALIDA_COBERTURA)
