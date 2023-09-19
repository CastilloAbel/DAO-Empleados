import empleados
import obreros
import administrativo
import vendedor
class Plantel:
    def __init__(self):
        self.empleados = dict()
        
    def agregar(self, nuevo:empleados.Empleado):
        self.empleados[nuevo.legajo] = nuevo
    
    def total_sueldos(self):
        return sum(list(map(lambda e: e.neto(), self.empleados.values())))
    
    def cantidad_tipo(self):
        c = {"Obrero":0, "Administrativo":0, "Vendedor":0}
        for e in self.empleados.values():
            tipo = e.__class__.__name__
            c[tipo] += 1
        return c