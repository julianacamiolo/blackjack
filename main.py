import random

# Definir las cartas y sus valores
cartas = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11  # El As vale 11 por defecto en este juego simple
}

# Función para repartir cartas
def repartir_cartas():
    carta1 = random.choice(list(cartas.keys()))
    carta2 = random.choice(list(cartas.keys()))
    return carta1, carta2

# Función para calcular la puntuación
def calcular_puntuacion(carta1, carta2):
    return cartas[carta1] + cartas[carta2]

# Función principal del juego
def jugar_blackjack():
    print("¡Bienvenido al juego de Blackjack!")

    # Repartir cartas al jugador
    cartas_jugador = repartir_cartas()
    puntuacion_jugador = calcular_puntuacion(cartas_jugador[0], cartas_jugador[1])
    print(f"Cartas del Jugador: {cartas_jugador[0]} y {cartas_jugador[1]} (Puntuación: {puntuacion_jugador})")

    # Repartir cartas a la banca
    cartas_banca = repartir_cartas()
    puntuacion_banca = calcular_puntuacion(cartas_banca[0], cartas_banca[1])
    print(f"Cartas de la Banca: {cartas_banca[0]} y {cartas_banca[1]} (Puntuación: {puntuacion_banca})")

    # Determinar el ganador
    if puntuacion_jugador > puntuacion_banca:
        print("¡El jugador gana!")
    elif puntuacion_jugador < puntuacion_banca:
        print("La banca gana.")
    else:
        print("¡Es un empate!")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_blackjack()