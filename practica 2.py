class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horario = []
    def agregar_horario(self, hora):
        if hora not in self.horario:
            self.horario.append(hora)
        else:
            print("Horario asignado")
class Buses:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horario = []
        self.conductor_asignado = []
    def agregar_ruta(self, ruta):
        self.ruta = ruta
    def registrar_horario(self, horario):
        if horario not in self.horario:
            self.horario.append(horario)
        else:
            print("Horario registrado para el bus")
    def asignar_conductor(self, conductor, horario):
        if horario in self.horario and horario not in conductor.horario:
            self.conductor_asignado.append(conductor)
            conductor.agregar_horario(horario)
        else:
            print("Horario no disponible")
class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    def agregar_bus(self, id_bus):
        bus = Buses(id_bus)
        self.buses.append(bus)
        print(f"Bus con ID {id_bus} agregado exitosamente")
    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
    def mostrar_menu(self):
        while True:
            print("\nMenu: ")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion =='1':
                id_bus = input("Ingrese el ID del bus: ")
                self.agregar_bus(id_bus)
            elif opcion == '2':
                id_bus = input("Ingrese el ID del bus: ")
                ruta = input("Ingrese la ruta: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        bus.agregar_ruta(ruta)
                        break
            elif opcion == '3':
                id_bus = input("Ingrese el ID del bus: ")
                horario = input("Ingrese el horario: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        bus.registrar_horario(horario)
                        break
            elif opcion == '4':
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
            elif opcion == '5':
                nombre = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario: ")
                for conductor in self.conductores:
                    if conductor.nombre == nombre:
                        conductor.agregar_horario(horario)
                        break
            elif opcion =='6':
                id_bus = input("Ingrese el ID del bus: ")
                nombre = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario: ")
                for bus in self.buses:
                    if bus.id_bus == id_bus:
                        for conductor in self.conductores:
                            if conductor.nombre == nombre:
                                bus.asignar_conductor(conductor, horario)
                                break
                        break
            elif opcion =='7':
                print("Fue un gusto!")
                break
            else:
                print("Opción no válida, intente de nuevo")
admin = Admin()
admin.mostrar_menu()
