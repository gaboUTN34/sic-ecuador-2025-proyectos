import pandas as pd

# Leer dataset local
df = pd.read_csv("EC03/GESTOR DE EXPEDIENTES CLÍNICOS Y ANALIZADOR DE SALUD/src/synthetic_clinical_dataset.csv")  # ajusta el nombre si es diferente

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





