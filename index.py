import random

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

min_clientes = 200
max_clientes = 450
min_kms_recorridos = 100
max_kms_recorridos = 5000

#Tipos de vehiculos
vehiculos = []
for i in range(len(datos_cotizacion)):
    vehiculos.append(datos_cotizacion[i][0])

#Función para obtener el tipo de vehículo del usuario
def obtener_tipo_vehiculo():
    print("\nSeleccione el tipo de vehículo:")

    cantidad_de_tipos = len(vehiculos)

    for i in range(cantidad_de_tipos):
        print(f'{i + 1}. {vehiculos[i]}')

    vehiculo_seleccionado = input("\nIngrese número de vehículo a seleccionar: ")
    numero_vehiculo = int(vehiculo_seleccionado)

    if (numero_vehiculo <= 0 or numero_vehiculo > cantidad_de_tipos):
        print("\nNúmero de vehículo inválido")
        return obtener_tipo_vehiculo()

    vehiculo = vehiculos[(numero_vehiculo - 1)]

    return vehiculo

#Función para obtener el recorrido en km del usuario
def obtener_kms():
    kms = input("\nIngrese la cantidad de kilómetros recorridos con el vehículo: ")

    if (int(kms) < min_kms_recorridos or int(kms) > max_kms_recorridos):
        print("\nCantidad de kilómetros incorrecta")
        return obtener_kms()
    
    return int(kms)

#Función para calcular el costo de mantenimiento
#cliente: [vehiculo, kms_recorridos]
def calcular_costo(cliente):
    vehiculo = cliente[0]
    kms_recorridos = cliente[1]

    for i in range(len(datos_cotizacion)):
        if (datos_cotizacion[i][0] == vehiculo):
            costo = datos_cotizacion[i][1] * kms_recorridos
            return costo

#Función para calcular la facturación
#cliente: [vehiculo, kms_recorridos]
def calcular_facturacion(cliente):
    vehiculo = cliente[0]
    kms_recorridos = cliente[1]

    kms_cotizacion_media = 0
    kms_cotizacion_alta = 0

    if kms_recorridos > 1000 and kms_recorridos <= 3000:
        kms_cotizacion_media = kms_recorridos - 1000
    elif kms_recorridos > 3000:
        kms_cotizacion_media = 3000 - 1000
        kms_cotizacion_alta = kms_recorridos - 3000

    for i in range(len(datos_cotizacion)):
        if (datos_cotizacion[i][0] == vehiculo):
            facturacion = 0
            facturacion += datos_cotizacion[i][2]
            facturacion += datos_cotizacion[i][3] * kms_cotizacion_media
            facturacion += datos_cotizacion[i][4] * kms_cotizacion_alta
            return facturacion

#Función para ordenar descendentemente resumenes de clientes por facturación
#resumen_clientes: [vehiculo, kms_recorridos, costos, facturacion][]
def ordenar_resumen_clientes(resumen_clientes):
    cantidad_clientes = len(resumen_clientes)

    for i in range(cantidad_clientes - 1):
        for j in range(i + 1, cantidad_clientes):
            resumen_cliente_a = resumen_clientes[i]
            resumen_cliente_b = resumen_clientes[j]
            facturacion_a = resumen_cliente_a[3]
            facturacion_b = resumen_cliente_b[3]
            if facturacion_a < facturacion_b:
                resumen_clientes[i] = resumen_cliente_b
                resumen_clientes[j] = resumen_cliente_a

    return resumen_clientes

#Función para generar datos aleatorios
#min: numero
#max: numero
def generar_datos_aleatorios(min, max):
    datos_aleatorios = []

    cantidad_de_datos = random.randint(min, max)

    cantidad_de_tipos = len(vehiculos) - 1

    for _ in range(cantidad_de_datos):
        vehiculo = vehiculos[random.randint(0, cantidad_de_tipos)]
        km_recorridos = random.randint(min_kms_recorridos, max_kms_recorridos)

        datos_aleatorios.append([vehiculo, km_recorridos])

    return datos_aleatorios

#Función para agregar datos manuales
#clientes: [vehiculo, kms_recorridos][]
def agregar_datos_manuales(clientes):
    datos = clientes

    print("Ingrese los datos del cliente")

    vehiculo = obtener_tipo_vehiculo()

    kms = obtener_kms()

    datos.append([vehiculo, kms])

    return datos

#Función para generar resumen
#clientes: [vehiculo, kms_recorridos][]
def generar_resumen(clientes):
    print("\nResumen del mes\n")

    cantidad_vehiculos = len(clientes)
    costos = 0
    facturacion = 0

    for i in range(len(clientes)):
        costos += calcular_costo(clientes[i])
        facturacion += calcular_facturacion(clientes[i])

    print(f'Cantidad de vehículos: {cantidad_vehiculos}')
    print(f'Costos: {costos}')
    print(f'Facturación: {facturacion}\n')

