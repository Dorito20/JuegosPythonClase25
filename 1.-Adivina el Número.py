#Modifica el juego para que le diga al jugador si está "muy cerca" o "muy lejos" del número secreto cuando falle.

import random 

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu número!"))
        intentos += 1
        distancia=abs(numero_secreto-intento)
        if intento < numero_secreto:
            if distancia<=10:
                print("Demasiado bajo y esta cerca, intenta de nuevo.")
            else:   
                print("Demasiado bajo y esta lejos, intenta de nuevo.")
        elif intento > numero_secreto:
            if distancia<=10:
                print("Demasiado bajo y esta cerca, intenta de nuevo.")
            else:   
                print("Demasiado bajo y esta lejos, intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()
