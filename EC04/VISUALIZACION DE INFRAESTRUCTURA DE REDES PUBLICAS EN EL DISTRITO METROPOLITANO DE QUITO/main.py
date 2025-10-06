import os
import pandas as pd
from estadisticas.basic_stats import (
    load_wifi_data,
    compute_basic_metrics,
    count_points_by_sector,
    count_points_by_parroquia,
    calcular_centroide_por_parroquia
)

# -----------------------------
# Rutas de archivos
# -----------------------------
RUTA_BASE = os.path.dirname(os.path.abspath(__file__))

RUTA_DATOS_PROCESADOS = os.path.join(
    RUTA_BASE, "manejo_de_datos", "zonas_puntos_wifi_procesados.csv"
)

RUTA_SALIDA_ANALISIS = os.path.join(
    RUTA_BASE, "resultados", "estadisticas_basicas.csv"
)

RUTA_SALIDA_CENTROIDES = os.path.join(
    RUTA_BASE, "resultados", "centroides_parroquias.csv"
)


# -----------------------------
# Funciones auxiliares
# -----------------------------
def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta)
        print("✅ Datos procesados cargados correctamente.\n")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {ruta}.")
        return None


def guardar_estadisticas(df_estadisticas, resumen, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    try:
        df_estadisticas.to_csv(ruta_salida, index=False)
        print(f"📁 Archivo guardado: {ruta_salida}\n")
        print("📊 Resumen general:")
        for k, v in resumen.items():
            print(f"- {k}: {v}")
    except Exception as e:
        print(f"❌ Error al guardar resultados: {e}")


# -----------------------------
# Función principal
# -----------------------------
def main():
    print("🔍 Cargando datos WiFi...")

    df = cargar_datos(RUTA_DATOS_PROCESADOS)
    if df is None:
        return

    try:
        # Usa la función que renombra columnas automáticamente
        gdf_wifi = load_wifi_data(df)

        print("\n📊 MÉTRICAS BÁSICAS")
        metrics = compute_basic_metrics(gdf_wifi)
        for key, value in metrics.items():
            print(f"{key}: {value}")

        print("\n📍 CONTEO POR SECTOR")
        df_sector = count_points_by_sector(gdf_wifi)
        print(df_sector)

        print("\n📍 CONTEO POR PARROQUIA")
        df_parroquia = count_points_by_parroquia(gdf_wifi)
        print(df_parroquia)

        print("\n📍 CENTROIDES POR PARROQUIA")
        df_centroides = calcular_centroide_por_parroquia(gdf_wifi)
        print(df_centroides)

        resumen = {
            "total_puntos_wifi": metrics["total_puntos"],
            "promedio_por_zona": metrics["promedio_por_sector"],
            "promedio_por_parroquia": metrics["promedio_por_parroquia"],
            "sectores_unicos": metrics["sectores_unicos"],
            "parroquias_unicas": metrics["parroquias_unicas"]
        }

        guardar_estadisticas(df_parroquia, resumen, RUTA_SALIDA_ANALISIS)
        guardar_estadisticas(df_centroides, resumen, RUTA_SALIDA_CENTROIDES)

    except Exception as e:
        print(f"❌ Error en la ejecución: {e}")


# -----------------------------
# Entrada del script
# -----------------------------
if __name__ == "__main__":
    main()
