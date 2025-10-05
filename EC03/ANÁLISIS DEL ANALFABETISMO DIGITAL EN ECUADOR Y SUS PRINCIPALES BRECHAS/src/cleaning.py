import pandas as pd
import re
import unicodedata
import os

# Funciones
def limpiar_texto(s):
    if s is None or (isinstance(s, float) and pd.isna(s)):
        return ""
    s = str(s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.replace("ñ", "ni").replace("Ñ", "Ni")
    s = re.sub(r'[¿?*":/]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def limpiar_df_texto(df):
    for c in df.select_dtypes(include='object'):
        df[c] = df[c].map(limpiar_texto)
    return df

# Crear directorios si no existen
os.makedirs('../data/processed', exist_ok=True)

# Cargar el archivo CSV original
df = pd.read_csv('../data/raw/2023.csv')

# Convertir todas las columnas a tipo string para un manejo uniforme
for column in df.columns:
    df[column] = df[column].astype(str)

# Limpiar las cabeceras
df.columns = [limpiar_texto(c) for c in df.columns]

# Limpiar el contenido textual
df = limpiar_df_texto(df)

# Estandarizar cabeceras
for c in df.columns:
    if "actividad economica" in c and "CIIU" in c:
        df = df.rename(columns={c: "CIIU"})
        break
for col in ["Provincia", "Genero", "Edad", "Puntuacion", "ID del envio"]:
    if col in df.columns:
        df = df.rename(columns={col: col})

# Selección de columnas deseadas
columnas_deseadas = [
    "ID del envio",
    "Registre su tipo de empresa o organizacion o ciudadano",
    "Provincia",
    "Genero",
    "CIIU",
    "Tiene conocimientos de computacion y navegacion en internet",
    "Utiliza firma electronica, para realizar compras, ventas, firmas de contratos, etc",
    "Conoce las oportunidades que el IOT (Internet de las cosas) puede aportar en su trabajo y empresa",
    "Conoce las oportunidades que el IA (Inteligencia artificial) puede aportar en su trabajo y empresa",
    "Edad",
    "Puntuacion"
]
df = df[[c for c in columnas_deseadas if c in df.columns]]

# Establecer índice
if "ID del envio" in df.columns:
    df = df.set_index("ID del envio")

# Reemplazar todos los NaN con cadena vacía y asegurar tipos consistentes
df = df.fillna("")

# Guardar el archivo procesado
df.to_csv('../data/processed/2023_filtrado_limpio1.csv', index=True)
print("Archivo generado: data/processed/2023_filtrado_limpio1.csv")