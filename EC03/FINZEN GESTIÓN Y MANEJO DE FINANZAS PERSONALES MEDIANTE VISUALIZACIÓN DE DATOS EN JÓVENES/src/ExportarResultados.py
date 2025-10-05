import os 
import pandas as pd
#====================================================================#
#             e.    RESULTADOS Y EXPORTACIÓN                         #
#====================================================================#


#guardar Dataframes especificos en la ruta indicada
def guardar_resultados_csv (dfs: dict[str, pd.DataFrame], carpeta_salida: str = "data/resultados"):
     # Crear carpeta si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        print(f" Carpeta creada: {carpeta_salida}")

    # Guardar cada DataFrame
    for nombre, df in dfs.items():
        if not isinstance(df, pd.DataFrame):
            continue  # omitir si el valor no es un DataFrame

        ruta = os.path.join(carpeta_salida, f"{nombre}.csv")
        try:
            df.to_csv(ruta, index=False, encoding="utf-8-sig")
            print(f"Archivo guardado: {ruta}  ({len(df)} filas)")
        except Exception as e:
            print(f" Error al guardar {nombre}: {e}")



# Crear un Excel con varias hojas (una por cada DataFrame)
def guardar_resultados_excel(dfs: dict[str, pd.DataFrame], carpeta_salida: str = "data/resultados", nombre: str = "analisis_finzen.xlsx"):
    # Asegurar carpeta
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta = os.path.join(carpeta_salida, nombre)

    # Escribir cada DataFrame en su propia hoja
    with pd.ExcelWriter(ruta) as writer:
        for nombre_hoja, df in dfs.items():
            if isinstance(df, pd.DataFrame):
                df.to_excel(writer, sheet_name=str(nombre_hoja)[:31], index=False)

    print(f"Excel guardado en: {ruta}")
    return ruta