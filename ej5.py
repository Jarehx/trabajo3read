# Creamos la clase Reparacion.
class Reparacion:

    # Constructor de la clase.
    def __init__(self, orden, cliente, equipo, falla, estado, tecnico, costo_estimado):

        self.orden = orden
        self.cliente = cliente
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado

    # Método para mostrar todos los datos de la reparación.
    def mostrar_datos(self):

        print("\nNúmero de orden:", self.orden)
        print("Cliente:", self.cliente)
        print("Equipo:", self.equipo)
        print("Falla:", self.falla)
        print("Estado:", self.estado)
        print("Técnico:", self.tecnico)
        print("Costo estimado: $", self.costo_estimado)


# Creamos los objetos y los almacenamos en una lista.
reparaciones = [

    Reparacion(101, "Juan Perez", "Notebook", "No enciende", "Pendiente", "Carlos", 45000),
    Reparacion(102, "Maria Lopez", "PC", "Problema de RAM", "En reparación", "Pedro", 30000),
    Reparacion(103, "Pedro Gomez", "Monitor", "Pantalla dañada", "Finalizada", "Carlos", 60000),
    Reparacion(104, "Ana Torres", "Notebook", "Batería defectuosa", "Pendiente", "Lucas", 25000),
    Reparacion(105, "Lucas Diaz", "PC", "Problema de fuente", "En reparación", "Pedro", 35000),
    Reparacion(106, "Sofia Ruiz", "Impresora", "No imprime", "Finalizada", "Lucas", 20000),
    Reparacion(107, "Mateo Silva", "Notebook", "Disco dañado", "Pendiente", "Carlos", 55000),
    Reparacion(108, "Camila Rios", "PC", "Sobrecalentamiento", "En reparación", "Pedro", 40000),
    Reparacion(109, "Martin Diaz", "Monitor", "Sin imagen", "Finalizada", "Lucas", 30000),
    Reparacion(110, "Lucia Perez", "Notebook", "Problema de teclado", "Pendiente", "Carlos", 15000)

]


# Función que busca una reparación por número de orden.
def buscar_por_orden(numero):

    # Recorremos todas las reparaciones.
    for reparacion in reparaciones:

        # Comprobamos si el número de orden coincide.
        if reparacion.orden == numero:

            # Devolvemos el objeto encontrado.
            return reparacion

    # Si no encontramos la reparación, devolvemos None.
    return None


# Función que filtra las reparaciones por estado.
def filtrar_por_estado(estado):

    # Contador de resultados.
    cantidad = 0

    print("\n========== REPARACIONES POR ESTADO ==========")

    # Recorremos todas las reparaciones.
    for reparacion in reparaciones:

        # Comparamos el estado ignorando mayúsculas y minúsculas.
        if reparacion.estado.lower() == estado.lower():

            # Mostramos los datos.
            reparacion.mostrar_datos()

            cantidad += 1

    # Comprobamos si hubo resultados.
    if cantidad == 0:

        print("No existen reparaciones con ese estado.")


# Función que filtra las reparaciones por técnico.
def filtrar_por_tecnico(tecnico):

    # Contador de resultados.
    cantidad = 0

    print("\n========== REPARACIONES POR TÉCNICO ==========")

    # Recorremos las reparaciones.
    for reparacion in reparaciones:

        # Comprobamos si el técnico coincide.
        if reparacion.tecnico.lower() == tecnico.lower():

            reparacion.mostrar_datos()

            cantidad += 1

    # Si no encontramos resultados, mostramos un mensaje.
    if cantidad == 0:

        print("No existen reparaciones asignadas a ese técnico.")


# Función que filtra las reparaciones por costo.
def filtrar_por_costo(limite):

    # Contador de resultados.
    cantidad = 0

    print("\n========== REPARACIONES POR COSTO ==========")

    # Recorremos todas las reparaciones.
    for reparacion in reparaciones:

        # Comprobamos si el costo es menor o igual al límite.
        if reparacion.costo_estimado <= limite:

            reparacion.mostrar_datos()

            cantidad += 1

    # Comprobamos si hubo resultados.
    if cantidad == 0:

        print("No existen reparaciones dentro de ese costo.")


# Función que muestra todas las reparaciones.
def mostrar_todas():

    print("\n========== TODAS LAS REPARACIONES ==========")

    # Recorremos la lista y mostramos cada objeto.
    for reparacion in reparaciones:

        reparacion.mostrar_datos()


# Menú principal del programa.

# Inicializamos la opción.
opcion = 0

# El menú continúa funcionando mientras no se seleccione salir.
while opcion != 6:

    print("\n========== SERVICIO TÉCNICO ==========")
    print("1. Mostrar todas las reparaciones")
    print("2. Buscar por número de orden")
    print("3. Filtrar por estado")
    print("4. Filtrar por técnico")
    print("5. Filtrar por costo")
    print("6. Salir")

    # Solicitamos una opción al usuario.
    opcion = int(input("\nSeleccione una opción: "))

    # Opción 1: mostrar todas las reparaciones.
    if opcion == 1:

        mostrar_todas()

    # Opción 2: buscar una reparación específica.
    elif opcion == 2:

        numero = int(input("Ingrese el número de orden: "))

        # Guardamos el resultado de la búsqueda.
        resultado = buscar_por_orden(numero)

        # Comprobamos si existe la reparación.
        if resultado != None:

            print("\n========== REPARACIÓN ENCONTRADA ==========")

            resultado.mostrar_datos()

        else:

            print("No se encontró ninguna reparación con ese número.")

    # Opción 3: filtrar por estado.
    elif opcion == 3:

        estado = input("Ingrese el estado de la reparación: ")

        filtrar_por_estado(estado)

    # Opción 4: filtrar por técnico.
    elif opcion == 4:

        tecnico = input("Ingrese el nombre del técnico: ")

        filtrar_por_tecnico(tecnico)

    # Opción 5: filtrar por costo.
    elif opcion == 5:

        costo = float(input("Ingrese el costo máximo: $"))

        filtrar_por_costo(costo)

    # Opción 6: salir del programa.
    elif opcion == 6:

        print("Saliendo del sistema de consultas...")

    # Si se ingresa una opción incorrecta.
    else:

        print("Opción inválida. Intente nuevamente.")