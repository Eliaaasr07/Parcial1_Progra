# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio

# Clase Servicios Extra  
class ServicioExtra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase Cliente 
class Cliente:
    def __init__(self, nombre, apellido, telf, dui):
        self.nombre = nombre
        self.apellido = apellido
        self.dui = dui
        self.telf = telf
        self.habitacion = None
        self.servicios_extra = []
        self.noche = 0

    def agregar_habitacion(self, habitacion):
        self.habitacion = habitacion

    def agregar_servicio_extra(self, servicio_extra):
        self.servicios_extra.append(servicio_extra)

    def calcular_total(self):
        total = self.habitacion.precio * self.noche
        for servicio_extra in self.servicios_extra:
            total += servicio_extra.precio
        return total

# Clase Recepcionista 
class Recepcionista:
    def __init__(self):
        self.habitaciones = []
        self.servicios_extra = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_servicio_extra(self, servicio_extra):
        self.servicios_extra.append(servicio_extra)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            print(f"Habitación {habitacion.numero}: {habitacion.tipo} - ${habitacion.precio}")

    def mostrar_servicios_extra(self):
        for servicio_extra in self.servicios_extra:
            print(f"{servicio_extra.nombre}: ${servicio_extra.precio}")

    def solicitar_datos_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        telf = input("Ingrese el teléfono del cliente: ")
        dui = input("Ingrese el DUI del cliente: ")
        return Cliente(nombre, apellido, telf, dui)

    def solicitar_noche(self):
        return int(input("Ingrese el número de noches de estadía: "))

    def seleccionar_habitacion(self):
        print("Seleccione el número de la habitación que desea:")
        self.mostrar_habitaciones()
        numero_habitacion = int(input("Ingrese el número de la habitación: "))
        habitacion_seleccionada = next(
            (h for h in self.habitaciones if h.numero == numero_habitacion), None)
        return habitacion_seleccionada

    def seleccionar_servicios_extras(self):
        servicios_seleccionados = []
        while True:
            respuesta = input("¿Desea algún servicio extra? (sí/no): ").lower()
            if respuesta == "sí":
                print("Seleccione el número del servicio extra que desea:")
                for idx, servicio in enumerate(self.servicios_extra, 1):
                    print(f"{idx}. {servicio.nombre} - ${servicio.precio}")
                numero_servicio = int(input("Ingrese el número del servicio extra: "))
                servicio_seleccionado = self.servicios_extra[numero_servicio - 1]
                servicios_seleccionados.append(servicio_seleccionado)
            elif respuesta == "no":
                break
            else:
                print("Respuesta no válida.")
        return servicios_seleccionados

    def entregar_factura(self, cliente):
        print("\n--- Factura ---")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
        print(f"Habitación: {cliente.habitacion.tipo} - ${cliente.habitacion.precio}/noche")
        print(f"Noches: {cliente.noche}")
        if cliente.servicios_extra:
            print("Servicios extras:")
            for servicio in cliente.servicios_extra:
                print(f"- {servicio.nombre}: ${servicio.precio}")
        total = cliente.calcular_total()
        print(f"Total a pagar: ${total}\n")

# Crear instancia del sistema
recepcionista = Recepcionista()

# Agregar habitaciones y servicios extra
habitacion1 = Habitacion(1, "Simple", 100)
habitacion2 = Habitacion(2, "Doble", 150)
recepcionista.agregar_habitacion(habitacion1)
recepcionista.agregar_habitacion(habitacion2)

servicio_extra1 = ServicioExtra("Uso de piscina", 20)
servicio_extra2 = ServicioExtra("Uso de cancha de golf", 30)
recepcionista.agregar_servicio_extra(servicio_extra1)
recepcionista.agregar_servicio_extra(servicio_extra2)

# Mostrar habitaciones y servicios extra
print("Habitaciones disponibles:")
recepcionista.mostrar_habitaciones()
print("Servicios extra disponibles:")
recepcionista.mostrar_servicios_extra()

# Solicitar datos del cliente y número de noches
cliente = recepcionista.solicitar_datos_cliente()
noche = recepcionista.solicitar_noche()
cliente.noche = noche

# Seleccionar habitación y servicios extra
habitacion_seleccionada = recepcionista.seleccionar_habitacion()
cliente.agregar_habitacion(habitacion_seleccionada)

servicios_extras_seleccionados = recepcionista.seleccionar_servicios_extras()
for servicio in servicios_extras_seleccionados:
    cliente.agregar_servicio_extra(servicio)

# Entregar factura
recepcionista.entregar_factura(cliente)
