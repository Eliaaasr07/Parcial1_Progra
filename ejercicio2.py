from datetime import datetime, timedelta
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

    def __str__(self):
        return f"Libro: {self.titulo} - {'Disponible' if self.disponible else 'No disponible'}"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Prestamo:
    def __init__(self, libro, usuario, fecha_retiro, dias_prestamo=14):
        self.libro = libro
        self.usuario = usuario
        self.fecha_retiro = fecha_retiro
        self.fecha_limite = fecha_retiro + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None
        libro.disponible = False

    def devolver_libro(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        self.libro.disponible = True
        if self.fecha_devolucion > self.fecha_limite:
            dias_tarde = (self.fecha_devolucion - self.fecha_limite).days
            print(f"Libro devuelto tarde por {dias_tarde} días. Se aplica una sanción.")
        else:
            print("Libro devuelto a tiempo.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        nuevo_libro = Libro(titulo)
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado a la biblioteca.")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre del usuario: ")
        nuevo_usuario = Usuario(nombre)
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario '{nombre}' registrado en la biblioteca.")

    def prestar_libro(self):
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        titulo_libro = input("Ingrese el título del libro: ")
        fecha_retiro_str = input("Ingrese la fecha de retiro (YYYY-MM-DD): ")
        fecha_retiro = datetime.strptime(fecha_retiro_str, "%Y-%m-%d")

        usuario = next((u for u in self.usuarios if u.nombre == nombre_usuario), None)
        libro = next((l for l in self.libros if l.titulo == titulo_libro and l.disponible), None)

        if usuario and libro:
            nuevo_prestamo = Prestamo(libro, usuario, fecha_retiro)
            self.prestamos.append(nuevo_prestamo)
            print(f"Préstamo registrado: '{libro.titulo}' prestado a {usuario.nombre}. Fecha límite: {nuevo_prestamo.fecha_limite}.")
        else:
            if not usuario:
                print(f"Usuario '{nombre_usuario}' no está registrado.")
            if not libro:
                print(f"El libro '{titulo_libro}' no está disponible o no existe.")

    def devolver_libro(self):
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        titulo_libro = input("Ingrese el título del libro: ")
        fecha_devolucion_str = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
        fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%Y-%m-%d")

        prestamo = next((p for p in self.prestamos if p.libro.titulo == titulo_libro and p.usuario.nombre == nombre_usuario and not p.fecha_devolucion), None)

        if prestamo:
            prestamo.devolver_libro(fecha_devolucion)
        else:
            print(f"No se encontró un préstamo activo para el libro '{titulo_libro}' del usuario '{nombre_usuario}'.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for libro in self.libros:
            print(libro)

biblioteca = Biblioteca()

print("\n--- Registro de Libros ---")
agregar_libros = True
while agregar_libros:
    biblioteca.agregar_libro()
    continuar = input("¿Desea agregar otro libro? (s/n): ")
    agregar_libros = continuar.lower() == 's'

print("\n--- Registro de Usuarios ---")
registrar_usuarios = True
while registrar_usuarios:
    biblioteca.registrar_usuario()
    continuar = input("¿Desea registrar otro usuario? (s/n): ")
    registrar_usuarios = continuar.lower() == 's'

biblioteca.mostrar_libros()

print("\n--- Préstamo de Libros ---")
prestar_libros = True
while prestar_libros:
    biblioteca.prestar_libro()
    continuar = input("¿Desea registrar otro préstamo? (s/n): ")
    prestar_libros = continuar.lower() == 's'

print("\n--- Devolución de Libros ---")
devolver_libros = True
while devolver_libros:
    biblioteca.devolver_libro()
    continuar = input("¿Desea registrar otra devolución? (s/n): ")
    devolver_libros = continuar.lower() == 's'
