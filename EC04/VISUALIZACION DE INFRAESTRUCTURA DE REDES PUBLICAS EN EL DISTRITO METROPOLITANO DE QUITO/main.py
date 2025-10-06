import os
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
    RUTA_BASE, "zonas_puntos_wifi.csv"
)


RUTA_SALIDA_ANALISIS = os.path.join(
    RUTA_BASE, "resultados", "estadisticas_basicas.csv"
)

# -----------------------------
# Función principal
# -----------------------------


def main():
    try:
        print(" Cargando datos WiFi...")

        gdf_wifi = load_wifi_data(RUTA_DATOS_PROCESADOS)
        print(
            f" Datos cargados correctamente. Total de registros: {len(gdf_wifi)}\n")

        print(" MÉTRICAS BÁSICAS")
        metrics = compute_basic_metrics(gdf_wifi)
        for key, value in metrics.items():
            print(f"- {key}: {value}")

        print("\n CONTEO POR SECTOR")
        df_sector = count_points_by_sector(gdf_wifi)
        print(df_sector)

        print("\n CONTEO POR PARROQUIA")
        df_parroquia = count_points_by_parroquia(gdf_wifi)
        print(df_parroquia)

        print("\n CENTROIDES POR PARROQUIA")
        df_centroides = calcular_centroide_por_parroquia(gdf_wifi)
        print(df_centroides)

        os.makedirs(os.path.dirname(RUTA_SALIDA_ANALISIS), exist_ok=True)
        df_parroquia.to_csv(RUTA_SALIDA_ANALISIS, index=False)
        print(f"\n Archivo guardado con métricas en: {RUTA_SALIDA_ANALISIS}")

    except Exception as e:
        print(f" Error en la ejecución: {e}")


# -----------------------------
# Entrada del script
# -----------------------------
if __name__ == "__main__":
    main()
