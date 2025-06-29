from padrao_MIDI import *

class Instrumento:
    def __init__(self, codigo):
        self.codigo = codigo

    def obter_valor_midi(self):
        return self.codigo

    def trocar(self):
        self.codigo += 1
        if self.codigo > INSTRUMENTO_MAXIMO:
            self.codigo = INSTRUMENTO_MINIMO