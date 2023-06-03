import json

def process_data(file_path):
    # Cargar los datos desde el archivo JSON
    with open(file_path) as file:
        data = json.load(file)

    # Obtener las filas de los datos
    rows = data['table']['rows']

    # Crear una lista de datos a enviar
    resultados = []

    # Recorrer las filas y obtener los valores de las columnas deseadas
    for row in rows:
        marca_temporal = row['c'][0]['v']
        asesores = str(row['c'][1]['v'])
        tactico_entregar = str(row['c'][2]['v'])
        cliente = str(row['c'][3]['v'])
        cc = str(row['c'][4]['v'])
        LineaBeneficio = int(row['c'][5]['v'])
        Dummi = int(row['c'][6]['v'])
        Imsi = str(row['c'][7]['v'])
        submitLinea = bool(row['c'][8]['v'])

        if submitLinea:
            datos = {
                'marca_temporal': marca_temporal,
                'asesores': asesores,
                'tactico_entregar': tactico_entregar,
                'cliente': cliente,
                'cc': cc,
                'LineaBeneficio': LineaBeneficio,
                'Dummi': Dummi,
                'Imsi': Imsi,
                'submitLinea': submitLinea
            }
            resultados.append(datos)

    return resultados

if __name__ == '__main__':
    data = process_data('archivos\datos.json')
    print(data[0])