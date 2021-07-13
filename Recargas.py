from random import shuffle


# RECARGA DEL MAZO COMPLETO
def recargar_mazo(mazo, monton):
    if len(mazo) == 0:
        for i in range(len(monton)-1):
            mazo.append(monton[i])
            del monton[i]

        shuffle(mazo)


# RECARGA DEL MAZO DE LOS JUGADORES
def recarga(mazo, mazo_jugador_o_bot):
    mazo_jugador_o_bot.append(mazo[0])
    del mazo[0]
    print(f'Se ha recargado una carta')


# RECARGA FORZADA
def forzar_recarga(contador, mazo, mazo_jugador_o_bot, monton, turno_jugador):
    cartas = []
    for i in range(contador):
        mazo_jugador_o_bot.append(mazo[0])
        del mazo[0]

        cartas.append(i)
        recargar_mazo(mazo, monton)

    if turno_jugador:
        jugador = 'Jugador'
    else:
        jugador = 'Bot'

    print(f'El {jugador} ha recargado {len(cartas)} cartas')

    contador = 0
    return False, contador

