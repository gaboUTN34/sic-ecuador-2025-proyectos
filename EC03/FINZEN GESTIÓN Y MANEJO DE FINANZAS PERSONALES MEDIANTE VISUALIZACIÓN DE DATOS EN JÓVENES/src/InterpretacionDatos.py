#====================================================================#
#             4.             Interpretación de Datos                 #
#====================================================================#
import pandas as pd
import numpy as np
import ProcesamientoDatos as pdata

# 1️.- Edad con mayores gastos

if "edad" in pdata.df_finanzas.columns and ("total_gastos" in pdata.df_finanzas.columns or "gastos_prioritarios" in pdata.df_finanzas.columns):
    # Calcular total_gastos si no existe
    if "total_gastos" not in pdata.df_finanzas.columns:
        def _sumar_gastos(fila):
            gp = sum(fila["gastos_prioritarios"].values()) if isinstance(fila.get("gastos_prioritarios"), dict) else 0
            gs = sum(fila["gastos_secundarios"].values()) if isinstance(fila.get("gastos_secundarios"), dict) else 0
            return gp + gs
        pdata.df_finanzas["total_gastos"] = pdata.df_finanzas.apply(_sumar_gastos, axis=1)

    # Promedio de gasto por edad
    promedio_por_edad = (
        pdata.df_finanzas.groupby("edad")["total_gastos"]
        .mean()
        .reset_index()
        .sort_values("total_gastos", ascending=False)
    )

    edad_max_gasto = promedio_por_edad.iloc[0]
    print("\n EDAD CON MAYORES GASTOS")
    print("-" * 50)
    print(f"La edad con mayor gasto promedio es {int(edad_max_gasto['edad'])} años, con un gasto medio de ${edad_max_gasto['total_gastos']:.2f}.")
    print("Esto puede reflejar que a medida que los jóvenes avanzan en edad, asumen más responsabilidades económicas o consumos personales.")

#2.- Correlación entre género y gastos
print("\nCORRELACIÓN ENTRE GÉNERO Y GASTOS ")
print("-" * 50)

df_corr = pdata.df_finanzas.copy()

# Convertir 'genero' a valores numéricos (0,1,2)
if "genero" in df_corr.columns:
    df_corr["genero_num"] = df_corr["genero"].astype("category").cat.codes

# Seleccionar solo columnas numéricas relevantes
columnas_numericas = [c for c in df_corr.columns if pd.api.types.is_numeric_dtype(df_corr[c])]

if len(columnas_numericas) >= 2:
    matriz_correlacion = df_corr[columnas_numericas].corr()

    print("Matriz de correlación (valores redondeados a 3 decimales):")
    print(matriz_correlacion.round(3))

    # Interpretación enfocada 
    if "genero_num" in matriz_correlacion.columns and "total_gastos" in matriz_correlacion.columns:
        corr_gen_gasto = matriz_correlacion.loc["genero_num", "total_gastos"]
        print("\n Interpretación del resultado:")
        if abs(corr_gen_gasto) < 0.2:
            print(f"- Correlación débil ({corr_gen_gasto:.3f}): el género tiene poca influencia en el nivel de gastos.")
        elif abs(corr_gen_gasto) < 0.5:
            print(f"- Correlación moderada ({corr_gen_gasto:.3f}): se observan ligeras diferencias en el comportamiento de gasto entre géneros.")
        else:
            print(f"- Correlación fuerte ({corr_gen_gasto:.3f}): existe una clara relación entre el género y el nivel de gasto.")
        print("En el contexto del proyecto FINZEN, esto puede reflejar diferentes patrones de consumo y prioridades financieras entre jóvenes según su género.")


# 3️.- Ahorro y dificultad percibida

if "ahorro_real" in pdata.df_finanzas.columns and "dificultad_equilibrio" in pdata.df_finanzas.columns:
    correlacion_ahorro_dificultad = pdata.df_finanzas["ahorro_real"].corr(pdata.df_finanzas["dificultad_equilibrio"])
    print("\n RELACIÓN ENTRE AHORRO Y DIFICULTAD FINANCIERA")
    print("-" * 50)
    print(f"Coeficiente de correlación: {correlacion_ahorro_dificultad:.3f}")
    if correlacion_ahorro_dificultad < -0.5:
        print(" Correlación negativa fuerte: a mayor ahorro, menor dificultad para equilibrar las finanzas.")
    elif correlacion_ahorro_dificultad < -0.2:
        print("Correlación negativa moderada: quienes logran ahorrar suelen sentir menos presión económica.")
    else:
        print("Correlación baja o nula: el ahorro real no parece influir directamente en la dificultad percibida.")
