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
    # Leer el archivo 'clusters_report.txt' omitiendo la primera fila
    df = pd.read_csv('clusters_report.txt', skiprows=[0], sep='\s+', engine='python')

    # Ajustar los nombres de las columnas
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Reemplazar los espacios en las palabras clave por coma y espacio
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(' ', ', ')

    return df

# Llamada a la función para obtener el DataFrame
df = ingest_data()
print(df)