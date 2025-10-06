# Contenido para: src/visualizacion.py

import matplotlib.pyplot as plt
import seaborn as sns
import os # os ya no es necesario para crear carpetas, pero es buena práctica mantenerlo si se añaden otras funciones

def visualizar_datos(df):
    """
    Genera y MUESTRA un conjunto de visualizaciones avanzadas una por una.
    """
    print("\nMostrando visualizaciones... Cierra cada ventana para ver la siguiente.")
    
    # --- Preparación y Estilo ---
    sns.set_theme(style="whitegrid", palette="muted")

    # === Gráfico 1: Distribución de Edad de los Pacientes ===
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], kde=True, bins=30, color='skyblue')
    plt.title('Distribución de Edades de los Pacientes', fontsize=16)
    plt.xlabel('Edad', fontsize=12)
    plt.ylabel('Cantidad de Pacientes', fontsize=12)
    plt.tight_layout()
    plt.show() # <-- CAMBIO: Muestra el gráfico y pausa el programa

    # === Gráfico 2: Conteo de Pacientes por Categoría de IMC ===
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Categoria_BMI', data=df, order=df['Categoria_BMI'].value_counts().index, palette='pastel')
    plt.title('Número de Pacientes por Categoría de IMC', fontsize=16)
    plt.xlabel('Cantidad de Pacientes', fontsize=12)
    plt.ylabel('Categoría de IMC', fontsize=12)
    plt.tight_layout()
    plt.show() # <-- CAMBIO: Muestra el gráfico y pausa el programa

    # === Gráfico 3: Relación entre Colesterol y Presión Arterial ===
    plt.figure(figsize=(10, 7))
    sns.scatterplot(
        data=df, 
        x='cholesterol', 
        y='systolic_bp', 
        hue='diabetes',
        palette={0: 'blue', 1: 'red'},
        alpha=0.6
    )
    plt.title('Colesterol vs. Presión Sistólica (Coloreado por Diabetes)', fontsize=16)
    plt.xlabel('Nivel de Colesterol', fontsize=12)
    plt.ylabel('Presión Arterial Sistólica', fontsize=12)
    plt.legend(title='Diabetes (1=Sí, 0=No)')
    plt.tight_layout()
    plt.show() # <-- CAMBIO: Muestra el gráfico y pausa el programa
    
    # === Gráfico 4: Distribución de Glucosa por Diagnóstico ===
    plt.figure(figsize=(12, 7))
    sns.violinplot(data=df, x='diagnosis', y='glucose', palette='rocket')
    plt.title('Distribución de Glucosa por Diagnóstico Principal', fontsize=16)
    plt.xlabel('Diagnóstico', fontsize=12)
    plt.ylabel('Nivel de Glucosa', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show() # <-- CAMBIO: Muestra el gráfico y pausa el programa

    print("\nFin de las visualizaciones.")