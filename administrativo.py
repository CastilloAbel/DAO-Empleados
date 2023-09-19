import empleados
class Administrativo(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, presentismo):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.presentismo = presentismo
    