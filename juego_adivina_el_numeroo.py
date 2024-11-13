def adivinaelnumero(x):

    from random import randint

    intentos= 0  #Definimos los intentos
    estimado = 0  #Definimos el valor estimado
    numero_secreto= randint (1,100) #Definimos un numero secreto aleatorio
    nombre= input ("Dime tu nombre: ") #Definimos el nombre del jugador

    print (f"{nombre}, he pensado un número entre 1 y 100/n tienes 8 intentos para adivinar")

    while intentos < 8: #Se corre el juego, se mostran mensajes dependiendo de si el numero es menor o mayor al ingresado
        estimado= int(input("Cual es el numero?: "))
        intentos += 1
        if estimado not in range(1,101):
            print("Tu número no se encuentra en el rango que va desde 1 a 100")
        elif estimado < numero_secreto:
            print("Mi numero es mas alto")
        elif estimado > numero_secreto:
            print("Mi numero es mas bajo")
        else:
            print (f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos") #En caso de ganar
            break 

    if estimado != numero_secreto: #En caso de perder
        print (f"Lo siento se han agotado los intentos. El número secreto era {numero_secreto}")

k = 0
adivinaelnumero(k)