from padrao_MIDI import *

class Nota:
    mapa = {
        'A':  9, 'a':  9, 
        'B': 11, 'b': 11, 
        'C':  0, 'c':  0,
        'D':  2, 'd':  2, 
        'E':  4, 'e':  4, 
        'F':  5, 'f':  5,
        'G':  7, 'g':  7
    }

    def __init__(self, caractere, oitava):
        self.caractere = caractere
        self.oitava = oitava

    def obter_valor_midi(self):
        if self.caractere in self.mapa:
            valor_base = self.mapa[self.caractere]
            valor_final = valor_base + 12*(self.oitava+2)
            if valor_final > VALOR_MIDI_MAXIMO:
                return None
            else:
                return valor_final
        return None
