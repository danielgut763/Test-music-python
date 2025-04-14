class Nota:
    mapa = {
        'A': 69, 'B': 71, 'C': 60,
        'D': 62, 'E': 64, 'F': 65,
        'G': 67, 'H': 70
    }

    def __init__(self, caractere, oitava_extra=0):
        self.caractere = caractere
        self.oitava_extra = oitava_extra

    def obter_valor_midi(self):
        if self.caractere in Nota.mapa:
            return Nota.mapa[self.caractere] + self.oitava_extra
        return None
