#!/usr/bin/python3
import empleados
import vendedor
import obreros
import administrativo
def cargar_empleados(arc):
    v = []
    archivo = open(arc, "r")
    for linea in archivo.readlines():
        lista = linea.strip().split(";")
        if lista[5] == "false" or lista[5] == "true":
            v.append(administrativo.Administrativo(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], lista[5]))
        elif int(lista [5]) <= 31:
            v.append(obreros.Obrero(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], int(lista[5])))
        else:
            v.append(vendedor.Vendedor(int(lista[0]), int(lista[1]), lista[2], lista[3], lista[4], int(lista[5])))
    archivo.close()
    return v

def main():
    v = cargar_empleados("empleados.csv")
    print(len(v))
if __name__ == "__main__":
    main()