# Este script es para ejecutar el dashboard y presentar los datos obtenidos del módulo visualizacion anteriormente.
# Se ejecuta mediante el módulo dash.

# TODO: implementar el dashboard en el proyecto como tal.
# TODO: completar las funciones declaradas para integrarlas con los demás módulos del equipo.

# Módulos principales de este script.
import dash
from dash import html, dcc

# TODO: Cargar los datos del módulo de visualización para presentarlos.
# TODO: Presentar los datos dentro del dashboard.

# Inicializar la app Dash
app = dash.Dash(__name__)

# Estilos CSS personalizados para que el dashboard se vea bonito c:
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dashboard puntos WiFi - DMQ</title>
        {%favicon%}
        {%css%}
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(127deg, #ff9a00 45%, #ff5e00 45%);
                min-height: 100vh;
            }

            .dashboard-container {
                max-width: 1400px;
                margin: 0 auto;
                padding: 20px;
            }

            .header {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }

            .main-title {
                color: #2c3e50;
                font-size: 2.5em;
                font-weight: 700;
                margin-bottom: 10px;
                background: linear-gradient(127deg, #1e3c72, #2a5298);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            .subtitle {
                color: #7f8c8d;
                font-size: 1.2em;
                font-weight: 300;
            }

            .section {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }

            .section:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
            }

            .section-title {
                color: #2c3e50;
                font-size: 1.8em;
                font-weight: 600;
                margin-bottom: 20px;
                display: flex;
                align-items: center;
                gap: 10px;
            }

            .section-title::before {
                content: '';
                width: 4px;
                height: 25px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                border-radius: 2px;
            }

            .filter-container {
                background: rgba(248, 249, 250, 0.8);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 20px;
                border: 1px solid rgba(236, 240, 241, 0.5);
            }

            .filter-label {
                color: #2c3e50;
                font-weight: 600;
                margin-bottom: 10px;
                display: block;
            }

            .dropdown {
                border-radius: 10px;
                border: 2px solid #e9ecef;
                transition: all 0.3s ease;
            }

            .dropdown:hover {
                border-color: #667eea;
            }

            .content-placeholder {
                background: linear-gradient(135deg, #f8f9fa, #e9ecef);
                height: 400px;
                border-radius: 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #6c757d;
                font-size: 1.1em;
                border: 2px dashed #dee2e6;
                transition: all 0.3s ease;
            }

            .content-placeholder:hover {
                border-color: #667eea;
                background: linear-gradient(135deg, #e9ecef, #dee2e6);
            }

            .metrics-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }

            .metric-card {
                background: rgba(255, 255, 255, 0.9);
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.3);
                transition: transform 0.3s ease;
            }

            .metric-card:hover {
                transform: translateY(-3px);
            }

            .metric-value {
                font-size: 2.5em;
                font-weight: 700;
                color: #2c3e50;
                margin-bottom: 5px;
            }

            .metric-label {
                color: #7f8c8d;
                font-size: 0.9em;
                font-weight: 500;
            }

            .footer {
                text-align: center;
                color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                font-size: 0.9em;
                margin-top: 40px;
            }

            /* Responsive design */
            @media (max-width: 768px) {
                .dashboard-container {
                    padding: 10px;
                }

                .main-title {
                    font-size: 2em;
                }

                .section {
                    padding: 20px;
                }

                .metrics-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Diseño del dashboard
app.layout = html.Div([
    html.Div([
        # Header
        html.Div([
            html.H1("Dashboard de análisis - Puntos WiFi Quito", className="main-title"),
            html.P(
                "VISUALIZACION DE INFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO",
                className="subtitle")
        ], className="header"),

        # Métricas principales básicas
        # TODO: obtener los datos de los archivos creados.
        # TODO: definir con el equipo los filtros a usarse, los que están aquí son de ejemplo.
        html.Div([
            html.Div([
                html.Div(" ", className="metric-value"),
                html.Div("Total de puntos WiFi", className="metric-label")
            ], className="metric-card"),

            html.Div([
                html.Div(" ", className="metric-value"),
                html.Div("Parroquias cubiertas", className="metric-label")
            ], className="metric-card"),

            html.Div([
                html.Div(" ", className="metric-value"),
                html.Div("Administraciones zonales", className="metric-label")
            ], className="metric-card"),

            html.Div([
                html.Div(" ", className="metric-value"),
                html.Div("Brecha digital estimada", className="metric-label")
            ], className="metric-card"),
        ], className="metrics-grid"),

        # Sección: Gráficos estadísticos
        html.Div([
            html.H2("Estadísticas de cobertura en la ciudad", className="section-title"),

            html.Div([
                html.Label("Filtrar por administración zonal", className="filter-label"),
                dcc.Dropdown(
                    id="sector",
                    options=[{'label': 'Todas las Zonas', 'value': 'all'}],
                    value='all',
                    className="dropdown"
                ),
            ], className="filter-container"),

            html.Div([
                html.Div("Aquí cargar los gráficos estadísticos",
                         className="content-placeholder")
            ])
        ], className="section"),

        # Sección: Mapa interactivo
        html.Div([
            html.H2("Mapa interactivo de puntos WiFi", className="section-title"),

            html.Div([
                html.Label("Filtrar por parroquia", className="filter-label"),
                dcc.Dropdown(
                    id="parroquia",
                    options=[{'label': 'Todas las Parroquias', 'value': 'all'}],
                    value='all',
                    className="dropdown"
                ),
            ], className="filter-container"),

            html.Div([
                html.Div("Aquí cargar el mapa con los puntos WiFi",
                         className="content-placeholder")
            ])
        ], className="section"),

        # Sección: Zonas prioritarias
        html.Div([
            html.H2("Análisis de posibles zonas prioritarias", className="section-title"),

            html.Div([
                html.Label("Filtrar por nivel de prioridad", className="filter-label"),
                dcc.Dropdown(
                    id="cercania",
                    options=[
                        {'label': 'Todas las Zonas', 'value': 'all'},
                        {'label': '🟥 Alta Prioridad - Baja Cobertura', 'value': 'alta'},
                        {'label': '🟨 Prioridad Media - Cobertura aceptable', 'value': 'media'},
                        {'label': '🟩 Baja Prioridad - Buena Cobertura', 'value': 'baja'}
                    ],
                    value='all',
                    className="dropdown"
                ),
            ], className="filter-container"),

            html.Div([
                html.Div("Aquí cargar el análisis de la densidad",
                         className="content-placeholder")
            ])
        ], className="section"),

        # Footer
        html.Div([
            html.P("2025 Proyecto VISUALIZACION DE INFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO"),
            html.P("Datos proporcionados por el API de puntos WiFi del Distrito Metropolitano de Quito")
        ], className="footer")

    ], className="dashboard-container")
])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)