# Creamos la clase TicketSoporte.
class TicketSoporte:

    # Constructor: inicializa los atributos de cada ticket.
    def __init__(self, numero, usuario, sector, problema, prioridad, estado):

        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado

    # Método para mostrar todos los datos del ticket.
    def mostrar_datos(self):

        print("\nNúmero:", self.numero)
        print("Usuario:", self.usuario)
        print("Sector:", self.sector)
        print("Problema:", self.problema)
        print("Prioridad:", self.prioridad)
        print("Estado:", self.estado)


# Creamos los objetos y los almacenamos en una lista.
tickets = [

    TicketSoporte(101, "Juan", "Informática", "PC no enciende", "Alta", "Pendiente"),
    TicketSoporte(102, "Maria", "Administración", "Problema con impresora", "Media", "Resuelto"),
    TicketSoporte(103, "Pedro", "Biblioteca", "Error de conexión", "Alta", "Pendiente"),
    TicketSoporte(104, "Sofia", "Dirección", "Problema con teclado", "Baja", "En proceso"),
    TicketSoporte(105, "Lucas", "Informática", "Falla de monitor", "Media", "Pendiente"),
    TicketSoporte(106, "Camila", "Secretaría", "Problema de internet", "Alta", "Resuelto"),
    TicketSoporte(107, "Mateo", "Biblioteca", "PC lenta", "Baja", "Pendiente"),
    TicketSoporte(108, "Valentina", "Administración", "Error de sistema", "Media", "En proceso")

]


# Función que busca un ticket por su número.
def buscar_ticket(numero):

    # Recorremos la lista de tickets.
    for ticket in tickets:

        # Comprobamos si el número coincide.
        if ticket.numero == numero:

            # Devolvemos el objeto encontrado.
            return ticket

    # Si termina el recorrido sin encontrarlo, devolvemos None.
    return None


# Solicitamos el número de ticket.
numero = int(input("Ingrese el número de ticket que desea buscar: "))

# Guardamos el resultado de la búsqueda.
resultado = buscar_ticket(numero)


# Comprobamos si encontramos el ticket.
if resultado != None:

    print("\n--- TICKET ENCONTRADO ---")

    # Utilizamos el método del objeto para mostrar sus datos.
    resultado.mostrar_datos()

else:

    # Este mensaje aparece una sola vez si no existe el ticket.
    print("Ticket no encontrado.")


# Segunda consulta: mostrar solamente los tickets pendientes.
print("\n========== TICKETS PENDIENTES ==========")

# Contador de tickets pendientes.
cantidad_pendientes = 0

# Recorremos nuevamente la lista.
for ticket in tickets:

    # Comprobamos si el estado es Pendiente.
    if ticket.estado == "Pendiente":

        # Mostramos los datos del ticket.
        ticket.mostrar_datos()

        # Aumentamos el contador.
        cantidad_pendientes += 1


# Mostramos la cantidad total de tickets pendientes.
print("\nCantidad de tickets pendientes:", cantidad_pendientes)

# Si no hay tickets pendientes, informamos.
if cantidad_pendientes == 0:

    print("No existen tickets pendientes.")