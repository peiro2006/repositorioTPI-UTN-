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