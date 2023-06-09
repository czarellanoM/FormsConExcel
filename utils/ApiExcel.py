import requests
import json


def fetch_data_from_google_sheets(url):

    # Realizar la solicitud GET a la API
    response = requests.get(url)

    # Obtener el contenido de la respuesta en formato JSON
    content = response.content.decode('utf-8').replace('/*O_o*/\ngoogle.visualization.Query.setResponse(', '')[:-2]

    # Convertir el contenido JSON a un diccionario de Python
    data = json.loads(content)

    # Ruta del archivo JSON de salida
    archivo_json = 'archivos\datos.json'

    # Guardar los datos en un archivo JSON
    with open(archivo_json, 'w') as file:
        json.dump(data, file, indent=4)


    #print(f"Los datos se han guardado en el archivo '{archivo_json}'.")
