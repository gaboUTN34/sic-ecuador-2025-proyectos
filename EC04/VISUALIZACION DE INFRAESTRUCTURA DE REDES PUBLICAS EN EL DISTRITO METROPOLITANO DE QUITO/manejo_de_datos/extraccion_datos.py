import requests
import pandas as pd
import os


URL_API = "https://tecnologia.quito.gob.ec/wifi_apirest.php"
ARCHIVO_SALIDA = os.path.join(os.path.dirname(__file__), 'puntos_wifi.csv')


def extraer_datos(url):
    
    """
    Algoritmo de la función para extraer los datos de la API elegida
    sin ordenar, para comprobar la correcta extracción de los mismos.
    """
    
    try:
        respponse = requests.get(URL_API)
        data = respponse.json()
        
        zonas_wifi = data.get("resultados", [])
        
        if not zonas_wifi:
            print("La API no devolvió datos.")
            return None
        
        df = pd.DataFrame(zonas_wifi)
        print("Extracción exitosa de datos. Zonas Wifi obtenidas")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None
    
if __name__ == "__main__":
    datos_extraidos = extraer_datos(URL_API)
    