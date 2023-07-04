#Algoritmo:

#Tengo que elegir dos temas para dos diferentes quizzes. Deben de ser absolutamente relativos a mi carrera.

#Primer quiz: Las preguntas serán relativas a comandos de programación. 

#Segundo quiz: Las preguntas serán relativas a operadores matemáticos en programación

 

#Aquí se importaron las funciones de respuestas correctas e incorrectas de un archivo que contiene las funciones utilizadas en el programa

from Funciones import resp_correct, resp_incorrect
import re
#Sistema de puntuaje 

#Esta función lo que realiza es realizar un promedio de lo que está dentro de una lista. Posteriormente arroja el promedio.
def average():
  sum_lista1_0 = sum(lista1_0)
  cantidad_lista1_0 = len(lista1_0)
  global average
  average = sum_lista1_0/cantidad_lista1_0
  global average_round
  average_round = round(average, 2)
  print("\n\nEl promedio de los quizzes fue de: " + str(average_round) + ". ")
  if average_round == 100:
    print("\n\nHas aprobado con una nota de excelencia\n\n")
  elif average_round > 89 and average_round < 100:
    print("\n\nHas aprobado con una nota excelente\n\n")
  elif average_round >80 and average_round < 89:
    print("\n\nHas aprobado con una nota buena\n\n")
  elif average_round > 69 and average_round < 80:
    print("\n\nHas aprobado\n\n")
  else:
    print("\n\nHas reprobado\n\n")

