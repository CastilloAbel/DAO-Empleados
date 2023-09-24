import empleados
import administrativo
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
    
    def buscar_empleados(self, legajo):
        return self.empleados[legajo]
    

    def mostrar_datos(self):
        for e in self.empleados.values():
            print(e)
