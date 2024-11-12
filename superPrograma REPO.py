
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

        import buscaminas #importamos el juego