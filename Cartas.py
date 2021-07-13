from Carta import Carta
import random

# Constantes
COLORES = ['rojo', 'verde', 'azul', 'amarillo']
NEGROS = 'negro'
CEROS = ['0']
NUMEROS = []
for i in range(1, 10):
    NUMEROS.append(str(i))
SIMBOLOS = ['+2', 'Ø', '<=>']
ESPECIALES = ['+4', 'comodin']


# Funcion para generar el mazo completo
def generar_mazo():
    listaMazo = []

    for i in range(len(COLORES)):
        carta = Carta(COLORES[i], CEROS[0])
        listaMazo.append(carta)

    for x in range(4):
        for i in range(len(ESPECIALES)):
            carta = Carta(NEGROS, ESPECIALES[i])
            listaMazo.append(carta)

    for x in range(2):
        for i in range(len(COLORES)):
            for j in range(len(NUMEROS)):
                carta = Carta(COLORES[i], NUMEROS[j])
                listaMazo.append(carta)

    for x in range(2):
        for i in range(len(COLORES)):
            for j in range(len(SIMBOLOS)):
                carta = Carta(COLORES[i], SIMBOLOS[j])
                listaMazo.append(carta)

    random.shuffle(listaMazo)
    return listaMazo


# Función para repartir las cartas
def repartir_cartas(mazoJugador, mazoBot, mazo):
    for i in range(7):
        mazoJugador.append(mazo[0])
        del mazo[0]
        mazoBot.append(mazo[0])
        del mazo[0]


if __name__ == '__main__':
    mazo = generar_mazo()
    # for i in range(len(mazo)):
    #     print(mazo[i])

    mazoJugador = []
    mazoBot = []
    repartir_cartas(mazoJugador, mazoBot, mazo)
    for i in range(len(mazoJugador)):
        print(mazoJugador[i])
        print(mazoBot[i])