#Función para generar resumen por vehiculo
#clientes: [vehiculo, kms_recorridos][]
def generar_resumen_por_vehiculo(clientes):
    print("\nResumen del mes por vehículo\n")

    cantidad_vehiculos = len(vehiculos)
    resumen_vehiculos = []

    for i in range(cantidad_vehiculos):
        vehiculo = vehiculos[i]
        kms_recorridos = 0
        costos = 0
        facturacion = 0

        for cliente in clientes:
            if cliente[0] == vehiculo:
                kms_recorridos += cliente[1]
                costos += calcular_costo(cliente)
                facturacion += calcular_facturacion(cliente)

        resumen_vehiculos.append([vehiculo, kms_recorridos, costos, facturacion])
    
    resumen_vehiculos = ordenar_resumen_clientes(resumen_vehiculos)

    for i in range(cantidad_vehiculos):
        print(f'Tipo de vehículo: {resumen_vehiculos[i][0]}')
        print(f'Kilómetros recorridos: {resumen_vehiculos[i][1]}')
        print(f'Costos: {resumen_vehiculos[i][2]}')
        print(f'Facturación: {resumen_vehiculos[i][3]}\n')

#Función para generar resumen por cliente
#clientes: [vehiculo, kms_recorridos][]
def generar_resumen_por_cliente(clientes):
    print("\nResumen del mes por cliente\n")

    cantidad_clientes = len(clientes)
    resumen_clientes = []

    for i in range(cantidad_clientes):
        cliente = clientes[i]
        vehiculo = cliente[0]
        kms_recorridos = cliente[1]
        costos = 0
        facturacion = calcular_facturacion(cliente)

        resumen_clientes.append([vehiculo, kms_recorridos, costos, facturacion])
    
    resumen_clientes = ordenar_resumen_clientes(resumen_clientes)

    for i in range(cantidad_clientes):
        print(f'Tipo de vehículo: {resumen_clientes[i][0]}')
        print(f'Facturación: {resumen_clientes[i][3]}\n')
        

#Función para generar resumen de un vehiculo
#clientes: [vehiculo, kms_recorridos][]
def generar_resumen_de_vehiculo(clientes):
    print("Resumen del mes de un vehículo")
    print("\nSeleccione el tipo de vehículo: \n")

    for i in range(len(vehiculos)):
        print(f'{i + 1}. {vehiculos[i]}')

    numero_vehiculo = int(input("\nIngrese número de vehículo a seleccionar: "))

    if (numero_vehiculo <= 0 or numero_vehiculo > len(vehiculos)):
        print("\nNúmero de vehículo incorrecto")
        return generar_resumen_de_vehiculo(clientes)
    
    vehiculo = vehiculos[(numero_vehiculo - 1)]

    cantidad_vehiculos = 0
    costos = 0
    facturacion = 0

    for i in range(len(clientes)):
        if clientes[i][0] == vehiculo:
            cantidad_vehiculos += 1
            costos += calcular_costo(clientes[i])
            facturacion += calcular_facturacion(clientes[i])
        
    print(f'\nCantidad de vehículos: {cantidad_vehiculos}')
    print(f'Costos: {costos}')
    print(f'Facturación: {facturacion}')

#Función para acceder al menu de la aplicación
def menu():
    print("\n\nBienvenido a la aplicación de cotización de vehículos")
    print("\nSeleccione una opción del menú:")
    print("1. Generar datos del mes")
    print("2. Ingresar datos manuales")
    print("3. Generar resumen del mes")
    print("4. Generar resumen del mes por vehiculo")
    print("5. Generar resumen del mes por cliente")
    print("6. Generar resumen del mes de un vehiculo")
    print("7. Salir\n")

    bandera = True

    datos = []

    while (bandera):
        opcion = input("Ingrese una opción del menú: ")

        if opcion == '1':
            print("\nGenerar datos del mes\n")
            datos = generar_datos_aleatorios(min_clientes, max_clientes)
            print('Datos generados correctamente')
            print(f'Cantidad de clientes: {len(datos)}\n')
        elif opcion == '2':
            print("\nIngresar datos manuales\n")
            datos = agregar_datos_manuales(datos)
            print('Datos agregados correctamente')
            print(f'Datos: {datos[len(datos) - 1]}\n')
        elif opcion == '3':
            print("\nGenerar resumen del mes\n")
            generar_resumen(datos)
        elif opcion == '4':
            print("\nGenerar resumen del mes por vehiculo\n")
            generar_resumen_por_vehiculo(datos)
        elif opcion == '5':
            print("\nGenerar resumen del mes por cliente\n")
            generar_resumen_por_cliente(datos)
        elif opcion == '6':
            print("\nGenerar resumen del mes de un vehiculo\n")
            generar_resumen_de_vehiculo(datos)
        elif opcion == '7':
            print("\nSalir")
            bandera = False
        elif opcion == '8':
            print(datos)
        else:
            print("\nOpción incorrecta\n")
            menu()
    
    print("\nGracias por utilizar la aplicación\n")

    return

#Inicio de la aplicación
menu()