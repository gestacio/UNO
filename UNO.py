# JUEGO DEL UNO EN PROGRAMACIÓN ESTRUCTURADA
import random
# import time

# Declaración de constantes
ceros = ['0']
simbolos = ['+2', 'Ø', '<=>']
colores = ['rojo', 'azul', 'verde', 'amarillo']
colorNegro = ['negro']
cartasEspeciales = ['+4', 'comodin']


# --------------- Definicion de funciones-----------------
# Devuelve el mazo entero del juego. (version de 108 cartas).
def crear_mazo():
    global mazo
    mazo = []
    comodines = []

    for x in range(1, 10):
        numeros.append(x)

    for x in colores:
        for y in numeros:
            diccionario = {
                'color': x,
                'valor': y
            }
            mazo.append(diccionario)

    for x in colores:
        for y in simbolos:
            diccionario = {
                'color': x,
                'valor': y
            }
            mazo.append(diccionario)

    mazo = mazo * 2

    for x in colorNegro:
        for y in cartasEspeciales:
            diccionario = {
                'color': x,
                'valor': y
            }
            comodines.append(diccionario)

    comodines = comodines * 4

    for x in comodines:
        mazo.append(x)

    for x in colores:
        for y in ceros:
            diccionario = {
                'color': x,
                'valor': y
            }
            mazo.append(diccionario)

    random.shuffle(mazo)
    return mazo


# Muestra las cartas que hay en el mazo.
def mostrar_mazo():
    for x in mazo:
        print(x)


# Reparte las cartas a cada jugador.
def repartir_cartas():
    for x in range(7):
        mazoJugador.append(mazo[x])
        del mazo[x]

        mazoBot.append(mazo[x])
        del mazo[x]


# Muestra las cartas de cada jugador.
def mostrar_mazo_jugadores():
    for x in mazoJugador:
        print(x)

    for x in mazoBot:
        print(x)


# Mostrar carta en mesa.
def carta_en_mesa():
    print(f"\nLa carta que está sobre la mesa es: \n{mesa[0]['color']} -> {mesa[0]['valor']}")


# Mostrar cartas al jugador.
def mostrar_mazo_jugador():
    print('\nEstas son tus cartas')

    for x in range(0, len(mazoJugador)):
        opcion = x + 1
        print(f"{opcion:2}. | {mazoJugador[x]['color']:8}| -> {mazoJugador[x]['valor']}")


# Mostrar cartas del bot.
def mostrar_mazo_bot():
    print('\nEstas son las cartas del bot')

    for x in range(0, len(mazoBot)):
        opcion = x + 1
        print(f"{opcion:2}. | {mazoBot[x]['color']:8}| -> {mazoBot[x]['valor']}")


