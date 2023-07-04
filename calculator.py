from sqlite3 import OperationalError
import sys 
def reiteracion():
    lista = []
    while True:
        absoluto()
        lista.append(resultado)
        print("\n" + str(lista))
        terminar = input("\n\n\nFavor de insertar ´done´ si ya acabaste y ´no´ si no has acabado")
        while terminar != "done" and terminar != "no":
            terminar = input("\n\n\nFavor de insertar ´done´ si ya acabaste y ´no´ si no has acabado")
        if terminar == "done":
            break
        elif terminar == "no":
            continue 
    promedio = average(lista)
    print(promedio)


def average(lista):
    sum_lista = sum(lista)
    len_lista = len(lista)
    average = sum_lista/len_lista
    average = round(average, 2)
    return "\n\n\n\nEl promedio es: " + str(average) + "\n\n\n"




def suma():
    global resultado
    resultado = 1
    lista_suma = []
    while True:
            try: 
                n1 = int(input("\n\nFavor de insertar el número: "))
                print("\n\n")
                lista_suma.append(n1)
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            print("Favor de insertar ´0´ si ya terminaste: ")
            if n1 == 0:
                break 
    resultado = sum(lista_suma)
    resultado  = round(resultado, 2)
    return "La respuesta es: " +str(resultado) + str("\n\n") 





def resta():
    global resultado
    resultado = 1
    while True:
            try: 
                n1 = float(input("Favor de insertar el primer numero: "))
                print("\n\n")
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            break 
    while True: 
            try: 
                n2 = float(input("Favor de insertar el segundo numero: "))
                print("\n\n")
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            break 
     
    resultado = n1-n2
    resultado  = round(resultado, 2)
    return "La respuesta es: " + str(resultado) + str(".\n\n\n")






def multiplicacion():
    global resultado
    resultado = 1
    lista_multi = []
    while True:
            try: 
                n1 = int(input("\n\nFavor de insertar el número: "))
                while n1 == 0:
                    print("Favor de no insertar 0")
                    n1 = int(input("\n\nFavor de insertar el número: "))
                print("\n\n")
                lista_multi.append(n1)
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            print("Favor de insertar ´1´ si ya terminaste: ")
            if n1 == 1:
                break 

    for i in lista_multi:
        resultado *= i
    resultado = round(resultado,2)
    return "La respuesta es: " + str(resultado) + str(".\n\n\n")
    




def division():
    global resultado
    resultado = 1
    while True:
            try: 
                n1 = float(input("Favor de insertar el primer numero: "))
                print("\n\n")
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            break 
    while True: 
            try: 
                n2 = float(input("Favor de insertar el segundo numero: "))
                print("\n\n")
            except(ValueError):
                print("The error was: Insertaste una letra" )
                continue 
            break 
     
    resultado = n1/n2
    resultado  = round(resultado, 2)
    return "La respuesta es: " + str(resultado) + str(".\n\n\n")




def interfaz():
    print("\n\n--------------------------------------------------------------")
    print("\n\nEsta es una calculadora")
    print("\n\nLas opciones son: ") 
    print("\n\nsuma")
    print("\nresta")
    print("\nmultiplicacion")
    print("\ndivision")
    print("\n\n--------------------------------------------------------------")


def absoluto():
    interfaz()
    print("\n\n")
    def inp():
        while True:
            try:
                operacion = input("Favor de insertar la operación: ")
                while operacion != "suma" and operacion != "sumita" and operacion != "resta" and operacion != "multiplicacion" and operacion != "division":
                    operacion = input("\n\nFavor de insertar la operación: ")
            except(ValueError):
                print("The error was: " + str(sys.exc_info()))
                continue 
            break 

        if operacion == "suma" or operacion == "sumita":
            funcion_suma = suma()
            print(funcion_suma)

        elif operacion == "resta":
            funcion_resta = resta()
            print(funcion_resta)

        elif operacion == "multiplicacion":
            funcion_multiplicacion = multiplicacion()
            print(funcion_multiplicacion)

        elif operacion == "division":
            funcion_division = division()
            print(funcion_division)


    inp()


def main():
    reiteracion()


main()


