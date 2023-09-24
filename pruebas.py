#!/usr/bin/python3
import empleados
import plantel
import vendedor
import obreros
import administrativo
def cargar_empleados(arc):
    p = plantel.Plantel()
    archivo = open(arc, "r")
    for linea in archivo.readlines():
        lista = linea.strip().split(";")
        if int(lista[0]) == 2:
            a = administrativo.Administrativo(int(lista[0]), int(lista[1]), lista[2], lista[3], int(lista[4]), True if lista[5] == "true" else False)
            p.agregar(a)
        elif int(lista[0]) == 1:
            o = obreros.Obrero(int(lista[0]), int(lista[1]), lista[2], lista[3], int(lista[4]), int(lista[5]))
            p.agregar(o)
        else:
            v = vendedor.Vendedor(int(lista[0]), int(lista[1]), lista[2], lista[3], int(lista[4]), int(lista[5]))
            p.agregar(v)
    archivo.close()
    return p

def main():
    p = cargar_empleados("DAO-Empleados\empleados.csv")
    print(p.cantidad_tipo())
    print("------------------")
    print(p.total_sueldos())
    print("------------------")
    try:
        legajo = int(input("Ingrese un empleado"))
        emp = p.buscar_empleados(legajo)       
    except KeyError:
            print("No se encuentro el empleado")
    else:
            print("Empleado Encontrado")
            print(emp.neto()) 

    print("----------------")
    p.mostrar_datos()
if __name__ == "__main__":
    main()