import Mensajes
import Recargas
from Atacar import ataque


# DEFINICIÓN DE JUGADAS PARA EL JUGADOR
def jugada_jugador(mazoJugador, monton, mazo, atacar, contador):
    # Si el bot ha hecho algún ataque
    if atacar:
        while True:
            mesa = monton[-1]
            posible_jugada = None
            # Ver si hay +2 o +4 en la baraja del jugador
            for i in range(len(mazoJugador)):
                if mazoJugador[i].valor == '+2' or mazoJugador[i].valor == '+4':
                    posible_jugada = True

            # Si hay
            if posible_jugada:
                print('PUEDES CONTRAATACAR SOLO CON CARTAS "+2" Y "+4"')
                print('SI NO DESEAS CONTRAATACAR, INTRODUCE "R"')
                print('\nEsta es la baraja en tu mano')
                for i in range(len(mazoJugador)):
                    i += 1
                    print(f'{i:3} - {mazoJugador[i - 1]}')

                print(f'\nElige una carta: (1 - {len(mazoJugador)})')
                print('Introduce "r" para recargar')
                print('Introduce "m" para mostrar carta en la mesa')
                carta_jugada = input()

                if carta_jugada == 'r':
                    atacar, contador = Recargas.forzar_recarga(contador, mazo, mazoJugador, monton, True)
                    turno_jugador = False
                    return turno_jugador, atacar, contador
                elif carta_jugada == 'm':
                    Mensajes.carta_en_mesa(monton)
                elif int(carta_jugada) - 1 in range(len(mazoJugador)):
                    carta_jugada = int(carta_jugada)
                    carta_jugada -= 1
                    carta_jugador = mazoJugador[carta_jugada]

                    print(f'\nHas jugado la carta: {carta_jugador}')
                    monton.append(carta_jugador)

                    if carta_jugador.valor == '+2' or \
                            carta_jugador.valor == '+4':
                        contador = ataque(carta_jugador, contador)
                        del mazoJugador[carta_jugada]
                        break
                    else:
                        Mensajes.error_seleccion_equivocada()

            # Si no hay
            else:
                atacar, contador = Recargas.forzar_recarga(contador, mazo, mazoJugador, monton, True)
                turno_jugador = False
                return turno_jugador, atacar, contador

    else:
        while True:
            mesa = monton[-1]

            print('\nEsta es la baraja en tu mano')
            for i in range(len(mazoJugador)):
                i += 1
                print(f'{i:3} - {mazoJugador[i - 1]}')

            print(f'\nElige una carta: (1 - {len(mazoJugador)})')
            print('Introduce "r" para recargar')
            print('Introduce "m" para mostrar carta en la mesa')
            carta_jugada = input()

            if carta_jugada == 'r':
                Recargas.recarga(mazo, mazoJugador)
                Recargas.recargar_mazo(mazo, monton)
            elif carta_jugada == 'm':
                Mensajes.carta_en_mesa(monton)
            elif not carta_jugada.isdigit():
                Mensajes.error_seleccion_equivocada()

            elif int(carta_jugada) - 1 in range(len(mazoJugador)):
                carta_jugada = int(carta_jugada)
                carta_jugada -= 1
                carta_jugador = mazoJugador[carta_jugada]

                if mesa.color == 'negro' or \
                        carta_jugador.color == 'negro' or \
                        mesa.color == carta_jugador.color or \
                        mesa.valor == carta_jugador.valor or \
                        monton[-1].valor == 'comodin':
                    pass
                else:
                    Mensajes.error_seleccion_equivocada()
                    continue

                print(f'\nHas jugado la carta: {carta_jugador}')

                if carta_jugador.valor == 'Ø' or \
                        carta_jugador.valor == '<=>':
                    monton.append(mazoJugador[carta_jugada])
                    del mazoJugador[carta_jugada]
                    continue
                elif carta_jugador.valor == 'comodin':
                    Mensajes.comodin()
                    monton.append(mazoJugador[carta_jugada])
                    del mazoJugador[carta_jugada]
                    continue

                elif carta_jugador.valor == '+2' or \
                        carta_jugador.valor == '+4':
                    contador = ataque(carta_jugador, contador)
                    Mensajes.cartas_acumuladas(contador)
                    monton.append(mazoJugador[carta_jugada])
                    del mazoJugador[carta_jugada]
                    atacar = True

                else:
                    monton.append(mazoJugador[carta_jugada])
                    del mazoJugador[carta_jugada]

                break

            else:
                Mensajes.error_seleccion_equivocada()

    turno_jugador = False
    return turno_jugador, atacar, contador
