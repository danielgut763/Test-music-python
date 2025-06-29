from padrao_MIDI import *

# Define um instrumento
# Permite obter seu valor MIDI e trocar para um novo instrumento
class Instrumento:
    def __init__(self, codigo):
        self.codigo = codigo

    def obter_valor_midi(self):
        return self.codigo

    def trocar(self):
        self.codigo += 1
        if self.codigo > INSTRUMENTO_MAXIMO:
            self.codigo = INSTRUMENTO_MINIMO