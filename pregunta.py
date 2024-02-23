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
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    data = []
    # Selecciona las líneas que contienen datos y omite las líneas vacías y las líneas de separación
    for line in lines:
        if line.strip() and not line.startswith('-'):
            row = line.split()
            # Unir las palabras clave con espacios múltiples
            if len(row) > 4:
                keywords = ' '.join(row[3:])
                row = row[:3] + [keywords]
            data.append(row)

    # Crear DataFrame
    df = pd.DataFrame(data, columns=['Cluster', 'Cantidad_de_palabras_clave', 'Porcentaje_de_palabras_clave', 'Palabras_clave'])

    # Reemplazar porcentaje
    df['Porcentaje_de_palabras_clave'] = df['Porcentaje_de_palabras_clave'].str.replace('%', '')

    # Convertir columnas a tipos numéricos donde sea aplicable
    df['Cantidad_de_palabras_clave'] = pd.to_numeric(df['Cantidad_de_palabras_clave'], errors='coerce')

    return df

# Llamada a la función para obtener el DataFrame
df = ingest_data()
print(df)
