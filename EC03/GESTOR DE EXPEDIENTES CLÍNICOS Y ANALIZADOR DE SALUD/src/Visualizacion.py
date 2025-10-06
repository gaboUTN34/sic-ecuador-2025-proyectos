# Contenido para: src/visualizacion.py

import matplotlib.pyplot as plt
import seaborn as sns

def visualizar_datos(df):
    """
    Genera y MUESTRA un conjunto de visualizaciones avanzadas una por una.
    """
    print("\nMostrando visualizaciones... Cierra cada ventana para ver la siguiente.")
    
    # Estilo
    sns.set_theme(style="whitegrid", palette="muted")

    # Gráfico 1: Distribución de Edad de los Pacientes 
    sns.histplot(df['age'], kde=True, bins=30, color='skyblue')
    plt.title('Distribución de Edades de los Pacientes', fontsize=16)
    plt.xlabel('Edad', fontsize=12)
    plt.ylabel('Cantidad de Pacientes', fontsize=12)
    plt.tight_layout()
    plt.show() 

    #Gráfico 2: Conteo de Pacientes por Categoría de IMC 
    plt.figure(figsize=(10, 6))
    sns.countplot(y='Categoria_BMI', data=df, order=df['Categoria_BMI'].value_counts().index, palette='pastel')
    plt.title('Número de Pacientes por Categoría de IMC', fontsize=16)
    plt.xlabel('Cantidad de Pacientes', fontsize=12)
    plt.ylabel('Categoría de IMC', fontsize=12)
    plt.tight_layout()
    plt.show() 

      # === GRÁFICO 3 (NUEVO): Factores de Riesgo por Diabetes ===
    # Este gráfico avanzado muestra cómo se distribuyen el IMC, Colesterol y Presión Sistólica
    # para pacientes CON y SIN diabetes. Es perfecto para el análisis de comorbilidades.
    df_melted = df.melt(id_vars=['diabetes'], value_vars=['bmi', 'cholesterol', 'systolic_bp'], 
                        var_name='Metrica', value_name='Valor')
    g = sns.FacetGrid(df_melted, col="Metrica", hue="diabetes", sharex=False, sharey=False, height=4, aspect=1.2)
    g.map(sns.kdeplot, "Valor", fill=True, alpha=0.7)
    g.add_legend(title="Diabetes (1=Sí)")
    g.fig.suptitle('Distribución de Métricas Clave según Estado de Diabetes', y=1.03, fontsize=16)
    plt.show()

    # === GRÁFICO 4 (NUEVO): Nivel de Creatinina por Grupo de Edad (Riesgo Renal) ===
    # Un "Swarmplot" es muy útil para ver cada paciente como un punto individual,
    # evitando que se solapen. Ideal para visualizar el riesgo renal por edad.
    plt.figure(figsize=(12, 7))
    sns.swarmplot(data=df, x='Grupo_Etario', y='creatinine', 
                  order=["Niño/Adolescente", "Adulto Joven", "Adulto", "Adulto Mayor"])
    plt.axhline(y=1.3, color='r', linestyle='--', label='Límite de Riesgo (1.3)')
    plt.title('Nivel de Creatinina por Grupo de Edad', fontsize=16)
    plt.xlabel('Grupo de Edad', fontsize=12)
    plt.ylabel('Nivel de Creatinina', fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.show()

  



    print("\nFin de las visualizaciones.")