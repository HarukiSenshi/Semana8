from datetime import datetime

def buscar_vuelos(origen, destino, fecha_salida):
    """
    Busca vuelos en una lista de vuelos según el origen, destino y fecha de salida especificados.

    Parámetros:
    origen (str): El código IATA del aeropuerto de origen.
    destino (str): El código IATA del aeropuerto de destino.
    fecha_salida (str): La fecha de salida en formato 'AAAA-MM-DD'.

    Retorna:
    list: Una lista de vuelos que coinciden con los criterios de búsqueda.
    """
    # Verificación de tipos de entrada
    if not isinstance(origen, str) or not isinstance(destino, str) or not isinstance(fecha_salida, str):
        raise ValueError("Los parámetros origen, destino y fecha_salida deben ser cadenas de texto.")
    
    # Verificación de formato de la fecha
    try:
        fecha_salida_dt = datetime.strptime(fecha_salida, "%Y-%m-%d")
    except ValueError:
        raise ValueError("El parámetro fecha_salida debe estar en el formato 'AAAA-MM-DD'.")

    # Filtrado de la lista de vuelos
    return [vuelo for vuelo in lista_vuelos if vuelo.origen == origen and vuelo.destino == destino and vuelo.fecha_salida == fecha_salida_dt]

# Ejemplo de uso:
# lista_vuelos = [Vuelo(origen='MAD', destino='BCN', fecha_salida=datetime(2023, 8, 1)), ...]
# resultado = buscar_vuelos('MAD', 'BCN', '2023-08-01')
