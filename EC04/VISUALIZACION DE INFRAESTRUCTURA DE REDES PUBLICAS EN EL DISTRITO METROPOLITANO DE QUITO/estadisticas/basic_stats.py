import pandas as pd
import os

RUTA_DATOS_PROCESADOS = r"C:\Users\USER-ASUS\Downloads\zonas_puntos_wifi_procesados.csv"
RUTA_SALIDA_ANALISIS = os.path.join(os.path.dirname(
    __file__), '..', 'resultados', 'estadisticas_basicas.csv')


def cargar_datos_procesados(ruta):
    """Carga los datos procesados."""
    try:
        df = pd.read_csv(ruta)
        print("Datos procesados cargados correctamente.\n")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}.")
        return None


def generar_estadisticas(df):
    """Genera métricas básicas y conteos por sector/parroquia."""
    print("Calculando estadísticas básicas...\n")

    total_puntos = len(df)
    puntos_por_zona = df['administracion_zonal'].value_counts().reset_index()
    puntos_por_zona.columns = ['administracion_zonal', 'cantidad_puntos']

    promedio_por_zona = puntos_por_zona['cantidad_puntos'].mean()

    # Detectar zonas sin cobertura (si hay lista de zonas conocidas)
    zonas_sin_cobertura = puntos_por_zona[puntos_por_zona['cantidad_puntos'] == 0]

    resumen = {
        'total_puntos_wifi': total_puntos,
        'promedio_por_zona': promedio_por_zona,
        'zonas_sin_cobertura': zonas_sin_cobertura.shape[0]
    }

    print("Estadísticas generales calculadas.\n")
    return puntos_por_zona, resumen


def guardar_estadisticas(puntos_por_zona, resumen, ruta_salida):
    """Guarda los resultados en un CSV."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    try:
        puntos_por_zona.to_csv(ruta_salida, index=False)
        print(f"Archivo guardado con métricas por zona en: {ruta_salida}\n")

        print("Resumen general:")
        for k, v in resumen.items():
            print(f"- {k}: {v}")

    except Exception as e:
        print(f"Error al guardar resultados: {e}")


if __name__ == "__main__":
    df = cargar_datos_procesados(RUTA_DATOS_PROCESADOS)
    if df is not None:
        puntos_por_zona, resumen = generar_estadisticas(df)
        guardar_estadisticas(puntos_por_zona, resumen, RUTA_SALIDA_ANALISIS)
