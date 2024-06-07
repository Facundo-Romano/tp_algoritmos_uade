import random

#Tipos de vehiculos
vehiculos = [
    'CHICO',
    'MEDIANO',
    'GRANDE',
    'CAMIONETA 4X4',
    'VAN',
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

#Función para obtener el tipo de vehículo del usuario
def obtener_tipo_vehiculo():
    print(" ")
    print("Seleccione el tipo de vehículo:")
    

    for i in range(len(vehiculos)):
        print(f'{i + 1}. {vehiculos[i]}')

    print(" ")
    numero_vehiculo = input("Ingrese número de vehículo a seleccionar: ")

    if (int(numero_vehiculo) <= 0 or int(numero_vehiculo) > len(vehiculos)):
        print(" ")
        print("Número de vehículo incorrecto")
        return obtener_tipo_vehiculo()

    vehiculo = vehiculos[(int(numero_vehiculo) - 1)]

    return vehiculo

#Función para obtener el recorrido en km del usuario
def obtener_kms():
    print(" ")
    kms = input("Ingrese la cantidad de kilometros recorridos con el vehículo: ")

    if (int(kms) < 100 or int(kms) > 5000):
        print(" ")
        print("Cantidad de kilometros incorrecta")
        return obtener_kms()
    
    return int(kms)

#Función para calcular el costo de mantenimiento
def calcular_costo(dato):
    vehiculo = dato[0]
    kms = dato[1]

    for i in range(len(datos_cotizacion)):
        if (datos_cotizacion[i][0] == vehiculo):
            costo = datos_cotizacion[i][1] * kms
            return costo

#Función para calcular la facturación
def calcular_facturacion(dato):
    vehiculo = dato[0]
    kms = dato[1]

    kms_1000_to_3000 = 0
    kms_3000_to_5000 = 0

    if kms > 1000 and kms <= 3000:
        kms_1000_to_3000 = kms - 1000
    elif kms > 3000:
        kms_1000_to_3000 = 2000
        kms_3000_to_5000 = kms - 3000

    for i in range(len(datos_cotizacion)):
        if (datos_cotizacion[i][0] == vehiculo):
            facturacion = 0
            facturacion += datos_cotizacion[i][2]
            facturacion += datos_cotizacion[i][3] * kms_1000_to_3000
            facturacion += datos_cotizacion[i][4] * kms_3000_to_5000
            return facturacion

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

    print("Ingrese los datos del cliente")

    vehiculo = obtener_tipo_vehiculo()

    kms = obtener_kms()

    datos.append([vehiculo, kms])

    return datos

#Función para generar resumen
def generar_resumen(datos):
    print(" ")
    print("Resumen del mes")
    print(" ")

    cantidad_vehiculos = len(datos)
    costos = 0
    facturacion = 0

    for i in range(len(datos)):
        costos += calcular_costo(datos[i])
        facturacion += calcular_facturacion(datos[i])

    print(f'Cantidad de vehículos: {cantidad_vehiculos}')
    print(f'Costos: {costos}')
    print(f'Facturación: {facturacion}')
    print(" ")
    

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
    print(" ")
    print(" ")
    print("Bienvenido a la aplicación de cotización de vehículos")
    print(" ")
    print("Seleccione una opción del menú:")
    print("1. Generar datos del mes")
    print("2. Ingresar datos manuales")
    print("3. Generar resumen del mes")
    print("4. Generar resumen del mes por vehiculo")
    print("5. Generar resumen del mes por cliente")
    print("6. Generar resumen del mes de un vehiculo")
    print("7. Salir")
    print(" ")

    bandera = True

    datos = []

    while (bandera):
        opcion = input("Ingrese una opción del menú: ")

        if opcion == '1':
            print(" ")
            print("Generar datos del mes")
            print(" ")
            datos = generar_datos_aleatorios(200, 450, vehiculos)
            print('Datos generados correctamente')
            print(f'Cantidad de clientes: {len(datos)}')
            print(" ")
        elif opcion == '2':
            print(" ")
            print("Ingresar datos manuales")
            print(" ")
            datos = agregar_datos_manuales(datos)
            print('Datos agregados correctamente')
            print(f'Datos: {datos[len(datos) - 1]}')
            print(" ")
        elif opcion == '3':
            print(" ")
            print("Generar resumen del mes")
            print(" ")
            generar_resumen(datos)
        elif opcion == '4':
            print(" ")
            print("Generar resumen del mes por vehiculo")
            print(" ")
            generar_resumen_por_vehiculo(datos)
        elif opcion == '5':
            print(" ")
            print("Generar resumen del mes por cliente")
            print(" ")
            generar_resumen_por_cliente(datos)
        elif opcion == '6':
            print(" ")
            print("Generar resumen del mes de un vehiculo")
            print(" ")
            generar_resumen_de_vehiculo(datos)
        elif opcion == '7':
            print(" ")
            print("Salir")
            print(" ")
            bandera = False
        elif opcion == '8':
            print(datos)
        else:
            print(" ")
            print("Opción incorrecta")
            print(" ")
            menu()
    
    print(" ")
    print("Gracias por utilizar la aplicación")
    print(" ")

    return


#Inicio de la aplicación
menu()