import random # se importa random para poder crear numero randoms



def juego_adivinar_numero (): #funcion donde se encuentra el juego

 numero_para_adivinar= random.randint(1,20) #se crea un numero al azar del 1 al 20 y se guarda en una variable
 intentos=0

 print("!!!!Descubre el numero del 1 al 20!!!!")

 while True:
   try: #el juego se encuentra en un bloque try para asegurar que el juego funcione si ingresa un valor que no es un numero
     numero=int(input("Ingrese un numero: "))
     intentos +=1
     if numero < numero_para_adivinar:
        print("Tu numero es menor al numero secreto.")
     elif numero > numero_para_adivinar:
        print("Tu numero es mayor al numero secreto.")
     else:
         print(f"Felicidades adivinaste el numero secreto en {intentos} intentos.")
         break
   except ValueError:
    print("Ingrese un valor numerico valido:")

juego_adivinar_numero()


def jugar_devuelta(): #funcion para saber si el jugador quiere jugar de vuelta
    while True:
     try:
         print("Ingrese 1 si quiere jugar de vulta y 2 si no quiere jugar de vuelta")
         jugar = int(input("¿Desea jugar de vuelta?: "))

         if jugar == 1:
            juego_adivinar_numero()
         elif jugar == 2:
             break
         else:
             print("Ingrese solamente 1 o 2 ")
     except ValueError:
         print("Ingrese solamente 1 o 2 ")



jugar_devuelta()