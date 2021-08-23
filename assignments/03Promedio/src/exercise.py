def main():
    #escribe tu código abajo de esta línea

    # Este programa calculará el promedio de 4 calificaciones
    # Autor: Diego Curiel

    n1 = int(input("Calificación de la materia: "))
    n2 = int(input("Calificación de la materia: "))
    n3 = int(input("Calificación de la materia: "))
    n4 = int(input("Calificación de la materia: "))
    resultado = str(float((n1+n2+n3+n4)/4))
    print ("El promedio es:",resultado)




if __name__ == '__main__':
    main()
