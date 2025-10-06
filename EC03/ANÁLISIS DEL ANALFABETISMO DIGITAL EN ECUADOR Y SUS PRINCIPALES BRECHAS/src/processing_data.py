
import pandas as pd
import matplotlib.pyplot as plt
import numpy

from src.cleaning import retornar_dataframe


class Data:
    def __init__(self):
        self.df = retornar_dataframe()

    def show_dataframe(self):
        print(self.df)

    def provincia_puntuacion(self):
        self.df['Puntuacion'] = pd.to_numeric(self.df['Puntuacion'], errors='coerce')
        self.df['Puntuacion'] = self.df['Puntuacion'].fillna(0)

        df_promedio_provincia = self.df.groupby('Provincia')['Puntuacion'].mean().reset_index()
        print(df_promedio_provincia)
        return df_promedio_provincia

    def genero_puntuacion_edad(self):
        df_edad_genero = self.df.copy()
        df_edad_genero = df_edad_genero.dropna(subset=['Edad','Genero'])
        df_edad_genero['Edad'] = pd.to_numeric(df_edad_genero['Edad'],errors='coerce')
        df_edad_genero['Puntuacion'] = pd.to_numeric(df_edad_genero['Puntuacion'], errors='coerce')

        df_edad_genero['Puntuacion'] = df_edad_genero['Puntuacion'].fillna(0)

        df_edad_genero['RangoEdad'] = pd.cut(df_edad_genero['Edad'], bins=[0,12,18,30,60,100],labels=['0-12','12-18','18-30','30-60','+60'],right=False)
        
        df_genero_puntuacion = (df_edad_genero.groupby(['Genero','RangoEdad'])['Puntuacion'].mean().reset_index())

        df_genero_puntuacion['Puntuacion'] = df_genero_puntuacion['Puntuacion'].fillna(0).round(2)
        print(df_genero_puntuacion)
        return df_genero_puntuacion

    def empresa_competencia(self):
        df_copia = self.df.copy()
        df_empresa_competencia = df_copia.rename(columns={'Registre su tipo de empresa organizacion ciudadano':'Empresa',
                                                          'Conoce su nivel de competencia digital e identifica claramente sus carencias con respecto a los requisitos de su entorno laboral': 'Entorno'})
        df_empresa_competencia['Entorno'] = df_empresa_competencia['Entorno'].map({'Si':1,'No':0})
        df_empresa_entorno = (df_empresa_competencia.groupby(['Empresa'])['Entorno'].sum().reset_index())
        print(df_empresa_entorno)
        return df_empresa_entorno
