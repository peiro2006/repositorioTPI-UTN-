
#Importamos el valor Random para los juegos

import random

jugar = 0
archivo = open("bienvenido.txt", "r") #preparamos el archivo
leerArchivo = archivo.read()

#Establecemos la variable para elejir los juegos

juegito = 0

#Mediante la estructura "while" (Mientras), comprobamos que mientra el valor de la variable "jueguito" no sea de 6, que se ejecute el super programa

while juegito != 6:
    
    #Mostramos en pantalla el menu de juegos

    print("")

    print(leerArchivo) #leemos el archivo

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
        def buscaminas(vida):

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

            eleccion1 = int(input("Elegi un numero y reza para que no contenga una mina!: "))

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
                        eleccion2 = int(input("Elegi otro numero y reza para que no contenga una mina!: "))
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
                                        eleccion3 = int(input("Elegi un numero y reza para que no contenga una mina!: "))
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
                                                        eleccion4 = int(input("Elegi un numero y reza para que no contenga una mina!: "))
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
                                                                        eleccion5 = int(input("Elegi un numero y reza para que no contenga una mina!: "))
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
                                                                                        eleccion6 = int(input("Elegi un numero y reza para que no contenga una mina!: "))
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
        jugar = 0
        buscaminas(jugar)
    if juegito == 2:
        def Ahorcado(x): 
            #Juego El Ahorcado#
            
            Palabras = ["esternocleidomastoideo","auriculares","zapatillas","bicicleta","musica","gato","codigo"]
            #randomchoice es para que seleccione aleatoriamente cualquier palabra de la variable palabras
            palabraclave = random.choice(Palabras)
            #Aca hace que la palabra elegida se transforme en guiones, varia dependiendo el largo de la palabra
            cadena = "-" * len(palabraclave)
            intentos=0
            print("Bienvenidos al ahorcado")
            while True:
                print(cadena)
                letra = input(" Ingrese una letra: ")
                #bucle for, pasa por toda la palabra la letra ingresada, si es correcta, cambia los guiones solo por esa letra.
                if letra in palabraclave:
                    for i in range(len(palabraclave)):
                        if palabraclave[i]==letra:
                            cadena=cadena[:i]+letra+cadena[i+1:]
                            #Esta funcion hace que cambie la letra que coincide, va hasta i (coincide) la modifica y las demas siguen igual.
                else:
                    intentos+=1
                    if intentos == 1:
                        print(" ")
                        print("Error 1/5 La letra no coincide, vuelve a intentarlo!")
                    elif intentos == 2:
                        print(" ")
                        print ("Error 2/5, La letra no coincide, vuelve a intentarlo!")
                    elif intentos == 3:
                        print(" ")
                        print ("Error 3/5, La letra no coincide, vuelve a intentarlo!")            
                    elif intentos ==4:
                        print(" ")
                        print ("Error 4/5, La letra no coincide, es tu última oportunidad!") 
                    elif intentos == 5:
                        print(" ")
                        print (f"Error 5/5, haz perdido!la palabra oculta era {palabraclave}")
                        break
                if cadena == palabraclave:
                        print (f"felicidades, has ganado. La palabra oculta era: {palabraclave}")
                        break
        x=0
        Ahorcado(x)                 
    if juegito == 3:
        print("")
    if juegito == 4:
        def piedrapapeltijera(ejemplo):
    
            print("")
            print("Piedra = 1")
            print("Papel = 2        ¡Gana el mejor de 3!")
            print("Tijera = 3")
            print("")

            jugando= 0 
            rM = 0
            rJ = 0

            juego = [1,2,3]

            while rM != 3 and rJ != 3:
                eleccionMaquina = random.sample(juego,1)[0]
                eleccion = int(input("Eleji entre las 3: "))

                if eleccion == eleccionMaquina:
                    print("Empate")

                if eleccion == 1 and eleccionMaquina == 3:
                    print("La maquina eligió tijera, ganaste!")
                    rJ = rJ + 1
                else:
                    if eleccion == 1 and eleccionMaquina == 2:
                        print("La maquina eligió papel, perdiste!")
                        rM = rM + 1


                if eleccion == 2 and eleccionMaquina == 1:
                    print("La maquina eligió piedra, ganaste!")
                    rJ = rJ + 1
                else:
                    if eleccion == 2 and eleccionMaquina == 3:
                        print("La maquina eligió tijera, perdiste!")
                        rM = rM + 1


                if eleccion == 3 and eleccionMaquina == 2:
                    print("La maquina eligió papel, ganaste!")
                    rJ = rJ + 1
                else:
                    if eleccion == 3 and eleccionMaquina == 1:
                        print("La maquina eligió piedra, perdiste!")
                        rM = rM + 1

            while jugando == 0:
                if rJ == 3:
                    print("¡Ganaste!")
                    break
                else:
                    if rM == 3:
                        print("¡Perdiste!")
                        break
        f = 0
        piedrapapeltijera(f)
    if juegito == 5:
        def BatallaNaval(jueguito):

            #SELECCIONAMOS EL TAMAÑO DESEADO DEL TABLERO.

            tamaño=input("seleccione el tamaño del tablero 1=3x3 2=4x4 3=5x5:")
            if tamaño =="1":
                t=3
            elif tamaño == "2":
                t=4
            else:
                if tamaño == "3":
                    t=5

            #CREAMOS LOS TABLEROS PARA CADA JUGADOR.

            tablero1= [[0 for columnas in range (t)]for filas in range (t)]
            for filas in range (0,(len(tablero1))):

                for columnas in range (0,(len(tablero1[filas]))): 
                    tablero1[filas-1][columnas-1]= 0
            for filas in tablero1:
                print (filas)
            print (" ")
            tablero2= [[0 for columnas2 in range (t)]for filas2 in range (t)]
            for filas2 in range (0,(len(tablero2))):

                for columnas2 in range (0,(len(tablero2[filas2]))): 
                    tablero2[filas2-1][columnas2-1]= 0
            for filas2 in tablero2:
                print (filas2)

            #CADA JUGADOR DEBE CARGAR SUS BARCOS, TENDRAN UNA CANTIDAD DETERMINADA DE BARCOS 1X1 SEGUN EL TAMAÑO DEL TABLERO.

            print("TURNO JUGADOR 1 COLOCAR BARCOS")
            if tamaño == "1":
                barcosp1=3
                barcosp2=3
                barcos1=30
                barcos2=30
            elif tamaño=="2":
                barcosp1=5
                barcosp2=5
                barcos1=50
                barcos2=50
            else:
                if tamaño=="3":
                    barcosp1=7
                    barcosp2=7
                    barcos1=70
                    barcos2=70

            #JUGADOR NUMERO 1 COLOCA SUS BARCOS.

            print("TURNO JUGADOR 1 COLOCAR BARCOS")
            while barcosp1>0: 
                n1= int(input("ingrese la fila donde colocar su barco: "))
                n2= int(input("ingrese columna donde colocar su barco: "))
                # VALIDAMOS LOS LIMITES Y CHEQUEAMOS SI LA POSICION ESTA OCUPADA.
                if 1 <= n1 <= t and 1 <= n2 <= t:
                    if tablero1[n1-1][n2-1] == 0:
                        tablero1[n1-1][n2-1] = 1
                        barcosp1 = barcosp1 - 1
                    else:
                        print("Posición ocupada, elige otra.")
                else:
                    print("Posición fuera de rango, intenta de nuevo.")
            for filas in tablero1:
                print (filas)

            #JUGADOR NUMERO 2 COLOCA SUS BARCOS.

            print("TURNO JUGADOR 2 COLOCAR BARCOS")
            while barcosp2>0:
                n3= int(input("ingrese la fila donde colocar su barco: "))
                n4= int(input("ingrese columna donde colocar su barco: "))
                if 1 <= n3 <= t and 1 <= n4 <= t:
                    if tablero2[n3-1][n4-1] == 0:
                        tablero2[n3-1][n4-1] = 2
                        barcosp2 = barcosp2 - 1
                    else:
                        print("Posición ocupada, elige otra.")
                else:
                    print("Posición fuera de rango, intenta de nuevo.")
            for filas in tablero2:
                print (filas)

            #AQUI COMIENZA EL BOMBARDEO DE BARCOS.

            while barcos1>0 and barcos2>0:
                print("TURNO JUGADOR 1, PUNTOS RESTANTES: ", barcos1)
                n3= int(input("ingrese fila: "))
                n4= int(input("ingrese columna: "))
                if tablero2[n3-1][n4-1]==2:
                    barcos2= barcos2 - 10 #RESTAMOS 10 PUNTOS SI LA BOMBA HUNDE UN BARCO ENEMIGO.
                    print ("¡HUNDISTE UN BARCO!")
                elif tablero2[n3-1][n4-1]!=2:
                    barcos1=barcos1-5 #RESTAMOS 5 PUNTOS SI LA BOMBA CAE EN EL AGUA.
                    print ("TU BOMBA CAYO EN EL AGUA")
                    while barcos1>0 and barcos2>0:
                        print("TURNO JUGADOR 2, PUNTOS RESTANTES: ", barcos2)
                        n1= int(input("ingrese fila: "))
                        n2= int(input("ingrese columna: "))
                        if tablero1[n1-1][n2-1]== 1:
                            barcos1=barcos1 - 10 #RESTAMOS 10 PUNTOS SI LA BOMBA HUNDE UN BARCO ENEMIGO.
                            print ("¡HUNDISTE UN BARCO!") 
                        else: 
                            if tablero1[n1-1][n2-1]!=1:
                                barcos2=barcos2-5 #RESTAMOS 5 PUNTOS SI LA BOMBA CAE EN EL AGUA.
                                print ("¡TU BOMBA CAYO EN EL AGUA!") 
                                break

            if barcos1<=0:
                print ("JUGADOR 2 ES EL GANADOR")   
            else:
                if barcos2<=0:
                    print ("JUGADOR 1 ES EL GANADOR")
        jueguito=0
        BatallaNaval(jueguito)