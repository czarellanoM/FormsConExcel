import json
import csv

# Leer el archivo JSON
RutaJson = 'datos.json'


with open(RutaJson) as json_file:
    data = json.load(json_file)

# Obtener las columnas del archivo JSON
columns = [col['label'] for col in data['table']['cols']]

# Obtener las filas del archivo JSON
rows = [row['c'] for row in data['table']['rows']]

# Crear un archivo CSV y escribir las columnas
with open('archivo.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)

    # Escribir las filas en el archivo CSV
    for row in rows:
        values = [col['v'] if 'v' in col else None for col in row]
        writer.writerow(values)

print("El archivo CSV se ha creado correctamente.")
