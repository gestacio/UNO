# FUNCIONES PARA LOS +4 Y +4
def ataque(carta_jugada, contador):
    if carta_jugada.valor == '+2':
        contador += 2
    elif carta_jugada.valor == '+4':
        contador += 4

    # print(f'CANTIDAD DE CARTAS ACUMULADAS = {contador}')

    return contador
