import empleados
class Vendedor(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, importe):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.importe = importe


    def neto(self):
        return self.sueldo + (self.importe * 0.01)
    
    def __str__(self) -> str:
        return super().__str__() + f", Importe: {self.importe}, Sueldo Neto: {self.neto()}"