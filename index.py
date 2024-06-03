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
#Segunda columna: costo mantenimiento por km
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
def generar_datos_aleatorios(min, max, categorias):
    datos_aleatorios = []

    cantidad_de_datos = random.randint(min, max)

    cantidad_de_categorias = len(categorias) - 1

    for i in range(cantidad_de_datos):
        categoria = categorias[random.randint(0, cantidad_de_categorias)]
        km_recorridos = random.randint(100, 5000)

        datos_aleatorios.append([categoria, km_recorridos])

    return datos_aleatorios

#Función para agregar datos manuales
def agregar_datos_manuales(datosIniciales):
    datos = datosIniciales

    #Agregar lógica

    return datos

#Función para generar resumen
def generar_resumen(datos):
    #Agregar lógica
    return datos

#Función para generar resumen por vehiculo
def generar_resumen_por_vehiculo(datos):
    #Agregar lógica
    return datos

#Función para generar resumen por cliente
def generar_resumen_por_cliente(datos):
    #Agregar lógica
    return datos

#Función para generar resumen de un vehiculo
def generar_resumen_de_vehiculo(datos):
    #Agregar lógica
    return datos

#Función para acceder al menu de la aplicación
def menu():
    print("Bienvenido a la aplicación de cotización de vehículos")
    print("Seleccione una opción:")
    print("1. Generar datos del mes")
    print("2. Ingresar datos manuales")
    print("3. Generar resumen del mes")
    print("4. Generar resumen del mes por vehiculo")
    print("5. Generar resumen del mes por cliente")
    print("6. Generar resumen del mes de un vehiculo")
    print("7. Salir")

    bandera = True

    datos = []

    while (bandera):
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            datos = generar_datos_aleatorios(200, 450, vehiculos)
            print('Datos generados correctamente')
            print(f'Cantidad de clientes: {len(datos)}')
        elif opcion == '2':
            datos = agregar_datos_manuales(datos)
            print('Datos agregados correctamente')
            print(f'Datos: {datos[len(datos) - 1]}')
        elif opcion == '3':
            generar_resumen(datos)
        elif opcion == '4':
            generar_resumen_por_vehiculo(datos)
        elif opcion == '5':
            generar_resumen_por_cliente(datos)
        elif opcion == '6':
            generar_resumen_de_vehiculo(datos)
        elif opcion == '7':
            bandera = False
        else:
            print("Opción incorrecta")
            menu()
    
    print("Gracias por utilizar la aplicación")

    return


#Inicio de la aplicación
menu()