class Empleado:
    def __init__(self, tipo, legajo, nombre, apellido, sueldo):
        self.tipo = tipo
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
    
    def neto(self):
        return self.sueldo
    
    
    def __str__(self) -> str:
        return f"Tipo: {self.tipo}, Legajo: {self.legajo}, Nombre: {self.nombre}, Apellido: {self.apellido}, Sueldo basico: {self.sueldo}"