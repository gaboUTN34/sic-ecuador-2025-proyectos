# Este script es para ejecutar el dashboard y presentar los datos obtenidos anteriormente.
# Se ejecuta mediante el módulo dash y el módulo flask (en pruebas).

# TODO 1: implementar el dashboard en el proyecto como tal.
# TODO 2: intentar que el dashboard sea interactivo.
# TODO 3: presentar los datos de forma ordenada y legible.
# TODO 4: completar las funciones declaradas para integrarlas con los demás módulos del equipo.

# Módulos principales de este script.
import dash
from dash import html

# TODO: Módulos realizados por el equipo, para la presentación de los datos (completar).


# TODO: Cargar y procesar datos

# Inicializar la app Dash
app = dash.Dash(__name__)

# Diseño del dashboard
app.layout = html.Div([
    html.H1("Dashboard del proyecto - Puntos WiFi del Distrito Metropolitano de Quito", style={'textAlign': 'center'}),

    # Sección: Gráficos estadísticos
    html.Div([
        html.H2("Estadísticas de cobertura en la ciudad"),
        html.Iframe(

        )
    ]),

    # Sección: Mapa interactivo
    html.Div([
        html.H2("Mapa de los puntos WiFi existentes"),
        html.Iframe(

        )
    ]),

    # Sección: Posibles zonas prioritarias
    html.Div([
        html.H2("Posibles zonas prioritarias"),
        html.Iframe(

        )
    ]),
])

# TODO: al finalizar el código cambiar la condición a False.
if __name__ == '__main__':
    app.run(debug=True)