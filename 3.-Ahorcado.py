# Crear una versión simple del juego "Ahorcado" donde el jugador intente adivinar una palabra letra por letra.

import random

def ahorcado():
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "juego"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("_ " * len(palabra_secreta))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(palabra_mostrada))

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break
    else:
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'.")

ahorcado()

#Deber: Modifica el código para que el juego dé una pista de la palabra secreta al inicio (por ejemplo, decir el tema o una letra inicial).

import random

def ahorcado():
    palabras = { 
        "python": "Lenguaje de programación popular",
        "programacion": "Actividad para crear software",
        "ahorcado": "Nombre del juego que estás jugando",
        "desarrollo": "Proceso de creación de software",
        "juego": "Forma de entretenimiento",
        "espacio": "Lugar donde se encuentran los planetas y estrellas",
        "musica": "Arte de organizar sonidos en el tiempo",
        "cientifico": "Profesional que realiza investigaciones y experimentos"       
    }
    palabra_secreta = random.choice(list(palabras))
    pistas = palabras[palabra_secreta]
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"Pista: {pistas}")
    print("_ " * len(palabra_secreta))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(palabra_mostrada))

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break
    else:
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'.")

ahorcado()