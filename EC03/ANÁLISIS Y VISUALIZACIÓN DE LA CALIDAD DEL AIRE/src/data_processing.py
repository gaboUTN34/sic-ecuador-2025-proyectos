"""
H-1
"""
import pandas as pd
import numpy as np
import re

CONTAMINANTES = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']

def quality_report(df_idx: pd.DataFrame) -> dict:
    # Garantizar que el índice sea datetime
    idx = df_idx.index
    if not isinstance(idx, pd.DatetimeIndex):
        # Si hay columna 'date' (o similar), úsala; si no, intenta convertir el index
        date_like_cols = [c for c in df_idx.columns if re.search(r'date|time|fecha|datetime|timestamp', str(c), re.I)]
        if date_like_cols:
            tcol = date_like_cols[0]
            dt = pd.to_datetime(df_idx[tcol], errors="coerce")
            idx = dt
        else:
            try:
                idx = pd.to_datetime(idx, errors="raise")
            except Exception:
                idx = None

    # Normalizar tz y ordenar para inferir frecuencia
    freq = None
    if isinstance(idx, pd.DatetimeIndex):
        if getattr(idx, "tz", None) is not None:
            idx = idx.tz_localize(None)  # quitar tz si existe
        idx = idx.sort_values()
        try:
            freq = pd.infer_freq(idx)
        except Exception:
            freq = None

    return {
        "rows": int(df_idx.shape[0]),
        "cols": int(df_idx.shape[1]),
        "duplicates": int(df_idx.index.duplicated().sum()),
        "inferred_freq": (freq or 'None'),
        "missing": {c: int(df_idx[c].isna().sum()) for c in df_idx.columns},
    }



def quality_report(df_idx: pd.DataFrame) -> dict:
    idx = df_idx.index
    try: freq = pd.infer_freq(idx)
    except Exception: freq = None
    return {
        "rows": int(df_idx.shape[0]),
        "cols": int(df_idx.shape[1]),
        "duplicates": int(idx.duplicated().sum()),
        "inferred_freq": str(freq),
        "missing": {c: int(df_idx[c].isna().sum()) for c in df_idx.columns}
    }

def resample_agg(df_idx: pd.DataFrame, rule="D", agg="median", cols=CONTAMINANTES) -> pd.DataFrame:
    cols = [c for c in cols if c in df_idx.columns]
    if not cols: return pd.DataFrame(index=df_idx.index)
    return getattr(df_idx[cols].resample(rule), agg)()

def descriptives(df_idx: pd.DataFrame, cols=CONTAMINANTES) -> pd.DataFrame:
    cols = [c for c in cols if c in df_idx.columns]
    if not cols: return pd.DataFrame()
    d = df_idx[cols].describe(percentiles=[.05,.5,.95]).T
    d = d.rename(columns={"50%":"p50","5%":"p05","95%":"p95"})
    return d[["count","mean","std","min","p05","p50","p95","max"]]

""" sin testear
def fill_gaps(df_idx: pd.DataFrame, method="none"):
    if method == "none": return df_idx
    if method == "ffill": return df_idx.fillna(method="ffill")
    if method == "linear": return df_idx.interpolate(limit_direction="both")
    raise ValueError("method inválido")
    """

