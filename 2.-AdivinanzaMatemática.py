# Crear un juego en el que la computadora presente al jugador un problema matemático sencillo (suma, resta, multiplicación o división) y el jugador tenga que resolverlo.

import random

def adivinanza_matematica():
    operaciones = ["+", "-", "*", "/"]
    operacion = random.choice(operaciones)
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    
    if operacion == "/":
        numero1 = numero1 * numero2  # Aseguramos que la división sea exacta

    print("¡Bienvenido al juego de Adivinanza Matemática!")
    print(f"Resuelve el siguiente problema: {numero1} {operacion} {numero2}")
    
    if operacion == "+":
        respuesta_correcta = numero1 + numero2
    elif operacion == "-":
        respuesta_correcta = numero1 - numero2
    elif operacion == "*":
        respuesta_correcta = numero1 * numero2
    elif operacion == "/":
        respuesta_correcta = numero1 // numero2

    respuesta = int(input("Introduce tu respuesta: "))

    if respuesta == respuesta_correcta:
        print("¡Correcto! Has resuelto el problema.")
    else:
        print(f"Incorrecto. La respuesta correcta era {respuesta_correcta}.")

adivinanza_matematica()

#Deber: Modifica el juego para que el jugador tenga tres oportunidades para adivinar la respuesta correcta antes de perder.

from random import randint

def adivinanza_matematica():
    operaciones = ['+', '-', '*', '/']
    operacion = operaciones[randint(0, 3)]
    Numero1 = randint(1, 10)
    Numero2 = randint(1, 10)
    
    if operacion == '/':
        Numero1 *= Numero2 # Aseguramos que la división sea exacta

    problema = f"{Numero1} {operacion} {Numero2}"
    
    if operacion == '+':
        respuesta_correcta = Numero1 + Numero2
    elif operacion == '-':
        respuesta_correcta = Numero1 - Numero2
    elif operacion == '*':
        respuesta_correcta = Numero1 * Numero2
    elif operacion == '/':
        respuesta_correcta = Numero1 / Numero2
        
    return problema, respuesta_correcta

def jugar():
    print("Bienvenido al juego de matemáticas.")
    
    problemas_resueltos = 0
    intentos = 3
    
    while problemas_resueltos < 1:  # Solo un problema por juego
        problema, respuesta_correcta = adivinanza_matematica()
        print(f"Resuelve el siguiente problema: {problema}")
        
        intento = intentos
        
        while intento > 0:
            
            respuesta_usuario = float(input("Introduce tu respuesta: "))
            if respuesta_usuario == respuesta_correcta:
                print("¡Correcto! Has resuelto el problema.")
                problemas_resueltos += 1
                break
            else:
                intento -= 1
                if intento > 0:
                    print(f"Incorrecto. Te quedan {intento} intentos.")
                else:
                    print(f"Lo siento, has agotado tus intentos. La respuesta correcta era {respuesta_correcta}.")
    
    print("¡Juego terminado! Gracias por jugar.")

adivinanza_matematica()

jugar()