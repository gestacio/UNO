class Carta:
    def __init__(self, color, valor):
        self.color = color
        self.valor = valor

    def __str__(self):
        return f'[{self.color:8} -> {self.valor}]'


if __name__ == '__main__':
    carta = Carta('amarillo', '0')
    print(carta)
