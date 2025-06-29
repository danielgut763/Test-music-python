from padrao_MIDI import *

# Define um tom da música, ou seja, uma nota e a sua oitava
class Tom:
    def __init__(self, nota, oitava):
        self.nota = nota
        self.oitava = oitava

    def obter_valor_midi(self):
        tom = self.nota + 12*(self.oitava+2)
        if tom > TOM_MAXIMO:
            raise ValueError("Tom inválido")
        else:
            return tom
