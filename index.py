import random

#Tipos de vehiculos
vehiculos = [
    'CHICO',
    'MEDIANO',
    'GRANDE',
    'CAMIONETA 4X4',
    'VAN'
]

#Matriz de datos de cotización de vehiculos
#Primera columna: tipo de vehiculo
#Segunda columna: precio mantenimiento por km
#Tercera columna: precio fijo hasta 1000km
#Cuarta columna: precio por km desde 1000km hasta 3000km 
#Quinta columna: precio por km a partir de 3000km
datos_cotizacion = [
    ['CHICO',           0.5,    7500,   550, 600],
    ['MEDIANO',         1.1,    8500,   650, 700],
    ['GRANDE',          2,      9500,   750, 800],
    ['CAMIONETA 4X4',   2.5,    10000,  800, 900],
    ['VAN',             2.8,    12000,  700, 800],
]

#Función para generar datos aleatorios
def cargar_datos_aleatorios(min, max, categorias):
    datos_aleatorios = []

    cantidad_de_datos = random.randint(min, max)

    cantidad_de_categorias = len(categorias) - 1

    for i in range(cantidad_de_datos):
        categoria = categorias[random.randint(0, cantidad_de_categorias)]
        km_recorridos = random.randint(0, 5000)

        datos_aleatorios.append([categoria, km_recorridos])

    return datos_aleatorios


datos = cargar_datos_aleatorios(200, 450, vehiculos)