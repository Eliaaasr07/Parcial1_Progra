# Clase Vehiculo
class Vehiculo:
    def __init__(self, tipo, marca, modelo, año, costo_renta_diario):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.costo_renta_diario = costo_renta_diario
        self.disponible = True

    def __str__(self):
        return f"{self.tipo} {self.marca} {self.modelo} ({self.año}) - ${self.costo_renta_diario} por día"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

# Clase Renta
class Renta:
    def __init__(self, vehiculo, cliente, dias_renta):
        self.vehiculo = vehiculo
        self.cliente = cliente
        self.dias_renta = dias_renta
        self.costo_total = dias_renta * vehiculo.costo_renta_diario
        vehiculo.disponible = False

    def __str__(self):
        return f"Renta de {self.vehiculo} por {self.dias_renta} días. Cliente: {self.cliente.nombre}. Costo total: ${self.costo_total}"

# Clase EmpresaRenta
class EmpresaRenta:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []
        self.rentas = []

    def agregar_vehiculo(self):
        tipo = input("Ingrese el tipo de vehículo (Auto, Camioneta, Motocicleta, etc.): ")
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        año = int(input("Ingrese el año del vehículo: "))
        costo_renta_diario = float(input("Ingrese el costo de renta diario del vehículo: $"))
        nuevo_vehiculo = Vehiculo(tipo, marca, modelo, año, costo_renta_diario)
        self.vehiculos.append(nuevo_vehiculo)
        print(f"Vehículo {nuevo_vehiculo} agregado al lote.")

    def registrar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ")
        licencia = input("Ingrese la licencia del cliente: ")
        nuevo_cliente = Cliente(nombre, licencia)
        self.clientes.append(nuevo_cliente)
        print(f"Cliente {nombre} registrado con licencia {licencia}.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles para renta:")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(vehiculo)

    def rentar_vehiculo(self):
        tipo = input("Ingrese el tipo de vehículo que desea rentar: ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        dias_renta = int(input("Ingrese el número de días de renta: "))

        cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
        vehiculo = next((v for v in self.vehiculos if v.tipo == tipo and v.disponible), None)

        if cliente and vehiculo:
            nueva_renta = Renta(vehiculo, cliente, dias_renta)
            self.rentas.append(nueva_renta)
            print(f"Renta exitosa: {nueva_renta}")
        else:
            if not cliente:
                print(f"Cliente {nombre_cliente} no está registrado.")
            if not vehiculo:
                print(f"No hay {tipo} disponible para renta.")

    def mostrar_rentas(self):
        print("Rentas actuales:")
        for renta in self.rentas:
            print(renta)

# Ejemplo de uso con entrada de datos del usuario
empresa_renta = EmpresaRenta()

# Agregar vehículos
print("\n--- Registro de Vehículos ---")
agregar_vehiculos = True
while agregar_vehiculos:
    empresa_renta.agregar_vehiculo()
    continuar = input("¿Desea agregar otro vehículo? (s/n): ")
    agregar_vehiculos = continuar.lower() == 's'

# Registrar clientes
print("\n--- Registro de Clientes ---")
registrar_clientes = True
while registrar_clientes:
    empresa_renta.registrar_cliente()
    continuar = input("¿Desea registrar otro cliente? (s/n): ")
    registrar_clientes = continuar.lower() == 's'

# Mostrar vehículos disponibles
empresa_renta.mostrar_vehiculos_disponibles()

# Renta de vehículos
print("\n--- Renta de Vehículos ---")
rentar_vehiculos = True
while rentar_vehiculos:
    empresa_renta.rentar_vehiculo()
    continuar = input("¿Desea realizar otra renta? (s/n): ")
    rentar_vehiculos = continuar.lower() == 's'

# Mostrar las rentas actuales
empresa_renta.mostrar_rentas()