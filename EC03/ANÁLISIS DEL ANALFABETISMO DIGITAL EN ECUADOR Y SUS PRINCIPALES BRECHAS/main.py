import pandas as pd
import re
import unicodedata

# ---------- Funciones ----------
def limpiar_texto(s):
    """Limpia texto: quita tildes, cambia ñ→ni, elimina signos y espacios extra."""
    if s is None or (isinstance(s, float) and pd.isna(s)): 
        return ""
    s = str(s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.replace("ñ", "ni").replace("Ñ", "Ni")
    s = re.sub(r'[¿?*":/]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def limpiar_df_texto(df):
    """Limpia todas las celdas de tipo texto en el DataFrame."""
    for c in df.select_dtypes(include='object'):
        df[c] = df[c].map(limpiar_texto)
    return df

# ---------- Cargar y limpiar ----------
df = pd.read_csv("2023.csv")

# Limpia cabeceras y contenido
df.columns = [limpiar_texto(c) for c in df.columns]
df = limpiar_df_texto(df)

# ---------- Estandarizar cabeceras ----------
# Detectar y renombrar CIIU
for c in df.columns:
    if "actividad economica" in c and "CIIU" in c:
        df = df.rename(columns={c: "CIIU"})
        break

# Renombres básicos
for col in ["Provincia", "Genero", "Edad", "Puntuacion", "ID del envio"]:
    if col in df.columns:
        df = df.rename(columns={col: col})

# ---------- Selección de columnas ----------
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
    "Utiliza firma electronica, para generar oficios, servicios, firmas de contratos, etc",
    "Conoce como utilizar herramientas de busqueda avanzada en Internet para mejorar los resultados en funcion de sus necesidades",
    "Identifica parametros que deben cumplir las paginas web y la informacion online para considerar su confiabilidad y calidad",
    "Clasifica la informacion mediante archivos y carpetas para facilitar su localizacion posterior",
    "Conoce o ha utilizado servicios de alojamiento de archivos en la nube",
    "Ha participado en consultas ciudadanas o encuestas a traves de internet (online) a propuestas de organizaciones publicas o sociales",
    "Ha elaborado y/o compartido documentos con otras personas de mi entorno laboral mediante herramientas colaborativas",
    "Conoce y tiene en cuenta los codigos de buena conducta aceptados en Internet",
    "Usted sabe como generar un perfil publico personal o profesional en las Redes Sociales controlando los detalles de la imagen que quiere transmitir",
    "Es capaz de utilizar los diferentes medios digitales para exponer de manera creativa esquemas graficos mapas conceptuales infografias",
    "Sabe editar y modificar con herramientas digitales el formato de diferentes tipos de archivo textos fotografias videos",
    "Usted utiliza algun formato o regla para referenciar y citar trabajos de investigacion",
    "Conoce los fundamentos de los procesos digitales y de la creacion de software. Entiendo los principios de la programacion",
    "Conoce y actua con prudencia cuando recibe mensajes cuyo remitente contenido o archivo adjunto sea desconocido (SPAM)",
    "Se interesa en conocer las politicas de privacidad de las plataformas que utiliza en Internet asi como el tratamiento que hacen de sus datos personales",
    "Se mantiene informado y actualizado sobre habitos saludables y seguros en el uso de la tecnologia y los fomenta y los difunde",
    "Conoce como reciclar la basura electronica",
    "Es capaz de identificar un problema tecnico de los dispositivos digitales y/o aplicaciones y entornos que utiliza",
    "Es capaz de evaluar y elegir de manera adecuada un dispositivo software aplicacion o servicio para realizar sus tareas",
    "Participa en experiencias innovadoras relacionadas con el uso de nuevas tecnologias",
    "Conoce su nivel de competencia digital e identifica claramente sus carencias con respecto a los requisitos de su entorno laboral",
    "Edad",
    "Puntuacion"
]

# Filtrar columnas disponibles
df = df[[c for c in columnas_deseadas if c in df.columns]]

# ---------- Índice y salida ----------
if "ID del envio" in df.columns:
    df = df.set_index("ID del envio")

print(df.head())
df.to_csv("2023_filtrado_limpio1.csv", index=True)
print("Archivo generado: 2023_filtrado_limpio1.csv")