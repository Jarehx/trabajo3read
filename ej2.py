# Creamos la clase RecursoDigital.
class RecursoDigital:

    # Constructor de la clase.
    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):

        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    # Método que muestra un resumen del recurso.
    def mostrar_resumen(self):

        print("\nCódigo:", self.codigo)
        print("Título:", self.titulo)
        print("Categoría:", self.categoria)

        # Comprobamos si el recurso está disponible.
        if self.disponible:
            print("Disponibilidad: Disponible")
        else:
            print("Disponibilidad: No disponible")


# Creamos los objetos de la biblioteca.
recursos = [

    RecursoDigital(101, "Introducción a Python", "Libro digital", "Juan Perez", 2022, True),
    RecursoDigital(102, "Programación con Python avanzado", "Tutorial", "Maria Lopez", 2023, True),
    RecursoDigital(103, "Manual de HTML y CSS", "Manual", "Pedro Gomez", 2021, False),
    RecursoDigital(104, "Historia de la informática", "Libro digital", "Ana Torres", 2020, True),
    RecursoDigital(105, "Python desde cero", "Video educativo", "Lucas Diaz", 2024, True),
    RecursoDigital(106, "Revista de tecnología", "Revista", "Sofia Ruiz", 2022, False),
    RecursoDigital(107, "Redes informáticas básicas", "Manual", "Mateo Silva", 2019, True),
    RecursoDigital(108, "Introducción a las bases de datos", "Libro digital", "Camila Rios", 2023, True),
    RecursoDigital(109, "Tutorial de Java", "Tutorial", "Martin Diaz", 2021, False),
    RecursoDigital(110, "Python para principiantes", "Video educativo", "Lucia Perez", 2024, True)

]


# Solicitamos el texto que se desea buscar.
busqueda = input("Ingrese una palabra o parte del título: ").lower()

# Contadores de resultados.
total_coincidencias = 0
disponibles = 0

print("\n========== RESULTADOS DE BÚSQUEDA ==========")

# Recorremos todos los recursos.
for recurso in recursos:

    # Convertimos el título a minúsculas.
    titulo = recurso.titulo.lower()

    # Comprobamos si el texto ingresado aparece en el título.
    if busqueda in titulo:

        # Mostramos el resumen del recurso encontrado.
        recurso.mostrar_resumen()

        # Contamos las coincidencias.
        total_coincidencias += 1

        # Comprobamos si el recurso está disponible.
        if recurso.disponible:

            print("Este recurso se encuentra disponible.")

            disponibles += 1

        else:

            print("Este recurso no se encuentra disponible.")


# Mostramos el resumen de la búsqueda.
print("\n========== RESUMEN ==========")

print("Total de coincidencias:", total_coincidencias)
print("Recursos disponibles:", disponibles)

# Comprobamos si hubo resultados.
if total_coincidencias == 0:

    print("La búsqueda no produjo resultados.")