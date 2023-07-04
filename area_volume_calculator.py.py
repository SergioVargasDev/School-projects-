import sys 

#? Always start your program with functions. Have in mind that the path that you need to follow is to have 3 base functions. 
#? First will be about having base functions of a property where you make operations with. Anoher function will be to insert inputs
#? , which will be used in another functions (first functions). Then you will have the third function, which will be about putting 
#? everything in only one function.

def Area_rectangulo(altura, base):
     global resultado
     resultado = altura * base
     print("el área del rectangulo es: " + str(resultado))



def Area_circulo():
     while True:
        try:
            radio = float(input("\n\nFavor de insertar el radio: "))                    
            while radio <= 0: 
                radio = float(input("\n\nFavor de insertar el radio: "))                    
        except(ValueError):
            print("\n\nThe error was: " + str(sys.exc_info()))
            continue 
        break
     area_circulo = 3.1416 * radio**2
     return "\n\nLa área del círculo es: " + str(area_circulo) + "\n\n\n\n\n\n\n\n"



def Volumen_rectangulo():
       while True:
                 try:
                     base = float(input("\n\nFavor de insertar la base del rectángulo: "))
                     while base <= 0: 
                         base = float(input("\n\nFavor de insertar la base del rectángulo: "))
                 except(ValueError):
                    print("\n\nThe error was: " + str(sys.exc_info()))
                    continue 
                 break
             
       while True:
                 try:
                  altura = float(input("\n\nFavor de insertar la altura del rectángulo: "))
                  while altura <= 0: 
                    altura = float(input("\n\nFavor de insertar la altura del rectángulo: "))
                 except(ValueError):
                    print("\n\nThe error was: " + str(sys.exc_info()))
                    continue 
                 break
             
              
       while True:
                 try:
                  ancho = float(input("\n\nFavor de insertar el ancho del rectángulo: "))
                  while altura <= 0: 
                    ancho = float(input("\n\nFavor de insertar el ancho del rectángulo: "))
                 except(ValueError):
                     print("\n\nThe error was: " + str(sys.exc_info()))
                     continue 
                 break
       
       volumen_rectangulo = base * altura * ancho
       return volumen_rectangulo 


def Volumen_circulo():
    while True:
                 try:
                    radio = float(input("\n\nFavor de insertar el radio: "))                    
                    while radio <= 0: 
                         radio = float(input("\n\nFavor de insertar el radio: "))
                 except(ValueError):
                    print("\n\nThe error was: " + str(sys.exc_info()))
                    continue 
                 break
    volumen_circulo = 4/3 * 3.1416 * radio
    return volumen_circulo

    


def lista(area_rectangulo):
    lista = []
    lista.append(area_rectangulo)
    print(lista)


def inputs():
    pregunta = input("\n\nFavor de insertar si será Rectángulo o Círculo: ")
    #? Here the while loop will be used when you want that the user can´t put inputs which aren´t the type required. In this case the while loop will
    #? be the only thing you need to, because the input can be any type. Also remember that if you want that the input can accept limmited things,
    #? you will have to use "!=" and the logic "and" operator.
    while pregunta != "Rectángulo" and pregunta != "rectángulo" and pregunta != "Rectangulo" and pregunta != "rectangulo" and pregunta != "Círculo" and pregunta != "círculo" and pregunta != "Circulo" and pregunta != "circulo":
       pregunta = input("\n\nFavor de insertar si será Rectángulo o Círculo: ")
    if pregunta == "Rectángulo" or pregunta == "rectángulo" or pregunta == "Rectangulo" or pregunta == "rectangulo":
        pregunta_2 = input("\n\nFavor de insertar si querrás sacar el área o el volumen: ")
        while pregunta_2 != "Área" and pregunta_2 != "área" and pregunta_2 != "Area" and pregunta_2 != "area" and pregunta_2 != "Volumen" and pregunta_2 != "volumen":
           pregunta_2 = input("\n\nFavor de insertar si querrás sacar el área o el volumen: ")            
        if pregunta_2 == "Área" or pregunta_2 == "área" or pregunta_2 == "Area" or pregunta_2 == "area":
        

             #? If the input can´t have multiple types, you´ll have to use the "try"/"except" functions. Which
             #? will be based in using a "while True" Whose main function is that the "while" is infinite. Then you will use the 
             #? "while" function in the "try" function  and then you´ll put the except function with the name of the error function. Afterwards in the 
             #? same identation you´ll put the "print("\n\nThe error was: " + str(sys.exc_info()))" and below you will insert the continue function which 
             #? will go again to the "while" loop. To finish just put a "break" function in the same identation as the except function. 

            while True:
                 try:
                     base = float(input("\n\nFavor de insertar la base del rectángulo: "))
                     while base <= 0: 
                         base = float(input("\n\nFavor de insertar la base del rectángulo: "))
                 except(ValueError):
                     print("\n\nThe error was: " + str(sys.exc_info()))
                     continue 
                 break
             
            while True:
                 try:
                  altura = float(input("\n\nFavor de insertar la altura del rectángulo: "))
                  while altura <= 0: 
                    altura = float(input("\n\nFavor de insertar la altura del rectángulo: "))
                 except(ValueError):
                    print("\n\nThe error was: " + str(sys.exc_info()))
                    continue 
                 break
             

            Area_rectangulo(base, altura)
        
    

        elif pregunta_2 == "Volumen" or pregunta_2 == "volumen":
            vol1 = Volumen_rectangulo()
            print("\n\nEl volumen del rectangulo es: " + str(vol1) + "\n\n\n\n\n\n\n\n")
        
            
    

          
                     
    elif pregunta == "Círculo" or pregunta == "círculo" or pregunta == "Circulo" or pregunta == "circulo":
        pregunta_2 = input("\n\nFavor de insertar si querrás sacar el área o el volumen: ")
        while pregunta_2 != "Área" and pregunta_2 != "área" and pregunta_2 != "Area" and pregunta_2 != "area" and pregunta_2 != "Volumen" and pregunta_2 != "volumen":
           pregunta_2 = input("\n\nFavor de insertar si querrás sacar el área o el volumen: ")           


        if pregunta_2 == "Área" or pregunta_2 == "área" or pregunta_2 == "Area" or pregunta_2 == "area":
            area2 = Area_circulo()
            print(area2)

           

        elif pregunta_2 == "Volumen" or pregunta_2 == "volumen":
             vol2 = Volumen_circulo()
             print(vol2)

        
             
#? Now that you´ve finished. You can use the whole function in another function so you can call it. 
def main():
    lista = []
    while True: 
        print("\n\nEste es un programa que otorga áreas y volúmenes de rectángulos y círculos")
        inputs()
        lista.append(resultado)
        pregunta = input("")
        if pregunta == "si":
             continue
        elif pregunta =="no":
             break 
        print(lista)
  
       

 
        
    
main()