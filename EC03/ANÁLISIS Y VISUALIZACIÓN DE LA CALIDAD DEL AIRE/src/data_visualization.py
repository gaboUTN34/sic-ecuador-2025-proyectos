"""
Módulo: Visualización de Datos de Calidad del Aire
---------------------------------------------------
Proporciona funciones para crear visualizaciones interactivas y estáticas
del análisis de calidad del aire, incluyendo series temporales, distribuciones,
correlaciones y análisis del Índice de Calidad del Aire (ICA).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional, Tuple
import warnings

warnings.filterwarnings('ignore')

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Colores ICA (importados de tu módulo)
ICA_COLORS = {
    "Buena": "#00E400",
    "Moderada": "#FFFF00",
    "Dañina para grupos sensibles": "#FF7E00",
    "Dañina": "#FF0000",
    "Muy dañina": "#8F3F97",
    "Peligrosa": "#7E0023"
}

CONTAMINANTES = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']


def plot_time_series(df: pd.DataFrame, columnas: List[str] = ['pm2_5', 'pm10'], figsize: Tuple[int, int] = (14, 6), titulo: str = "Evolución Temporal de Contaminantes") -> None:
    """
    Gráfico de líneas para visualizar la evolución temporal de contaminantes.
    
    Parámetros:
        df: DataFrame con índice datetime
        columnas: Lista de columnas a graficar
        figsize: Tamaño de la figura
        titulo: Título del gráfico
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    for col in columnas:
        if col in df.columns:
            ax.plot(df.index, df[col], label=col.upper(), linewidth=1.5, alpha=0.8)
    
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Concentración (µg/m³)", fontsize=12)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_ica_distribution(df: pd.DataFrame, 
                        figsize: Tuple[int, int] = (12, 5)) -> None:
    """
    Visualiza la distribución de categorías ICA mediante gráfico de barras y pie chart.
    
    Parámetros:
        df: DataFrame con columna 'ica_category'
        figsize: Tamaño de la figura
    """
    if 'ica_category' not in df.columns:
        print("❌ La columna 'ica_category' no existe. Ejecuta add_ica_category() primero.")
        return
    
    # Orden de categorías
    orden_ica = ["Buena", "Moderada", "Dañina para grupos sensibles", "Dañina", "Muy dañina", "Peligrosa"]
    
    # Contar frecuencias
    counts = df['ica_category'].value_counts()
    counts = counts.reindex(orden_ica, fill_value=0)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Gráfico de barras
    colors = [ICA_COLORS.get(cat, '#CCCCCC') for cat in counts.index]
    ax1.bar(range(len(counts)), counts.values, color=colors, edgecolor='black', alpha=0.8)
    ax1.set_xticks(range(len(counts)))
    ax1.set_xticklabels(counts.index, rotation=45, ha='right', fontsize=9)
    ax1.set_ylabel("Frecuencia", fontsize=11)
    ax1.set_title("Distribución de Categorías ICA", fontsize=13, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Gráfico circular
    ax2.pie(counts.values, labels=counts.index, colors=colors, autopct='%1.1f%%',
            startangle=90, textprops={'fontsize': 9})
    ax2.set_title("Proporción de Días por Categoría ICA", fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def plot_heatmap_hourly(df: pd.DataFrame, columna: str = 'pm2_5', figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Heatmap mostrando patrones horarios y por día de la semana.
    
    Parámetros:
        df: DataFrame con índice datetime
        columna: Columna a visualizar
        figsize: Tamaño de la figura
    """
    if columna not in df.columns:
        print(f"❌ La columna '{columna}' no existe en el DataFrame.")
        return
    
    # Crear copia con día de semana y hora
    df_temp = df.copy()
    df_temp['dow'] = df_temp.index.dayofweek  # 0=Lunes, 6=Domingo
    df_temp['hour'] = df_temp.index.hour
    
    # Pivotear datos
    pivot = df_temp.pivot_table(values=columna, index='dow', columns='hour', aggfunc='mean')
    
    # Nombres de días
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    pivot.index = [dias[i] for i in pivot.index]
    
    # Crear heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(pivot, cmap='YlOrRd', annot=False, fmt='.1f', cbar_kws={'label': f'{columna.upper()} (µg/m³)'})
    plt.title(f'Patrón Horario de {columna.upper()} por Día de la Semana', fontsize=14, fontweight='bold')
    plt.xlabel('Hora del Día', fontsize=12)
    plt.ylabel('Día de la Semana', fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_monthly_boxplot(df: pd.DataFrame, 
                        columna: str = 'pm2_5',
                        figsize: Tuple[int, int] = (14, 6)) -> None:
    """
    Boxplot mostrando la distribución mensual de un contaminante.
    
    Parámetros:
        df: DataFrame con columna 'month'
        columna: Columna a visualizar
        figsize: Tamaño de la figura
    """
    if columna not in df.columns or 'month' not in df.columns:
        print(f"❌ Falta columna '{columna}' o 'month' en el DataFrame.")
        return
    
    plt.figure(figsize=figsize)
    
    # Preparar datos
    df_plot = df[[columna, 'month']].dropna()
    
    # Crear boxplot
    bp = plt.boxplot([df_plot[df_plot['month'] == m][columna].values 
                    for m in range(1, 13)],
                    labels=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
                    patch_artist=True, showfliers=True)
    
    # Colorear cajas
    colors = plt.cm.viridis(np.linspace(0, 1, 12))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    plt.xlabel("Mes", fontsize=12)
    plt.ylabel(f"{columna.upper()} (µg/m³)", fontsize=12)
    plt.title(f"Distribución Mensual de {columna.upper()}", fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df: pd.DataFrame, 
                        columnas: Optional[List[str]] = None,
                        figsize: Tuple[int, int] = (10, 8)) -> None:
    """
    Matriz de correlación entre contaminantes.
    
    Parámetros:
        df: DataFrame con datos de contaminantes
        columnas: Lista de columnas a correlacionar (por defecto CONTAMINANTES)
        figsize: Tamaño de la figura
    """
    if columnas is None:
        columnas = [c for c in CONTAMINANTES if c in df.columns]
    else:
        columnas = [c for c in columnas if c in df.columns]
    
    if len(columnas) < 2:
        print("❌ Se necesitan al menos 2 columnas para calcular correlaciones.")
        return
    
    # Calcular correlación
    corr = df[columnas].corr()
    
    # Crear heatmap
    plt.figure(figsize=figsize)
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Máscara triangular
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title("Matriz de Correlación entre Contaminantes", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_top_n_contaminated_days(df: pd.DataFrame, 
                                columna: str = 'pm2_5',
                                n: int = 10,
                                figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Gráfico de barras horizontales de los N días más contaminados.
    
    Parámetros:
        df: DataFrame con índice datetime
        columna: Columna a analizar
        n: Número de días a mostrar
        figsize: Tamaño de la figura
    """
    if columna not in df.columns:
        print(f"❌ La columna '{columna}' no existe.")
        return
    
    # Agrupar por día y ordenar
    daily = df.groupby(df.index.date)[columna].mean().sort_values(ascending=False).head(n)
    
    # Crear gráfico
    plt.figure(figsize=figsize)
    colors = plt.cm.Reds(np.linspace(0.4, 0.9, n))
    plt.barh(range(n), daily.values, color=colors, edgecolor='black', alpha=0.8)
    plt.yticks(range(n), [str(d) for d in daily.index])
    plt.xlabel(f"{columna.upper()} (µg/m³)", fontsize=12)
    plt.ylabel("Fecha", fontsize=12)
    plt.title(f"Top {n} Días con Mayor Concentración de {columna.upper()}", 
            fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_distribution_histogram(df: pd.DataFrame, 
                                columna: str = 'pm2_5',
                                bins: int = 50,
                                figsize: Tuple[int, int] = (10, 6)) -> None:
    """
    Histograma con curva KDE mostrando la distribución de un contaminante.
    
    Parámetros:
        df: DataFrame
        columna: Columna a visualizar
        bins: Número de bins del histograma
        figsize: Tamaño de la figura
    """
    if columna not in df.columns:
        print(f"❌ La columna '{columna}' no existe.")
        return
    
    data = df[columna].dropna()
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Histograma
    ax.hist(data, bins=bins, color='skyblue', edgecolor='black', 
            alpha=0.7, density=True, label='Histograma')
    
    # Curva KDE
    data.plot(kind='kde', ax=ax, color='red', linewidth=2, label='KDE')
    
    ax.set_xlabel(f"{columna.upper()} (µg/m³)", fontsize=12)
    ax.set_ylabel("Densidad", fontsize=12)
    ax.set_title(f"Distribución de {columna.upper()}", fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_scatter_comparison(df: pd.DataFrame, 
                        col_x: str = 'pm2_5', 
                        col_y: str = 'pm10',
                        figsize: Tuple[int, int] = (10, 6)) -> None:
    """
    Scatter plot comparando dos contaminantes.
    
    Parámetros:
        df: DataFrame
        col_x: Columna para eje X
        col_y: Columna para eje Y
        figsize: Tamaño de la figura
    """
    if col_x not in df.columns or col_y not in df.columns:
        print(f"❌ Una o ambas columnas no existen en el DataFrame.")
        return
    
    plt.figure(figsize=figsize)
    plt.scatter(df[col_x], df[col_y], alpha=0.5, s=10, c='purple', edgecolors='none')
    plt.xlabel(f"{col_x.upper()} (µg/m³)", fontsize=12)
    plt.ylabel(f"{col_y.upper()} (µg/m³)", fontsize=12)
    plt.title(f"Relación entre {col_x.upper()} y {col_y.upper()}", 
            fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_monthly_averages(df: pd.DataFrame, 
                        columna: str = 'pm2_5',
                        figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Gráfico de barras de promedios mensuales.
    
    Parámetros:
        df: DataFrame con columna 'month'
        columna: Columna a promediar
        figsize: Tamaño de la figura
    """
    if columna not in df.columns or 'month' not in df.columns:
        print(f"❌ Falta columna '{columna}' o 'month'.")
        return
    
    monthly = df.groupby('month')[columna].mean()
    
    plt.figure(figsize=figsize)
    colors = plt.cm.plasma(np.linspace(0, 1, 12))
    plt.bar(monthly.index, monthly.values, color=colors, edgecolor='black', alpha=0.8)
    plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                            'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
    plt.xlabel("Mes", fontsize=12)
    plt.ylabel(f"Promedio de {columna.upper()} (µg/m³)", fontsize=12)
    plt.title(f"Promedio Mensual de {columna.upper()}", fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def create_dashboard_summary(df: pd.DataFrame, 
                            columna_principal: str = 'pm2_5',
                            figsize: Tuple[int, int] = (16, 12)) -> None:
    """
    Dashboard completo con múltiples visualizaciones en una sola figura.
    
    Parámetros:
        df: DataFrame completo
        columna_principal: Contaminante principal a analizar
        figsize: Tamaño de la figura
    """
    fig = plt.figure(figsize=figsize)
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # 1. Serie temporal
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(df.index, df[columna_principal], color='steelblue', linewidth=1)
    ax1.set_title(f'Evolución Temporal de {columna_principal.upper()}', fontweight='bold')
    ax1.set_ylabel('Concentración (µg/m³)')
    ax1.grid(True, alpha=0.3)
    
    # 2. Distribución ICA
    if 'ica_category' in df.columns:
        ax2 = fig.add_subplot(gs[1, 0])
        counts = df['ica_category'].value_counts()
        colors_ica = [ICA_COLORS.get(cat, '#CCCCCC') for cat in counts.index]
        ax2.bar(range(len(counts)), counts.values, color=colors_ica, alpha=0.8)
        ax2.set_xticks(range(len(counts)))
        ax2.set_xticklabels(counts.index, rotation=45, ha='right', fontsize=8)
        ax2.set_title('Distribución Categorías ICA', fontweight='bold')
        ax2.set_ylabel('Frecuencia')
    
    # 3. Histograma
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.hist(df[columna_principal].dropna(), bins=40, color='coral', 
            edgecolor='black', alpha=0.7)
    ax3.set_title(f'Distribución de {columna_principal.upper()}', fontweight='bold')
    ax3.set_xlabel('Concentración (µg/m³)')
    ax3.set_ylabel('Frecuencia')
    
    # 4. Promedios mensuales
    if 'month' in df.columns:
        ax4 = fig.add_subplot(gs[2, 0])
        monthly = df.groupby('month')[columna_principal].mean()
        ax4.bar(monthly.index, monthly.values, color='mediumseagreen', alpha=0.8)
        ax4.set_title('Promedio Mensual', fontweight='bold')
        ax4.set_xlabel('Mes')
        ax4.set_ylabel(f'{columna_principal.upper()} (µg/m³)')
        ax4.set_xticks(range(1, 13))
    
    # 5. Top días contaminados
    ax5 = fig.add_subplot(gs[2, 1])
    daily = df.groupby(df.index.date)[columna_principal].mean().sort_values(ascending=False).head(7)
    ax5.barh(range(len(daily)), daily.values, color='crimson', alpha=0.8)
    ax5.set_yticks(range(len(daily)))
    ax5.set_yticklabels([str(d) for d in daily.index], fontsize=8)
    ax5.set_title('Top 7 Días Más Contaminados', fontweight='bold')
    ax5.set_xlabel(f'{columna_principal.upper()} (µg/m³)')
    ax5.invert_yaxis()
    
    plt.suptitle('Dashboard de Calidad del Aire', fontsize=16, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()