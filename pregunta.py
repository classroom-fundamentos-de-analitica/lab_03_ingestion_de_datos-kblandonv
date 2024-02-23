"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd

def ingest_data():
    # Leer el archivo 'clusters_report.txt'
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Crear listas para almacenar los datos
    cluster = []
    cantidad_de_palabras_clave = []
    porcentaje_de_palabras_clave = []
    principales_palabras_clave = []

    # Iterar sobre las líneas del archivo y extraer los datos
    for line in lines:
        if line.strip() and not line.startswith('-'):
            # Dividir la línea en partes usando múltiples espacios como delimitador
            parts = line.split()

            # Extraer los datos de cada columna
            cluster.append(int(parts[0]))
            cantidad_de_palabras_clave.append(int(parts[1]))
            porcentaje_de_palabras_clave.append(float(parts[2].replace('%', '')))
            principales_palabras_clave.append(', '.join(parts[3:]))

    # Crear el DataFrame
    df = pd.DataFrame({
        'cluster': cluster,
        'cantidad_de_palabras_clave': cantidad_de_palabras_clave,
        'porcentaje_de_palabras_clave': porcentaje_de_palabras_clave,
        'principales_palabras_clave': principales_palabras_clave
    })

    return df

# Llamar a la función para obtener el DataFrame
df = ingest_data()
print(df)


