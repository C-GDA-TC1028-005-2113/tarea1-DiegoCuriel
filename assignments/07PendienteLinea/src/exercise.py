def main():
    #escribe tu código abajo de esta línea
    # Este es un programa que calcula la pendiente de una linea
    # Autor: Diego Curiel

    x1 = float(input ("Dame x1: "))
    y1 = float(input ("Dame y1: "))

    x2 = float(input ("Dame x2: "))
    y2 = float(input ("Dame y2: "))

    resultado = str((y2 - y1)/(x2 - x1))

    print ("Pendiente:", resultado)




if __name__ == '__main__':
    main()
