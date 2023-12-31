import empleados
class Obrero(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, dias):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.dias = dias
    def neto(self):
        return self.sueldo / 20 * self.dias
    
    def __str__(self) -> str:
        return super().__str__() + f", Dias: {self.dias}, Sueldo Neto: {self.neto()}"