# Creamos la clase Componente.
class Componente:

    # Constructor de la clase.
    def __init__(self, codigo, nombre, tipo, marca, stock, ubicacion):

        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock
        self.ubicacion = ubicacion

    # Método que comprueba si existe stock.
    def hay_stock(self):

        if self.stock > 0:
            return True
        else:
            return False

    # Método para mostrar los datos del componente.
    def mostrar_datos(self):

        print("\nCódigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Stock:", self.stock)
        print("Ubicación:", self.ubicacion)


# Creamos los objetos y los guardamos en una lista.
componentes = [

    Componente(101, "Resistencia 220 ohms", "Resistencia", "Genérica", 50, "Estante A"),
    Componente(102, "Capacitor 100uF", "Capacitor", "Samsung", 30, "Estante B"),
    Componente(103, "Arduino Uno", "Placa", "Arduino", 12, "Estante C"),
    Componente(104, "LED rojo", "LED", "Genérico", 100, "Estante A"),
    Componente(105, "Transistor BC547", "Transistor", "NPN", 25, "Estante D"),
    Componente(106, "Arduino Nano", "Placa", "Arduino", 8, "Estante C"),
    Componente(107, "Capacitor 220uF", "Capacitor", "Samsung", 15, "Estante B"),
    Componente(108, "LED verde", "LED", "Genérico", 0, "Estante A"),
    Componente(109, "Resistencia 1K", "Resistencia", "Genérica", 75, "Estante A"),
    Componente(110, "Transistor TIP122", "Transistor", "NPN", 10, "Estante D")

]


# Solicitamos los criterios de búsqueda.
tipo_buscar = input("Ingrese el tipo de componente: ")

stock_minimo = int(input("Ingrese la cantidad mínima de stock: "))

# Contador de componentes que cumplen las condiciones.
cantidad = 0

# Variable auxiliar para guardar el componente con mayor stock.
mayor_stock = None

print("\n========== COMPONENTES ENCONTRADOS ==========")

# Recorremos todos los componentes.
for componente in componentes:

    # Comprobamos el tipo y la cantidad de stock.
    if componente.tipo.lower() == tipo_buscar.lower() and componente.stock >= stock_minimo:

        # Mostramos los datos del componente.
        componente.mostrar_datos()

        # Aumentamos el contador.
        cantidad += 1

        # Comparamos el stock con el mayor encontrado hasta el momento.
        if mayor_stock == None or componente.stock > mayor_stock.stock:

            # Guardamos el objeto con mayor stock.
            mayor_stock = componente


# Mostramos la cantidad de resultados.
print("\nCantidad de componentes encontrados:", cantidad)

# Comprobamos si existen resultados.
if cantidad > 0:

    print("\n========== COMPONENTE CON MAYOR STOCK ==========")

    # Mostramos el componente con mayor cantidad.
    mayor_stock.mostrar_datos()

else:

    print("No existen componentes que cumplan ambas condiciones.")