import empleados
class Obrero(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, dias):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.dias = dias
    