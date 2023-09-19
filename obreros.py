import empleados
class Obrero(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, dias):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.dias = dias
    def neto(self):
        return self.sueldo / 20 * self.dias