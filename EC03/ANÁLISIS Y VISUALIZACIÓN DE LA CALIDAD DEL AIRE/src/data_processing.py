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