# Muestra la baraja del jugador realiza la jugada.
def jugada_jugador():
    global forzarRecarga
    global contador
    global pierdeTurno
    global darVuelta

    fin_jugada = False
    contraatacar = False

    # Bloque para la recarga forzaza de cartas
    if forzarRecarga:

        for carta in mazoJugador:
            if carta['valor'] == '+2' or carta['valor'] == '+4':
                contraatacar = True
                while contraatacar:
                    print('\n¿Desea contraatacar la jugada del oponente? (y / n)')
                    opcion = input()

                    if opcion.lower() == 'y':
                        while not fin_jugada:
                            mostrar_mazo_jugador()

                            print(f'\nRealiza tu jugada eligiendo una carta (1 - {len(mazoJugador)})')
                            print('Introduce "r" para recargar y no contraatacar')
                            print('O puedes introducir "m" para ver la carta en la mesa')
                            jugada = input()

                            if jugada.lower() == 'r':
                                contraatacar = False
                            elif jugada.lower() == 'm':
                                print(mesa[0])
                            elif jugada.isdigit():
                                if int(jugada) in range(0, len(mazoJugador) + 1):
                                    jugada = int(jugada) - 1

                                    if mazoJugador[jugada]['valor'] == '+2':
                                        contador += 2
                                        forzarRecarga = True
                                    elif mazoJugador[jugada]['valor'] == '+4':
                                        contador += 4
                                        forzarRecarga = True
                                    else:
                                        continue

                                    mesa[0] = mazoJugador[jugada]
                                    monton.append(mesa[0])

                                    print(f"Has jugado la carta: {mesa[0]['color']} -> {mesa[0]['valor']}")
                                    del mazoJugador[jugada]

                                    fin_jugada = True
                                else:
                                    print('Lo siento, esta jugada no es válida1')
                            else:
                                print('Lo siento, esta jugada no es válida2')
                        break

                    elif opcion.lower() == 'n':
                        contraatacar = False
                    else:
                        print('\nOpción no válida, por favor introduce "y" ó "n"')

        if not contraatacar:
            i = 0
            while i < contador:
                mazoJugador.append(mazo[0])
                del mazo[0]
                recargar_mazo()
                i = i + 1

            print(f'Se han recargado {contador} cartas')
            contador = 0
            forzarRecarga = False
            pierdeTurno = True

    # Bloque para evaluar pierde turno y dar vuelta
    if pierdeTurno:
        fin_jugada = True
        pierdeTurno = False
    if darVuelta:
        fin_jugada = True
        darVuelta = False

    # Bloque para la jugada del jugador
    while not fin_jugada:
        mostrar_mazo_jugador()

        print(f'\nRealiza tu jugada eligiendo una carta (1 - {len(mazoJugador)})')
        print('Puedes introducir "r" para robar una carta')
        print('O puedes introducir "m" para ver la carta en la mesa')
        jugada = input()

        if jugada.lower() == 'r':
            mazoJugador.append(mazo[0])
            del mazo[0]
            recargar_mazo()
        elif jugada.lower() == 'm':
            print(mesa[0])
        elif jugada.isdigit():
            if int(jugada) in range(0, len(mazoJugador) + 1):
                jugada = int(jugada) - 1

                if mazoJugador[jugada]['color'] != mesa[0]['color'] \
                        and mazoJugador[jugada]['valor'] != mesa[0]['valor'] \
                        and mazoJugador[jugada]['color'] != 'negro':
                    print('Esta jugada no es válida')
                    print('Por favor introduce una carta válida')
                    continue

                mesa[0] = mazoJugador[jugada]
                monton.append(mesa[0])

                print(f"Has jugado la carta: {mesa[0]['color']} -> {mesa[0]['valor']}")
                del mazoJugador[jugada]

                if mesa[0]['valor'] == '+2' or mesa[0]['valor'] == '+4':
                    forzarRecarga = True
                    if mesa[0]['valor'] == '+2':
                        contador += 2
                    elif mesa[0]['valor'] == '+4':
                        contador += 4

                if mesa[0]['valor'] == 'Ø':
                    pierdeTurno = True
                if mesa[0]['valor'] == '<=>':
                    darVuelta = True
                if mesa[0]['valor'] == 'comodin':
                    print('\nJuega una carta con el color deseado')
                    pierdeTurno = True

                fin_jugada = True
            else:
                print('Lo siento, esta jugada no es válida')
        else:
            print('Lo siento, esta jugada no es válida')


# Realiza la jugada del bot.
def jugada_bot():
    global forzarRecarga
    global contador
    global pierdeTurno
    global darVuelta

    posiblejugada = []
    recargar = True
    eliminar = 0

    # Bloque para la recarga forzada de cartas
    if forzarRecarga:

        for carta in mazoBot:
            if carta['valor'] == '+2':
                posiblejugada.append(carta)
            elif carta['valor'] == '+4':
                posiblejugada.append(carta)

        if len(posiblejugada) > 0:
            random.shuffle(posiblejugada)
            mesa[0] = posiblejugada[0]

            if mesa[0]['valor'] == '+2' or mesa[0]['valor'] == '+4':
                forzarRecarga = True
                if mesa[0]['valor'] == '+2':
                    contador += 2
                elif mesa[0]['valor'] == '+4':
                    contador += 4

            print(f'\nLa jugada del bot fue: {mesa[0]["color"]} -> {mesa[0]["valor"]}')
            monton.append(mesa[0])

            for x in range(len(mazoBot)):
                if mesa[0] == mazoBot[x]:
                    eliminar = x

            del mazoBot[eliminar]

            recargar = False
        else:
            i = 0
            while i < contador:
                mazoBot.append(mazo[0])
                del mazo[0]
                recargar_mazo()
                # mostrar_mazo_bot()
                i = i + 1

            print(f'Se han recargado {contador} cartas')
            forzarRecarga = False
            contador = 0
            pierdeTurno = True

    # Bloque para evaluar pierde turno y dar vuelta
    if pierdeTurno:
        recargar = False
        pierdeTurno = False
    if darVuelta:
        recargar = False
        darVuelta = False

    # Bloque para la jugada del bot
    while recargar:
        for carta in mazoBot:
            if mesa[0]['color'] == 'negro':
                posiblejugada.append(carta)
            elif carta['color'] == mesa[0]['color']:
                posiblejugada.append(carta)
            elif carta['valor'] == mesa[0]['valor']:
                posiblejugada.append(carta)
            elif carta['color'] == 'negro':
                posiblejugada.append(carta)

        random.shuffle(posiblejugada)
        if len(posiblejugada) == 0:
            mazoBot.append(mazo[0])
            del mazo[0]
            recargar_mazo()
            # mostrar_mazo_bot()
        else:
            mesa[0] = posiblejugada[0]
            print(f'\nLa jugada del bot fue: {mesa[0]["color"]} -> {mesa[0]["valor"]}')
            monton.append(mesa[0])

            for x in range(len(mazoBot)):
                if mesa[0] == mazoBot[x]:
                    eliminar = x

            del mazoBot[eliminar]

            if mesa[0]['valor'] == '+2' or mesa[0]['valor'] == '+4':
                forzarRecarga = True
                if mesa[0]['valor'] == '+2':
                    contador += 2
                elif mesa[0]['valor'] == '+4':
                    contador += 4

            if mesa[0]['valor'] == 'Ø':
                pierdeTurno = True
            if mesa[0]['valor'] == '<=>':
                darVuelta = True
            if mesa[0]['valor'] == 'comodin':
                print('\nLa máquina ha jugado un comodín')
                pierdeTurno = True

            recargar = False


