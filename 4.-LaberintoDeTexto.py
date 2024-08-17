# Crear un juego donde el jugador deba escapar de un laberinto siguiendo direcciones dadas por el juego.

def laberinto():
    laberinto = {
        "entrada": {"norte": "pasillo", "sur": None, "este": None, "oeste": None},
        "pasillo": {"norte": "salida", "sur": "entrada", "este": "cuarto oscuro", "oeste": None},
        "cuarto oscuro": {"norte": None, "sur": None, "este": None, "oeste": "pasillo"},
        "salida": {"norte": None, "sur": "pasillo", "este": None, "oeste": None},
    }
    posicion_actual = "entrada"
    print("¡Bienvenido al laberinto! Tienes que encontrar la salida.")

    while True:
        direccion = input(f"Estás en {posicion_actual}. Puedes ir hacia: {list(laberinto[posicion_actual].keys())}. ¿Hacia dónde vas? ").lower()

        if direccion in laberinto[posicion_actual] and laberinto[posicion_actual][direccion]:
            posicion_actual = laberinto[posicion_actual][direccion]
            if posicion_actual == "salida":
                print("¡Felicidades, encontraste la salida!")
                break
        else:
            print("No puedes ir en esa dirección, intenta de nuevo.")

laberinto()

#Deber: Añade más habitaciones y direcciones en el laberinto para hacerlo más complejo.

def laberinto():
    laberinto = {
        "entrada": {"norte": "pasillo", "sur": None, "este": None, "oeste": None},
        "pasillo": {"norte": "salida", "sur": "entrada", "este": "cuarto oscuro", "oeste": "lago"},
        "lago": {"norte": None, "sur": "entrada", "este": None, "oeste": "pasillo"},
        "cuarto oscuro": {"norte": None, "sur": "hadas", "este": None, "oeste": "pasillo"},
        "hadas": {"norte": "cuarto oscuro", "sur": None, "este": None, "oeste": "entrada"},
        "salida": {"norte": None, "sur": "pasillo", "este": None, "oeste": "lago"},
    }
    posicion_actual = "entrada"
    print("¡Bienvenido al laberinto! Tienes que encontrar la salida.")

    while True:
        direccion = input(f"Estás en {posicion_actual}. Puedes ir hacia: {list(laberinto[posicion_actual].keys())}. ¿Hacia dónde vas? ").lower()

        if direccion in laberinto[posicion_actual] and laberinto[posicion_actual][direccion]:
            posicion_actual = laberinto[posicion_actual][direccion]
            if posicion_actual == "salida":
                print("¡Felicidades, encontraste la salida!")
                break
        else:
            print("No puedes ir en esa dirección, intenta de nuevo.")

laberinto()