import geopandas as gpd
import pandas as pd


def load_wifi_data(df: pd.DataFrame) -> gpd.GeoDataFrame:
    """
    Convierte un DataFrame con puntos WiFi en un GeoDataFrame.
    Renombra columnas automáticamente si es necesario.
    """

    # Diccionario de posibles nombres → nombre estándar
    columnas_esperadas = {
        "Longitude": "longitud",
        "Longitud": "longitud",
        "LON": "longitud",
        "Latitud": "latitud",
        "Latitude": "latitud",
        "LAT": "latitud",
        "zona": "zona",
        "admin_zone": "zona",
        "Parish": "parroquia",
        "parroquia": "parroquia"
    }

    # Renombrar columnas según coincidencia
    df = df.rename(columns={
                   col: columnas_esperadas[col] for col in df.columns if col in columnas_esperadas})

    # Validar que todas las columnas necesarias estén presentes
    required_columns = {"longitud", "latitud", "zona", "parroquia"}
    if not required_columns.issubset(df.columns):
        # 🔍 Para depurar
        print(f"Columnas disponibles en CSV: {list(df.columns)}")
        raise ValueError(
            f"El CSV debe contener las columnas: {required_columns}")

    # Convertir a GeoDataFrame
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df["longitud"], df["latitud"]),
        crs="EPSG:4326"
    )
    return gdf


def compute_basic_metrics(gdf: gpd.GeoDataFrame) -> dict:
    metrics = {
        "total_puntos": len(gdf),
        "sectores_unicos": gdf["zona"].nunique(),
        "parroquias_unicas": gdf["parroquia"].nunique(),
        "promedio_por_sector": gdf.groupby("zona").size().mean(),
        "promedio_por_parroquia": gdf.groupby("parroquia").size().mean()
    }
    return metrics


def count_points_by_sector(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    return gdf.groupby("zona").size().reset_index(name="total_puntos")


def count_points_by_parroquia(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    return gdf.groupby("parroquia").size().reset_index(name="total_puntos")


def calcular_centroide_por_parroquia(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    centroides = gdf.groupby("parroquia").geometry.apply(
        lambda x: x.unary_union.centroid)
    df_centroides = centroides.reset_index()
    df_centroides["longitud_centroide"] = df_centroides.geometry.x
    df_centroides["latitud_centroide"] = df_centroides.geometry.y
    return df_centroides[["parroquia", "longitud_centroide", "latitud_centroide"]]
