# Creamos la clase Videojuego.
class Videojuego:

    # Constructor de la clase.
    def __init__(self, codigo, titulo, genero, plataforma, anio, horas_estimadas):

        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas

    # Método para mostrar todos los datos del videojuego.
    def mostrar_datos(self):

        print("\nCódigo:", self.codigo)
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("Plataforma:", self.plataforma)
        print("Año:", self.anio)
        print("Horas estimadas:", self.horas_estimadas)

    # Método que comprueba si el género coincide.
    def es_del_genero(self, genero):

        return self.genero.lower() == genero.lower()

    # Método que comprueba si supera una cantidad de horas.
    def supera_horas(self, cantidad):

        return self.horas_estimadas > cantidad


# Creamos los objetos y los almacenamos en una lista.
videojuegos = [

    Videojuego(101, "Minecraft", "Sandbox", "PC", 2011, 80),
    Videojuego(102, "GTA V", "Acción", "PC", 2013, 50),
    Videojuego(103, "The Witcher 3", "RPG", "PC", 2015, 100),
    Videojuego(104, "Resident Evil 4", "Terror", "PlayStation", 2023, 20),
    Videojuego(105, "FIFA 24", "Deportes", "PC", 2023, 40),
    Videojuego(106, "Cyberpunk 2077", "RPG", "PC", 2020, 60),
    Videojuego(107, "God of War", "Acción", "PlayStation", 2018, 25),
    Videojuego(108, "Stardew Valley", "Simulación", "PC", 2016, 55)

]


# Función para buscar un videojuego por código.
def buscar_por_codigo(codigo):

    # Recorremos la lista.
    for videojuego in videojuegos:

        # Comprobamos si el código coincide.
        if videojuego.codigo == codigo:

            # Devolvemos el objeto encontrado.
            return videojuego

    # Si no encontramos coincidencias, devolvemos None.
    return None


# Primera consulta: buscar por género.
genero_buscar = input("Ingrese el género que desea consultar: ")

# Contador de resultados.
cantidad_genero = 0

print("\n========== VIDEOJUEGOS POR GÉNERO ==========")

# Recorremos todos los videojuegos.
for videojuego in videojuegos:

    # Utilizamos el método de la clase para comprobar el género.
    if videojuego.es_del_genero(genero_buscar):

        videojuego.mostrar_datos()

        cantidad_genero += 1


# Comprobamos si hubo resultados.
if cantidad_genero == 0:

    print("No existen videojuegos de ese género.")


# Segunda consulta: buscar por duración.
horas = float(input("\nIngrese una cantidad de horas: "))

# Contador de resultados.
cantidad_horas = 0

print("\n========== VIDEOJUEGOS QUE SUPERAN LAS HORAS ==========")

# Recorremos nuevamente la lista.
for videojuego in videojuegos:

    # Utilizamos el método para comprobar la duración.
    if videojuego.supera_horas(horas):

        videojuego.mostrar_datos()

        cantidad_horas += 1


# Comprobamos si hubo resultados.
if cantidad_horas == 0:

    print("No existen videojuegos que superen esa cantidad de horas.")


# Tercera consulta: búsqueda por código.
codigo = int(input("\nIngrese el código del videojuego: "))

# Guardamos el resultado de la función.
resultado = buscar_por_codigo(codigo)

# Comprobamos si encontramos el videojuego.
if resultado != None:

    print("\n========== VIDEOJUEGO ENCONTRADO ==========")

    resultado.mostrar_datos()

else:

    print("No se encontró ningún videojuego con ese código.")