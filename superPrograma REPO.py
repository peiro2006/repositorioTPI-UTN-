#Importamos el valor Random para los juegos

import random

#Establecemos la variable para elejir los juegos

juegito = 1

#Mediante la estructura "while" (Mientras), comprobamos que mientra el valor de la variable "jueguito" no sea de 6, que se ejecute el super programa

while juegito != 6:
    
    #Mostramos en pantalla el menu de juegos

    print("")
    print("¡Binvenido al menu de juegos!")
    print("")
    print("1: BUSCAMINAS (Autor: Nazareno Peirone)")
    print("")
    print("2: AHORCADO (Autor: Augusto Baricco)")
    print("")
    print("3: ADIVINA EL NUMERO (Autora: Guadalupe Torres)")
    print("")
    print("4: PIEDRA, PAPEL O TIJERA (Autor: Matias Medina)")
    print("")
    print("5: BATALLA NAVAL (Autor: Ramiro Quintero)")
    print("")
    print("(Ingrese el numero 6 para salir del menu)")
    
    
    juegito = int(input("Ingrese el número del juego que desee jugar: "))

    if juegito == 1:

        #Establecemos las vidas

        vida = 1

        #Le damos la bienvenida al jugador mediante textos

        print("")
        print("Bienvenido al Buscaminas!")
        print("")

        #Establecemos las filas y las imprimimos en pantalla, imprimiendo tambien las reglas del juego

        f1= [1, 2, 3]
        f2= [4, 5, 6]
        f3= [7, 8, 9]

        print(f1)
        print(f"{f2}    ¡Hay 3 bombas en estos 9 numeros!")
        print(f3)
        print("")
        print("Regla 1: Tras elegir un numero, no podes volver a elegirlo")
        print("Regla 2: No se puede elegir un numero menor a 1, ni un numero mayor a 10")
        print("")

        #Asignamos una mina a un valor por cada fila de manera aleatoria

        minasF1 = random.sample(f1,1)[0]
        minasF2 = random.sample(f2,1)[0]
        minasF3 = random.sample(f3,1)[0]

        #Le pedimos al jugador que ingrese un numero

        eleccion1 = int(input("Eleji un numero y reza para que no contenga una mina!: "))

        #Ahora, arrancamos el algoritmo del juego:
        #Las aclaraciones iran al lado de los codigos

        if eleccion1 == 0 or eleccion1 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                print("El numero ingresado rompe las reglas, perdiste")
                vida = vida - 1

        while eleccion1 != 0 and eleccion1 <= 9 and vida == 1: #Ingresamos los valores necesarios para iniciar el juego

            if eleccion1 == minasF1 or eleccion1 == minasF2 or eleccion1 == minasF3 : #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                print("¡Perdiste!")
                vida = vida - 1
                break
            else:
                if eleccion1 != minasF1 or eleccion1 != minasF2 or eleccion1 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                    print("Te salvaste")
                    eleccion2 = int(input("Eleji otro numero y reza para que no contenga una mina!: "))
                    if eleccion2 == eleccion1 or eleccion2 == 0 or eleccion2 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                        print("El numero ingresado rompe las reglas, perdiste")
                        vida = vida - 1
                        break
                    else:
                        while eleccion2 != 0 and eleccion2 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                            if eleccion2 == minasF1 or eleccion2 == minasF2 or eleccion2 == minasF3 or eleccion2 == 0 or eleccion2 > 9: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                print("¡Perdiste!")
                                vida = vida - 1
                                break
                            else:
                                if eleccion2 != minasF1 or eleccion2 != minasF2 or eleccion2 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                    print("Te salvaste")
                                    eleccion3 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                    if eleccion3 == eleccion2 or eleccion3 == eleccion1 or eleccion3 == 0 or eleccion3 > 9: #Aca se comprueba que el jugador no rompa la reglas del juego
                                        print("El numero ingresado rompe las reglas, perdiste")
                                        vida = vida - 1
                                        break
                                    else:
                                        while eleccion3 != 0 and eleccion3 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                            if eleccion3 == minasF1 or eleccion3 == minasF2 or eleccion3 == minasF3 or eleccion3 == 0 or eleccion3 > 9: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                print("¡Perdiste!")
                                                vida = vida - 1
                                                break
                                            else:
                                                if eleccion3 != minasF1 or eleccion3 != minasF2 or eleccion3 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                    print("Te salvaste")
                                                    eleccion4 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                    if eleccion4 == eleccion3 or eleccion4 == eleccion2 or eleccion4 == eleccion1 or eleccion4 == 0 or eleccion4 > 9:
                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                        vida = vida - 1
                                                        break
                                                    else:
                                                        while eleccion4 != 0 and eleccion4 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                            if eleccion4 == minasF1 or eleccion4 == minasF2 or eleccion4 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                print("¡Perdiste!")
                                                                vida = vida - 1
                                                                break
                                                            else:
                                                                if eleccion4 != minasF1 or eleccion4 != minasF2 or eleccion4 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                                    print("Te salvaste")
                                                                    eleccion5 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                                    if eleccion5 == eleccion4 or eleccion5 == eleccion3 or eleccion5 == eleccion2 or eleccion5 == eleccion1 or eleccion5 == 0 or eleccion5 > 9:
                                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                                        vida = vida - 1
                                                                        break
                                                                    else:
                                                                        while eleccion5 != 0 and eleccion5 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                                            if eleccion5 == minasF1 or eleccion5 == minasF2 or eleccion5 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                                print("¡Perdiste!")
                                                                                vida = vida - 1
                                                                                break
                                                                            else:
                                                                                if eleccion5 != minasF1 or eleccion5 != minasF2 or eleccion5 != minasF3: #Si el jugador elijio un numero sin mina, este continua el recorrido
                                                                                    print("Te salvaste")
                                                                                    eleccion6 = int(input("Eleji un numero y reza para que no contenga una mina!: "))
                                                                                    if eleccion6 == eleccion5 or eleccion6 == eleccion4 or eleccion6 == eleccion3 or eleccion6 == eleccion2 or eleccion6 == eleccion1 or eleccion6 == 0 or eleccion6 > 9:
                                                                                        print("El numero ingresado rompe las reglas, perdiste") #Aca se comprueba que el jugador no rompa la reglas del juego
                                                                                        vida = vida - 1
                                                                                        break
                                                                                    else:
                                                                                        while eleccion6 != 0 and eleccion6 < 10 and vida == 1: #Comprobamos que el valor no sea invalido y que el jugador tenga una vida
                                                                                            if eleccion6 == minasF1 or eleccion6 == minasF2 or eleccion6 == minasF3: #Si el jugador elijio un numero con mina, este pierde su vida, terminando el juego
                                                                                                print("¡Perdiste!")
                                                                                                vida = vida - 1
                                                                                                break
                                                                                            else:
                                                                                                if eleccion6 != minasF1 or eleccion6 != minasF2 or eleccion6 != minasF3: #Si el jugador elijio un numero sin mina, este finaliza el juego
                                                                                                    vida = 2
                                                                                                    while vida == 2:
                                                                                                        print("¡GANASTE!") #:D
                                                                                                        break 
  