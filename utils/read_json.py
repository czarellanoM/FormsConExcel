import json

# Cargar los datos desde el archivo JSON
with open('archivos\datos.json') as file:
    data = json.load(file)

# Obtener las filas de los datos
rows = data['table']['rows']

# Recorrer las filas y obtener los valores de las columnas deseadas
for row in rows:
    marca_temporal = row['c'][0]['v']
    asesores = row['c'][1]['v']
    tactico_entregar = row['c'][2]['v']
    cliente = row['c'][3]['v']
    cc = row['c'][4]['v']
    LineaBeneficio = row['c'][5]['v']
    Dummi = row['c'][6]['v']
    Imsi = row['c'][7]['v']
    submitLinea = row['c'][8]['v']


    # Hacer algo con los valores obtenidos
    print(f"Marca temporal: {marca_temporal}")
    print(f"Asesores: {asesores}")
    print(f"Táctico a entregar: {tactico_entregar}")
    print(f"cliente: {cliente}")
    print(f"Lienea en beneficio: {LineaBeneficio}")
    print(f"DUMMI: {Dummi}")
    print(f"Imsi: {Imsi}")
    print(f"Enviada : {submitLinea}")
    
