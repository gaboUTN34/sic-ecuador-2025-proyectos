# Este script es para ejecutar el dashboard y presentar los datos obtenidos anteriormente.
# Se ejecuta mediante el módulo dash y el módulo flask (en pruebas).

# TODO 1: implementar el dashboard en el proyecto como tal.
# TODO 2: intentar que el dashboard sea interactivo.
# TODO 3: presentar los datos de forma ordenada y legible.
# TODO 4: completar las funciones declaradas para integrarlas con los demás módulos del equipo.

# Módulos principales de este script.
import dash
from dash import html, dcc
import subprocess, sys, os

# TODO: ejecutar los módulos del equipo
def ejecutar_extraccion_datos():
    try:
        # Obtener la ruta del script
        ruta_extraccion = os.path.join('manejo_de_datos', 'extraccion_datos.py')

        # Ejecutar el script
        resultado = subprocess.run([sys.executable, ruta_extraccion],
                                   capture_output=True, text=True, check=True)

        if resultado.stdout:
            print(resultado.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error en extracción de datos: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")

# Ejecutar la extracción al iniciar el dashboard
print("Iniciando extracción de datos...")
ejecutar_extraccion_datos()

# Inicializar la app Dash
app = dash.Dash(__name__)

# Diseño del dashboard
app.layout = html.Div([
    html.H1("Dashboard del proyecto - Puntos WiFi del Distrito Metropolitano de Quito", style={'textAlign': 'center'}),

    # Sección: Gráficos estadísticos
    html.Div([
        html.H2("Estadísticas de cobertura en la ciudad"),
        html.Label("\nFiltrar por sector"),
        dcc.Dropdown(
            id="sector",
            options=[{'label':'Todos', 'value':'all'}],
            value = 'all'
        ),
        html.Iframe(
            src="https://www.example.net"
        ),
    ], style={'width': '80%', 'margin': '20px auto'}),

    # Sección: Mapa interactivo
    html.Div([
        html.H2("Mapa de los puntos WiFi existentes"),
        html.Label("\nFiltrar por parroquia"),
        dcc.Dropdown(
            id="parroquia",
            options=[{'label':'Todos', 'value':'all'}],
            value = 'all'
        ),
        html.Iframe(
            src="https://www.example.com"
        )
    ], style={'width': '80%', 'margin': '20px auto'}),

    # Sección: Posibles zonas prioritarias
    html.Div([
        html.H2("Posibles zonas prioritarias"),
        html.Label("\nFiltrar por punto más cercano"),
        dcc.Dropdown(
            id="cercania",
            options=[{'label':'Todos', 'value':'all'}],
            value = 'all'
        ),
        html.Iframe(
            src="https://www.example.com"
        )
    ], style={'width': '80%', 'margin': '20px auto'}),
])

# TODO: al finalizar el código cambiar la condición a False.
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)