#Esta función propicia que tú tengas la potestad de elegir cuántas veces se repetirá el quiz. 
def reiteracion():
  #Primero empezamos definiendo los contadores y las listas a usar
  global contador1
  contador1 = 0
  global lista1
  lista1 = []
  global lista1_0
  lista1_0 = []
  global x 
  #Aquí se pregunta cuántas veces se repetirá el quiz
  x = int(input("\nFavor de insertar la cantidad de veces a realizar el quiz: "))
  while x <= 0:
    x = int(input("\nFavor de insertar la cantidad de veces a realizar el quiz: "))
  while contador1 < x:
    #En base al contador, se iterará en base al rango que se estipulé
    for contador1 in range(x):
      #Si se está dentro de la secuencia, se mandará a llamar la función de preguntas 
      pregunta_dicotómica()
      lista1_0 = lista1_0 + [resultado_porcentaje1]
      lista1 = lista1 + [resultado_porcentaje1]
      contador1 = contador1 + 1

    print("\n-------------Lista de Quizzes--------------")
    print("\n\n" + str(lista1_0 ) + ". ")
    search_text = "\n"
    replace_text = ""
    with open(r'archivo_texto.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open(r'archivo_texto.txt', 'w') as file:
       file.write(data)
    average()
    print(data)
    




#Esta es la función de sistema de puntos que captura todas las respuestas correctas e incorrectas y posteriormente saca el resultado, el cual es devuelto por el return hasta el fin el quiz
def sis_puntos1 ():
  print("\n\n-------------Has finalizado el Quiz--------------")
  print("\n\nEstos son tus aciertos y deshaciertos de tu quiz: ")
  # Sistema para otorgar calificación de 0-100.  
  print("\n\nTus aciertos son: " + str(resp_correcta)) 
  print("\n\nTus deshaciertos son: " + str(resp_incorrecta))
  global resultado_porcentaje1
  resultado_porcentaje1 = resp_correcta/10*100
  return resultado_porcentaje1


  
#Pregunta acerca si iniciar el sistema

  
def pregunta_dicotómica():
  print("\n\n¿Quieres iniciar el sistema de quizzes?")
  print("\n\nFavor de responder con 1 o 2 : ") 
  print("\n\n1.- Sí")
  print("\n2.- No")
  respq = int(input("\n\n¿Quieres iniciar el quiz? "))
  while respq < 1 or respq > 2:
    print("\nFavor de responder con Sí o No: ") 
    print("\n1.- Sí")
    print("\n2.- No")
    respq = int(input("\n¿Quieres iniciar el quiz? "))


  #Preguna sobre qué quiz se elegirá    
  if respq == 1:
    print("\n\n--------------------------------------------QUIZ------------------------------------------------\n\n")
    print("\n¿Qué tipo de Quiz quieres realizar?")
    print("\n\n1.- Comandos de Programación")
    print("\n2.- Operadores Matemáticos en Programación")
    global respqu
    respqu = int(input("\n\nFavor de insertar qué tipo de quiz se realizará: "))
    while respqu < 1 or respqu > 2:
      respqu = int(input("\n\nFavor de insertar qué tipo de quiz se realizará: "))
      
    #Quiz 1
    if respqu == 1:
      print("\n\nEstás a punto de comenzar ")
      print("\n\nEste quiz constará de sólo 10 preguntas. Disfruta y aprende.")
      
#estipular que las variables iniciales de respuestas correctas e incorrectas valen 0
      
      global resp_correcta
      resp_correcta = 0
      global resp_incorrecta
      resp_incorrecta = 0

      #Inicio del primer Quiz
      
      print("\n\n------------------Pregunta 1--------------------")
      print("\n\n¿Qué es un 'string'?")
      print("\n\n1.- Tipo de datos compuestos por secuencias de caracteres que representan texto. ")
      print("\n2.- Tipo de función que redondea un número hasta el entero inferior más próximo. ")
      print("\n3.- Tipo de función que sirve para sumar dos o más datos. ")
      resp1 = int(input("\n\nEscribe tu respuesta: "))
      while resp1 < 1 or resp1 > 3:
        resp1 = int(input("\n\nEscribe tu respuesta: "))
        
      if resp1 == 1:
        resp_correct()
        resp_correcta = resp_correcta + 1
    
      elif resp1 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
      elif resp1 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1




      print("\n\n------------------Pregunta 2--------------------")
      print("\n\n¿Un 'string' va entre comillas?")
      print("\n\n1.- Verdadero")
      print("\n2.- Falso")
      resp2 = int(input("\n\nEscribe tu respuesta: "))
      while resp2 < 1 or resp2 > 2:
        resp2 = int(input("\n\nEscribe tu respuesta: "))
          
      if resp2 == 1: 
        resp_correct()
        resp_correcta = resp_correcta + 1
        
      elif resp2 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1




        
      print("\n\n------------------Pregunta 3--------------------")
      print( "\n\n¿Qué función acepta exclusivamente números enteros?")
      print("\n\n1.- float")
      print("\n2.- Input")
      print("\n3.- Int")
      resp3 = int(input("\n\nEscribe tu respuesta: "))
      while resp3 < 1 or resp3 > 3:
        resp3 = int(input("\n\nEscribe tu respuesta: "))

      if resp3 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp3 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
        
      elif resp3 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1





            
      print("\n\n------------------Pregunta 4--------------------")
      print( "\n\n¿Qué función acepta enteros y asimismo números racionales con punto decimal?")
      print("\n1.- input")
      print("\n2.- int")
      print("\n3.- float")
        
      resp4 = int(input("\n\nEscribe tu respuesta: "))
      while resp4 < 1 or resp4 > 3:
        resp4= int(input("\n\nEscribe tu respuesta: "))
      if resp4 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp4 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
        
      elif resp4 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1

      



      print("\n\n------------------Pregunta 5--------------------")
      print( "\n\n¿Qué es un valor booleano'?")
      print("\n\n1.- Aquel valor absoluto que puede ser utilizado en cualquier función")
      print("\n2.- Aquel valor que arroja un valor 'True' o 'False'")
      print("\n3.- Aquel valor que necesita de un input para ser ejecutado")
        
      resp5 = int(input("\n\nEscribe tu respuesta: "))
      while resp5 < 1 or resp5 > 3:
        resp5= int(input("\n\nEscribe tu respuesta: "))
        
      if resp5 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp5 == 2:
        resp_correct()
        resp_correcta = resp_correcta + 1
        
        
      elif resp5 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1





      print("\n\n------------------Pregunta 6--------------------")
      print("\n\n¿Cuál de estas funciones tiene un 'output' de valor booleano'?")
      print("\n1.- If")
      print("\n2.- Sum ")
      print("\n3.- Average")
        
      resp6 = int(input("\n\nEscribe tu respuesta: "))
      while resp6 < 1 or resp6 > 3:
        resp6= int(input("\n\nEscribe tu respuesta: "))
        
      if resp6 == 1:
        resp_correct()
        resp_correcta = resp_correcta + 1
        
      elif resp6 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
      
      elif resp6 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1





      print("\n\n------------------Pregunta 7--------------------")
      print("\n\n¿Cuál es el orden correcto de estas condicionales?")
      print("\n1.- if \n    elif \n    else")
      print("\n2.- elif \n    if \n    else")
      print("\n3-  elif \n    else \n    if")
        
      resp7 = int(input("\n\nEscribe tu respuesta: "))
      while resp7 < 1 or resp7 > 3:
        resp7= int(input("\n\nEscribe tu respuesta: "))
      if resp7 == 1:
         resp_correct()
         resp_correcta = resp_correcta + 1
    
      elif resp7 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
        
      elif resp7 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
       




      print("\n\n------------------Pregunta 8--------------------")
      print("\n\n¿El condicional 'if' siempre precederá al 'elif' y al 'else'?")
      print("\n1.- Verdadero")
      print("\n2.- Falso")
      resp8 = int(input("\n\nEscribe tu respuesta: "))
      while resp8 < 1 or resp8 > 2:
        resp8 = int(input("\n\nEscribe tu respuesta: "))
          
      if resp8 == 1: 
        resp_correct()
        resp_correcta = resp_correcta + 1
        
      elif resp8 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1





      
      print("\n\n------------------Pregunta 9--------------------")
      print("\n\n¿Para qué sirve la función 'Len'?")
      print("\n1.- Para meter valores de una función en otra")
      print("\n2.- Para poder adjudicarle un valor a una variable")
      print("\n3.- Para saber la cantidad de elementos que hay en un objeto")
        
      resp9 = int(input("\n\nEscribe tu respuesta: "))
      while resp9 < 1 or resp9 > 3:
        resp9= int(input("\n\nEscribe tu respuesta: "))

        
      if resp9 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
    
      elif resp9 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
        
      elif resp9 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1




      
            
      print("\n\n------------------Pregunta 10--------------------")
      print("\n\n¿Para qué es usada la función 'For'?")
      print("\n1.- Para iterar en una secuencia")
      print("\n2.- Para devolver variables dentro de una función")
      print("\n3.- Para saber cuántos elementos contiene una lista")
        
      resp10 = int(input("\n\nEscribe tu respuesta: "))
      while resp10 < 1 or resp10 > 3:
        resp10= int(input("\n\nEscribe tu respuesta: "))

        
      if resp10 == 1:
        resp_correct()
        resp_correcta = resp_correcta + 1
        
    
      elif resp10 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        
        
      elif resp10 == 3:
          falso = resp_incorrect()
          print(f"\nTu respuesta es {falso}.")
          resp_incorrecta = resp_incorrecta + 1
        

      

        
      #Aquí se le adjudica al valor de "resultado_porcentaje1" a la función, esto propiciará que lo que arroje la función será el return absoluto del "resultado_porcentaje1" Ya que la funcionalidad del "return" es para que todo lo que hace dicha función lo devuelva y tu con cualquier variable puedes igualarla a la función y arrojará la variable a la que se le adjudicó el return.
      resultado_porcentaje1 = sis_puntos1()
      #Llamar sistema de puntos 
      print("\n\nTu resultado es: " + str(round(resultado_porcentaje1, 2)) + ". \n")

















      
     #Inicio del segundo Quiz
    elif respqu == 2:
      print("\nEstás a punto de comenzar ")
      print("\nEste quiz constará de sólo 10 preguntas. Disfruta y aprende.")

      
      resp_correcta = 0
      resp_incorrecta = 0

      
      print("\n\n------------------Pregunta 1--------------------")
      print("\n\n¿Qué significa: '*' en lenguaje de programación")
      print("\n1.- Resta ")
      print("\n2.- Multiplicación. ")
      print("\n3.- División. ")
      resp1 = int(input("\n\nEscribe tu respuesta: "))
      while resp1 < 1 or resp1 > 3:
        resp1 = int(input("\n\nEscribe tu respuesta: "))
        
      if resp1 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp1 == 2:
        resp_correct()
        resp_correcta = resp_correcta + 1
      
      elif resp1 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1





        
      print("\n\n------------------Pregunta 2--------------------")
      print("\n\n¿El símbolo '//' significa división con resultado entero, excluyendo decimales si es que hay?")
      print("\n1.- Verdadero")
      print("\n2.- Falso")
      resp2 = int(input("\n\nEscribe tu respuesta: "))
      while resp2 < 1 or resp2 > 2:
        resp2 = int(input("\n\nEscribe tu respuesta: "))
      if resp2 == 1: 
         resp_correct()
         resp_correcta = resp_correcta + 1
        
      elif resp2 == 2:
         falso = resp_incorrect()
         print(f"\nTu respuesta es {falso}.")
         resp_incorrecta = resp_incorrecta + 1






      print("\n\n------------------Pregunta 3--------------------")
      print("\n\n¿Qué significa: '**' en lenguaje de programación")
      print("\n1.- Multiplicación ")
      print("\n2.- Raíz Cuadrada. ")
      print("\n3.- Exponenciación")

      resp3 = int(input("\n\nEscribe tu respuesta: "))
      while resp3 < 1 or resp3 > 3:
        resp3 = int(input("\n\nEscribe tu respuesta: "))
        
      if resp3 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp3 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1

      
      elif resp3 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1




    
      print("\n\n------------------Pregunta 4--------------------")
      print("\n\n¿Qué respuesta arroja: 6**6? ")
      print("\n1.- 6 ")
      print("\n2.- 36 ")
      print("\n3.- 72")
      

      
      resp4 = int(input("\n\nEscribe tu respuesta: "))
      while resp4 < 1 or resp4 > 3:
        resp4 = int(input("\n\nEscribe tu respuesta: "))
        
      if resp4 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
    
      elif resp4 == 2:
        resp_correct()
        resp_correcta = resp_correcta + 1

      elif resp4 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1




      
      print("\n\n------------------Pregunta 5--------------------")
      print("\n\nQué respuesta arroja: 7//2 ")
      print("\n1.- 3.5 ")
      print("\n2.- 4 ")
      print("\n3.- 3")
      

      resp5 = int(input("\n\nEscribe tu respuesta: "))
      while resp5 < 1 or resp5 > 3:
        resp5 = int(input("\n\nEscribe tu respuesta: "))

        
      if resp5 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1

        
      elif resp5 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1

        
      elif resp5 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1



      print("\n\n------------------Pregunta 6--------------------")
      print("\n\n¿La función SQRT devuelve la raíz cuadrada de un valor numérico?")
      print("\n1.- Verdadero")
      print("\n2.- Falso")
      resp6 = int(input("\n\nEscribe tu respuesta: "))
      while resp6 < 1 or resp6 > 2:
        resp6 = int(input("\n\nEscribe tu respuesta: "))
      if resp6 == 1: 
         resp_correct()
         resp_correcta = resp_correcta + 1
        
      elif resp6 == 2:
         falso = resp_incorrect()
         print(f"\nTu respuesta es {falso}.")
         resp_incorrecta = resp_incorrecta + 1



      
    
      print("\n\n------------------Pregunta 7--------------------")
      print("\n\n7.-¿Qué realiza el operador: '%' ")
      print("\n1.- Se usa para obtener el residuo de un problema de división")
      print("\n2.- Porcentaje de un número estableciendo parámetros al operador ")
      print("\n3.- Comentarios para hacer énfasis en el algoritmo")
      

      resp7 = int(input("\n\nEscribe tu respuesta: "))
      while resp7 < 1 or resp7 > 3:
        resp7 = int(input("\n\nEscribe tu respuesta: "))

      
      if resp7 == 1:
        resp_correct()
        resp_correcta = resp_correcta + 1


      elif resp7 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1


      elif resp7 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1







      print("\n\n------------------Pregunta 8--------------------")
      print("\n\n¿Qué arroja la siguiente operación? 7%2 ")
      print("\n1.- 1")
      print("\n2.- 2")
      print("\n3.- 3")
      

      resp8 = int(input("\n\nEscribe tu respuesta: "))
      while resp8 < 1 or resp8 > 3:
        resp8 = int(input("\n\nEscribe tu respuesta: "))

      
      if resp8 == 1:
        resp_correct()
        resp_correcta = resp_correcta + 1


      elif resp8 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1


      elif resp8 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1
        




      print("\n\n------------------Pregunta 9--------------------")
      print("\n\n¿Qué arroja la operación siguiente?")
      print("Operación: 5*5**2")
      print("\n1.- 50")
      print("\n2.- 25")
      print("\n3.- 125")
      

      resp9 = int(input("\n\nEscribe tu respuesta: "))
      while resp9 < 1 or resp9 > 3:
        resp9 = int(input("\n\nEscribe tu respuesta: "))

      
      if resp9 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1


      elif resp9 == 2:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1


      elif resp9 == 3:
        resp_correct()
        resp_correcta = resp_correcta + 1





      print("\n\n------------------Pregunta 10--------------------")
      print("\n\n¿Cuál es el resultado de la siguiente operación?")
      print("Operación: 3(5+4)**2")
      print("\nRespuesta 1.- 729")
      print("\nRespuesta 2.- 243")
      print("\nRespuesta 3.- 81")
      

      resp10 = int(input("\n\nEscribe tu respuesta: "))
      while resp10 < 1 or resp10 > 3:
        resp10 = int(input("\n\Escribe tu respuesta: "))

      
      if resp10 == 1:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1


      elif resp10 == 2:
        resp_correct()
        resp_correcta = resp_correcta + 1


      elif resp10 == 3:
        falso = resp_incorrect()
        print(f"\nTu respuesta es {falso}.")
        resp_incorrecta = resp_incorrecta + 1

        
      

      #Llamar sistema de puntos
      resultado_porcentaje1 = sis_puntos1()
      #Aquí se le adjudica al valor de "resultado_porcentaje1" a la función, esto propiciará que lo que arroje la función será el return absoluto del "resultado_porcentaje1" Ya que la funcionalidad del "return" es para que todo lo que hace dicha función lo devuelva y tu con cualquier variable puedes igualarla a la función y arrojará la variable a la que se le adjudicó el return.
      print("\n\nTu resultado es: " + str(round(resultado_porcentaje1, 2)) + ". \n")
      
      

  #Condicional de que si no quieren iniciar el quiz, arroje lo estipulado en la condición
  elif respq == 2:
    print("\nCorrecto. ¡Esperamos vuelvas!")
    pregunta_dicotómica()
    
    
    
#Llamar a la función para que ejecute el programa 
reiteracion()










