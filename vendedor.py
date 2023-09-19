import empleados
class Vendedor(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, importe):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.importe = importe
    