import random


# ----- BIENVENIDA -----
def mensaje_bienvenida():
    print(''.center(50, '-'))
    print('|'+'Bienvenido a mi juego de UNO!'.center(48)+'|')
    print('|'+'En esta ocasión, lo he programado con POO!'.center(48)+'|')
    print('|'+'Espero sea de tu agrado =D'.center(48)+'|')
    print('|'+'Búscame en Github: github.com/gestacio'.center(48)+'|')
    print('|'+'Búscame en LinkedIn: likedin.com/in/gestacio'.center(48)+'|')
    print(''.center(50, '-'))


# ----- MOSTRAR CARTAS - JUGADOR - BOT -----
def ver_barajas(mazoJugador, mazoBot):
    print('Jugador:')
    for i in range(len(mazoJugador)):
        print(mazoJugador[i])

    print('Bot:')
    for i in range(len(mazoBot)):
        print(mazoBot[i])


def ver_baraja_jugador(mazoJugador):
    for i in range(len(mazoJugador)):
        print(mazoJugador[i])


def ver_baraja_bot(mazoBot):
    for i in range(len(mazoBot)):
        print(mazoBot[i])


# ----- ELEGIR PRIMER TURNO -----
def elegir_primer_turno(turno_jugador):
    while True:
        print(f'\nElige un número entre 0 y 1 para saber quién comienza primero:\n')
        numero_real = random.randrange(0, 2)
        # print(numero_real)
        numero = input()

        if not numero.isdigit():
            error_seleccion_equivocada()
        elif numero not in ['0', '1']:
            error_seleccion_equivocada()
        else:
            numero = int(numero)
            if numero == numero_real:
                turno_jugador = True
                return turno_jugador
            else:
                turno_jugador = False
                return turno_jugador


# ----- QUIEN JUEGA -----
def mostrar_turno(turno_jugador):
    print()
    if turno_jugador:
        print(''.center(50, '-'))
        print('|'+'Es el turno del jugador'.center(48)+'|')
        print(''.center(50, '-'))
    else:
        print(''.center(50, '-'))
        print('|'+'Es el turno del bot'.center(48)+'|')
        print(''.center(50, '-'))


# ----- MOSTRAR CARTA EN MESA -----
def carta_en_mesa(monton):
    print()
    print(''.center(50, '-'))
    print('|'+f'La carta que se encuentra en la mesa es:'.center(48)+'|')
    print('|'+f'{monton[-1]}'.center(48)+'|')
    print(''.center(50, '-'))
    print()


# ----- MOSTRAR MONTÓN -----
def mostrar_monton(monton):
    for i in range(len(monton)):
        print(f'{monton[i]}')


# ----- MENSAJES DE ERROR -----
def error_seleccion_equivocada():
    print()
    print(''.center(50, '-'))
    print('|'+'Valor no válido'.center(48)+'|')
    print('|'+'Por favor, vuelve a intentarlo'.center(48)+'|')
    print(''.center(50, '-'))
    print()


# ----- JUGADA JUGADOR == COMODIN
def comodin():
    print(''.center(50, '-'))
    print('|'+'Puedes elegir un color tirando otra carta'.center(48)+'|')
    print(''.center(50, '-'))


# ----- CARTA JUGADA DEL BOT -----
def carta_jugada_bot(carta):
    print(''.center(50, '-'))
    print('|'+f'El bot ha jugado la carta {carta}'.center(48)+'|')
    print(''.center(50, '-'))


# ----- CARTAS ACUMULADAS AL ATACAR -----
def cartas_acumuladas(contador):
    print(''.center(50, '-'))
    print('|'+f'CANTIDAD DE CARTAS ACUMULADAS = {contador}'.center(48)+'|')
    print(''.center(50, '-'))


# ----- FIN DE LA PARTIDA -----
def fin_partida_jugador():
    print(''.center(50, '-'))
    print('|'+'EL JUEGO HA TERMINADO'.center(48)+'|')
    print('|'+'¡¡¡FELICIDADES, ERES EL GANADOR DE ESTA PARTIDA!!!'.center(48)+'|')
    print('|'+'¿DESEAS JUGAR DE NUEVO?'.center(48)+'|')
    print(''.center(50, '-'))


def fin_partida_bot():
    print(''.center(50, '-'))
    print('|'+'EL JUEGO HA TERMINADO'.center(48)+'|')
    print('|'+'ESTA VEZ EL BOT HA SIDO EL GANADOR ;)'.center(48)+'|')
    print('|'+'¿DESEAS JUGAR DE NUEVO? (s/n)'.center(48)+'|')
    print(''.center(50, '-'))


def error_jugar_de_nuevo():
    print(''.center(50, '-'))
    print('|'+'Por favor elije una opción adecuada'.center(48)+'|')
    print('|'+'Solo pueden ser "s" o "n"''.center(48)'+'|')
    print(''.center(50, '-'))


if __name__ == '__main__':
    mensaje_bienvenida()
