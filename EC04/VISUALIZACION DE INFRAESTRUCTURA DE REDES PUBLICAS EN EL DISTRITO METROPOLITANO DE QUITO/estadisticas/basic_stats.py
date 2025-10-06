import pandas as pd
import geopandas as gpd


def load_wifi_data(path: str) -> gpd.GeoDataFrame:
    """
    Carga un archivo CSV con puntos WiFi y lo convierte en GeoDataFrame.
    Ajusta los nombres de columnas según el CSV original.
    """
    df = pd.read_csv(path)

    df = df.rename(columns={
        "lat": "latitud",
        "lng": "longitud",
        "az": "zona"
    })

    required_columns = {"longitud", "latitud", "zona", "parroquia"}
    if not required_columns.issubset(df.columns):
        raise ValueError(
            f"El CSV debe contener las columnas: {required_columns}")

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df["longitud"], df["latitud"]),
        crs="EPSG:4326"
    )
    return gdf


def count_points_by_sector(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Cuenta el número total de puntos WiFi por sector/zona.
    """
    return gdf.groupby("zona").size().reset_index(name="total_puntos")


def count_points_by_parroquia(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Cuenta el número total de puntos WiFi por parroquia.
    """
    return gdf.groupby("parroquia").size().reset_index(name="total_puntos")


def compute_basic_metrics(gdf: gpd.GeoDataFrame) -> dict:
    """
    Calcula métricas descriptivas básicas.
    """
    metrics = {
        "total_puntos": len(gdf),
        "sectores_unicos": gdf["zona"].nunique(),
        "parroquias_unicas": gdf["parroquia"].nunique(),
        "promedio_por_sector": gdf.groupby("zona").size().mean(),
        "promedio_por_parroquia": gdf.groupby("parroquia").size().mean()
    }
    return metrics


def calcular_centroide_por_parroquia(gdf: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Calcula el centroide (latitud y longitud central) de cada parroquia.
    """
    centroides = gdf.dissolve(by="parroquia").centroid
    df_centroides = pd.DataFrame({
        "parroquia": centroides.index,
        "latitud_centroide": centroides.y,
        "longitud_centroide": centroides.x
    })
    return df_centroides