# Recarga el mazo completo si no hay cartas en él, con las cartas del montón
def recargar_mazo():
    if len(mazo) == 0:
        for carta in range(len(monton)):
            mazo.append(monton[carta])
        i = 0
        while i < len(monton) - 1:
            del monton[i]


# Inicio del juego.
def iniciar_juego():
    print(''.center(50, '-'))
    print('''
      BIENVENIDO A ESTE JUEGO DE ¡UNO!
    * DESARROLLADOR: GABRIEL ESTACIO
    * GITHUB: github.com/gestacio
      ESPERO LO DISFRUTES!
    ''')
    print(''.center(50, '-'))


def comprobar_fin_juego():
    global finDelJuego
    global iniciarJuego

    if len(mazoJugador) == 0 or len(mazoBot) == 0:
        comprobar = True
        while comprobar:
            if len(mazoJugador) == 0:
                finDelJuego = True
                print('FELICIDADES, HAS GANADO EL JUEGO')
            elif len(mazoBot) == 0:
                finDelJuego = True
                print('LA MÁQUINA GANÓ ESTA VEZ, MEJOR SUERTE A LA PRÓXIMA :)')

            print('¿DESEAS VOLVER A JUGAR? (y/n)')
            volver_a_jugar = input()

            if volver_a_jugar.lower() == 'y':
                comprobar = False
            elif volver_a_jugar.lower() == 'n':
                print('ESPERO VOLVER A VERTE PRONTO, ¡HASTA OTRA! =D')
                iniciarJuego = False
                comprobar = False

        return True
    else:
        return False


# -----------------------------------------------------------------------------
# ----------------------------- INICIO DEL JUEGO ------------------------------
# -----------------------------------------------------------------------------
iniciarJuego = True
while iniciarJuego:
    # Declaración de variables
    forzarRecarga = None
    pierdeTurno = None
    darVuelta = None
    #
    # mazo = []
    mazoJugador = []
    mazoBot = []
    #
    monton = []
    mesa = []
    numeros = []
    #
    contador = 0

    # Funciones inicio del juego
    iniciar_juego()
    mazo = crear_mazo()
    repartir_cartas()

    # Primera carta en la mesa
    mesa.append(mazo[0])
    del mazo[0]
    monton.append(mesa[0])

    finDelJuego = False
    while not finDelJuego:
        carta_en_mesa()
        jugada_jugador()
        finDelJuego = comprobar_fin_juego()
        if finDelJuego:
            break

        carta_en_mesa()
        # mostrar_mazo_bot()
        # time.sleep(2)
        jugada_bot()
        print(f'Cartas restantes del bot: {len(mazoBot)}')
        finDelJuego = comprobar_fin_juego()
        if finDelJuego:
            break

        # print(contadorBot)
        # print(len(mazo))
        # print(len(mazoJugador))
        # print(len(mazoBot))
        # print(monton)
        # print(mesa)

salir = input('Introduzca cualquier tecla para salir')
