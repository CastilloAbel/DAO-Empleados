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
        if lista[5] == "false" or lista[5] == "true":
            a = administrativo.Administrativo(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], bool(lista[5]))
            p.agregar(a)
        elif int(lista [5]) <= 31:
            o = obreros.Obrero(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], int(lista[5]))
            p.agregar(o)
        else:
            v = vendedor.Vendedor(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], int(lista[5]))
            p.agregar(v)
    archivo.close()
    return p

def main():
    p = cargar_empleados("empleados.csv")
    print(p.cantidad_tipo())
if __name__ == "__main__":
    main()