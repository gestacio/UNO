from random import shuffle
from Atacar import ataque
import Recargas
import Mensajes
import time


# DEFINICIÓN DE JUGADAS PARA EL BOT
def jugada_bot(mazoBot, monton, mazo, atacar, contador):
    mesa = monton[-1]
    posible_jugada = []
    print(f'Cantidad de cartas en la baraja del Bot: {len(mazoBot)}\n')
    if atacar:
        i = 0
        while i < len(mazoBot):

            if mazoBot[i].valor == '+2' or mazoBot[i].valor == '+4':
                carta_bot = mazoBot[i]
                posible_jugada.append(carta_bot)
                # print(f'TIENES UNA POSIBLE JUGADA: {carta_bot}')
            i += 1

        if len(posible_jugada) > 0:
            shuffle(posible_jugada)
            # print(f'SE HA JUGADO LA CARTA {posible_jugada[0]}')
            Mensajes.carta_jugada_bot(posible_jugada[0])
            monton.append(posible_jugada[0])
            contador = ataque(posible_jugada[0], contador)
            mazoBot.remove(posible_jugada[0])

            turno_jugador = True
            return turno_jugador, True, contador

        else:
            atacar, contador = Recargas.forzar_recarga(contador, mazo, mazoBot, monton, False)
            turno_jugador = True
            return turno_jugador, atacar, contador

    else:
        turno_bot = True
        while turno_bot:
            mesa = monton[-1]
            carta_bot = None
            posible_jugada = []
            # Mensajes.ver_baraja_bot(mazoBot)

            for i in range(len(mazoBot)):
                carta_bot = mazoBot[i]
                if mesa.color == 'negro' or \
                        carta_bot.color == 'negro' or \
                        mesa.color == carta_bot.color or \
                        mesa.valor == carta_bot.valor or \
                        monton[-1].valor == 'comodin':
                    # print(f'TIENES UNA POSIBLE JUGADA: {carta_bot}')
                    posible_jugada.append(carta_bot)

            if len(posible_jugada) > 0:
                shuffle(posible_jugada)

                if posible_jugada[0].valor == 'Ø' or \
                        posible_jugada[0].valor == '<=>' or \
                        posible_jugada[0].valor == 'comodin':
                    # print(f'SE HA JUGADO LA CARTA {posible_jugada[0]}')
                    Mensajes.carta_jugada_bot(posible_jugada[0])
                    monton.append(posible_jugada[0])
                    mazoBot.remove(posible_jugada[0])
                    turno_bot = True

                elif posible_jugada[0].valor == '+2' or \
                        posible_jugada[0].valor == '+4':
                    contador = ataque(posible_jugada[0], contador)
                    # print(f'SE HA JUGADO LA CARTA {posible_jugada[0]}')
                    Mensajes.carta_jugada_bot(posible_jugada[0])
                    monton.append(posible_jugada[0])
                    mazoBot.remove(posible_jugada[0])
                    Mensajes.cartas_acumuladas(contador)
                    atacar = True
                    turno_bot = False

                else:
                    # print(f'SE HA JUGADO LA CARTA {posible_jugada[0]}')
                    Mensajes.carta_jugada_bot(posible_jugada[0])
                    monton.append(posible_jugada[0])
                    mazoBot.remove(posible_jugada[0])
                    turno_bot = False

            else:
                time.sleep(1)
                Recargas.recarga(mazo, mazoBot)
                Recargas.recargar_mazo(mazo, monton)

    print(f'\nCantidad de cartas en la baraja del Bot: {len(mazoBot)}')
    turno_jugador = True
    return turno_jugador, atacar, contador
