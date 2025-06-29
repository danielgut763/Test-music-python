class Instrumento:
    def __init__(self, valor):
        self.valor = valor

    def trocar(self, caractere, instrumento_anterior=None):
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
            digito = int(caractere)
            if digito % 2 == 0:
                if instrumento_anterior is not None:
                    self.valor = instrumento_anterior.valor + digito
                else:
                    return None
            else:
                self.valor = 15
        return self.valor
