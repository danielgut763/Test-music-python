class Instrumento:
    def __init__(self):
        self.valor = 0

    def trocar(self, caractere, valor_anterior=None):
        if caractere == '!':
            self.valor = 24
        elif caractere in 'oOiIuU':
            self.valor = 110
        elif caractere == '\n':
            self.valor = 123
        elif caractere == ';':
            self.valor = 15
        elif caractere == ',':
            self.valor = 114
        elif caractere.isdigit():
            dig = int(caractere)
            if dig % 2 == 0 and valor_anterior is not None:
                self.valor = valor_anterior + dig
            else:
                self.valor = 15
        return self.valor
