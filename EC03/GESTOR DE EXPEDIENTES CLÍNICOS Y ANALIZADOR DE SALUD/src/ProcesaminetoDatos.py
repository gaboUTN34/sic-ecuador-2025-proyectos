import pandas as pd

# Leer dataset local
df = pd.read_csv("EC03/GESTOR DE EXPEDIENTES CLÍNICOS Y ANALIZADOR DE SALUD/data/dataset_final.csv")  # ajusta el nombre si es diferente

#Creara columnas adicionales
Grupo_etario_lista = []
Categoria_bmi_lista =[]

for i, row in df.iterrows():
    edad = row["age"]
    if edad < 18:
        Grupo_etario_lista.append("Niño/Adolescente")
    elif 18 <= edad < 40:
        Grupo_etario_lista.append("Adulto Joven")
    elif 40 <= edad < 65:
        Grupo_etario_lista.append("Adulto")
    else:
        Grupo_etario_lista.append("Adulto Mayor")
    
    bmi = row['bmi']
    if bmi < 18.5:
        Categoria_bmi_lista.append("Bajo Peso")
    elif 18.5 <= bmi < 25:
        Categoria_bmi_lista.append("Normal")
    elif 25 <= bmi < 30:
        Categoria_bmi_lista.append("Sobrepeso")
    else:
        Categoria_bmi_lista.append("Obesidad")
        
df["Grupo_Etario"] = Grupo_etario_lista
df["Categoria_BMI"] = Categoria_bmi_lista

print("="*60)
print("PUNTAJE DE RIESGO")
print("="*60)

def clasificar_glucosa(df):
    normales = []
    prediabetes = []
    nuevo_diabetes = []
    con_diabetes = []

    for _, fila in df.iterrows():
        id_paciente = fila ["patient_id"]
        valor_glucosa = fila ["glucose"]
        diag_diabetes = fila ["diabetes"]

        if valor_glucosa < 140 and diag_diabetes == 0:
            normales.append((id_paciente, valor_glucosa))
        elif 140 <= valor_glucosa < 200 and diag_diabetes == 0:
            prediabetes.append((id_paciente, valor_glucosa))
        elif 200 <= valor_glucosa and diag_diabetes == 0:
            nuevo_diabetes.append((id_paciente, valor_glucosa))
        else:
            con_diabetes.append((id_paciente, valor_glucosa))
        
    df_normales = pd.DataFrame(normales, columns=["patient_id", "glucose"])
    df_prediabetes = pd.DataFrame(prediabetes, columns=["patient_id", "glucose"])
    df_nuevo_diabetes = pd.DataFrame(nuevo_diabetes, columns=["patient_id", "glucose"])
    df_con_diabetes = pd.DataFrame(con_diabetes, columns=["patient_id", "glucose"])

    return df_normales, df_prediabetes, df_nuevo_diabetes, df_con_diabetes  

df_normales, df_prediabetes, df_nuevo_diabetes, df_con_diabetes = clasificar_glucosa(df)
print("="*60)
print("PACIENTES CLASIFICADOS MEDICIÓN DE GLUCOSA")
print("="*60)

print("Cantidad de pacientes normales:", len(df_normales))
print("Normales:")
print(df_normales.head(20), "\n")

print("Cantidad de pacientes con prediabetes:", len(df_prediabetes))
print("Prediabetes:")
print(df_prediabetes.head(), "\n")

print("Cantidad de pacientes con nuevo diagnóstico de diabetes:", len(df_nuevo_diabetes))
print("Recien diagnosticados con Diabetes:")
print(df_nuevo_diabetes.head(), "\n")

print("Cantidad de pacientes con diabetes diagnosticada:", len(df_con_diabetes))
print("Prediagnosticados con Diabetes:")
print(df_con_diabetes.head(), "\n")






