from Cartas import generar_mazo
from Cartas import repartir_cartas
from JugadaJugador import jugada_jugador
from JugadaBot import jugada_bot
import Mensajes
import os

# import random


inicioJuego = True
while inicioJuego:
    os.system('cls')
    mazoJugador = []
    mazoBot = []
    monton = []
    turnoJugador = None
    contador = 0
    atacar = None

    mazo = generar_mazo()
    Mensajes.mensaje_bienvenida()
    repartir_cartas(mazoJugador, mazoBot, mazo)

    monton.append(mazo[0])
    del mazo[0]

    turnoJugador = Mensajes.elegir_primer_turno(turnoJugador)

    finJuego = False
    while not finJuego:
        Mensajes.mostrar_turno(turnoJugador)
        Mensajes.carta_en_mesa(monton)

        if turnoJugador:
            turnoJugador, atacar, contador = jugada_jugador(mazoJugador, monton, mazo, atacar, contador)

        else:
            # Mensajes.ver_baraja_bot(mazoBot)
            turnoJugador, atacar, contador = jugada_bot(mazoBot, monton, mazo, atacar, contador)
            # Mensajes.ver_baraja_bot(mazoBot)

        if len(mazoJugador) == 0 or len(mazoBot) == 0:
            if len(mazoJugador) == 0:
                Mensajes.fin_partida_jugador()
            elif len(mazoBot) == 0:
                Mensajes.fin_partida_bot()

            finJuego = True

            while True:
                jugarDeNuevo = input()

                if jugarDeNuevo == 's':
                    inicioJuego = True
                    break
                elif jugarDeNuevo == 'n':
                    inicioJuego = False
                    break
                else:
                    Mensajes.error_jugar_de_nuevo()

print()
print('GRACIAS POR JUGAR ^-^'.center(50))
print()
os.system('PAUSE')
