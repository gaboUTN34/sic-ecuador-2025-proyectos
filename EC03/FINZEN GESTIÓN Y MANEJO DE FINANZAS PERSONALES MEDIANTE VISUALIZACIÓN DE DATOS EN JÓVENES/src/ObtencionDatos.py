import pandas as pd
import numpy as np

#====================================================================#
#                 1.     Obtencion de datos                          #
#====================================================================#

def obtener_datos(nombre_archivo):
  # Cambia 'mi_archivo.xlsx' por la ruta real de tu archivo
  df = pd.read_csv(nombre_archivo, sep=';')


  def nuevo_dic(data):
      data_str = str(data).strip()
      if "$" in data_str :
        data_str = data_str.replace("$", "")
      if "%" in data_str :
        data_str = data_str.replace("%", "")
      dic = {}

      # Si NO hay comas, procesar como un solo elemento
      if " " not in data_str:
          if not data_str:
              return {"0": "0"}

          if ":" in data_str:
              clave, valor = data_str.split(":", 1)
              clave = clave.strip()
              valor_str = valor.strip()
              # Attempt to convert to int, handle errors by keeping as string
              try:
                  valor = int(valor_str)
              except ValueError:
                  valor = valor_str
          else:
              clave = "0"
              valor = data_str # Use the element as value

          dic[clave] = valor
          return dic

      # Si HAY comas, procesar múltiples elementos
      else:
          elementos = data_str.split(" ")

          for elemento in elementos:
              elemento = elemento.strip()
              if not elemento:
                  continue

              if ":" in elemento:
                  clave, valor = elemento.split(":", 1)
                  clave = clave.strip()
                  valor_str = valor.strip()
                  # Attempt to convert to int, handle errors by keeping as string
                  try:
                      valor = int(valor_str)
                  except ValueError:
                      valor = valor_str
              else:
                  clave = "0"
                  valor = elemento  # Usar el elemento como valor

              dic[clave] = valor

          return dic

  # Rename columns
  df.rename(columns={
      "Id": "id",
      "Nombre": "nombre",
      "Apellido": "apellido",
      "Ingrese su edad": "edad",
      "Cedula": "cedula",
      "Género": "genero",
      "¿Cuenta con apoyo financiero por parte de su familia?": "apoyo_familiar",
      "¿Esta estudiando actualmente?": "estudio_actual",
      "¿Qué carrera universitaria o técnica estás cursando actualmente?": "carrera",
      "¿Esta trabajando actualmente?": "trabajo_actual",
      "¿Cual es tu ocupacion o puesto en tu trabajo?": "ocupacion",
      "¿Estas emprendiendo actualmente?": "emprendimiento_actual",
      "¿Como se llama tu negocio?": "nombre_negocio",
      "¿Cuenta con ingresos mensuales (Trabajo fijo, Temporal, Negocio propio, Apoyo familiar, Otro)?": "tipo_ingreso",
      "¿Cuáles son sus ingresos mensuales? (USD)": "ingresos",
      "¿Cuáles son sus gastos fundamentales al mes ? (USD)": "gastos_prioritarios",
      "¿Cuáles son sus gastos ocasionales al mes? (USD)": "gastos_secundarios",
      "¿Qué porcentaje de tus ingresos destinas al ahorro?": "porcentaje_ahorro",
      "En una escala del 1 al 5, qué tan difícil es para ti equilibrar tus finanzas (ingresos con respecto a tus gastos)?": "dificultad_equilibrio"
  }, inplace=True)

  # Nombres de las columnas dentro del dataframe que se transformaran en diccionarios
  columnas_con_diccionarios = [
      "ingresos",
      "gastos_prioritarios",
      "gastos_secundarios"
  ]

  # Apply nuevo_dic function to specified columns
  for col in columnas_con_diccionarios:
      df[col] = df[col].apply(nuevo_dic)

  return df