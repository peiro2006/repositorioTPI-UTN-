def piedrapapeltijera(ejemplo): #Aplicamos la función
    import random #Le pedimos a la maquina que elija una opción aleatoria
    print("")
    print("Piedra = 1")
    print("Papel = 2        ¡Gana el mejor de 3!")
    print("Tijera = 3")
    print("") #Elegimos la opción nosotros

    jugando= 0  
    rM = 0
    rJ = 0

    juego = [1,2,3] #opciones a elegir, 1 piedra, 2 papel y 3 tijeras

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

    while jugando == 0: #Llegados a este punto se disputa el ganador
        if rJ == 3:
            print("¡Ganaste!")
            break
        else:
            if rM == 3:
                print("¡Perdiste!")
                break
f = 0
piedrapapeltijera(f) #Llamado a la función
