def Ahorcado(x): 
    #Juego El Ahorcado#
    import random
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
