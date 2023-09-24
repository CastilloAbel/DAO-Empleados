import empleados
class Administrativo(empleados.Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo, presentismo):
        super().__init__(tipo, legajo, nombre, apellido, sueldo)
        self.presentismo = presentismo

    def neto(self):
        return (self.sueldo * 1.13 if self.presentismo else self.sueldo)
    
    def __str__(self) -> str:
        return super().__str__() + f", Presentismo: {self.presentismo}, Sueldo Neto: {self.neto()}"