"""
H-1
"""
import pandas as pd
import numpy as np
import re

CONTAMINANTES = ['CO', 'NO','NO2','03','SO2','PM2.5', 'PM10', 'NH3']

def _guess_time_col(df):
    cands = [c for c in df.columns if re.search(r'date|time|fecha|datetime|timestamp', str(c), re.I)]
    for c in cands + list(df.columns):
        try:
            pd.to_datetime(df[c], errors="raise"); return c
        except Exception:
            pass
    return None


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2.columns = [str(c).strip().lower() for c in df2.columns]
    tcol = _guess_time_col(df2)
    if tcol is None: raise ValueError("No se detectó columna temporal.")
    df2[tcol] = pd.to_datetime(df2[tcol], errors="coerce", utc=True)
    df2 = df2.dropna(subset=[tcol]).sort_values(tcol).set_index(tcol)
    for p in CONTAMINANTES:
        if p in df2.columns: df2[p] = pd.to_numeric(df2[p], errors="coerce")
    return df2

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

