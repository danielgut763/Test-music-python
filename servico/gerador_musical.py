from midiutil import MIDIFile

from musicaClasses.instrumento import Instrumento
from musicaClasses.nota import Nota
from servico.FuncoesQueTestamCaracter.testaSeAumentaVolume import testa_se_aumenta_volume
from servico.FuncoesQueTestamCaracter.testaSeFim import testa_se_fim
from servico.FuncoesQueTestamCaracter.testaSeNovoInstrumento import testa_se_novo_instrumento
from servico.FuncoesQueTestamCaracter.testaSePausa import testa_se_pausa
from servico.FuncoesQueTestamCaracter.testaSeSobeOitava import testa_se_sobe_oitava

class GeradorMusical:
    def __init__(self, texto, bpm):
        self.texto = texto
        self.midi = MIDIFile(1)
        self.tempo = bpm
        self.canal = 0
        self.volume = 100
        self.oitava = 0
        self.instrumento = Instrumento()
        self.nota_atual = 0
        self.ultima_nota = None

        # Definindo o instrumento inicial e o tempo
        self.midi.addTempo(0, 0, self.tempo)
        self.midi.addProgramChange(0, self.canal, 0, self.instrumento.valor)

    def processar(self):
        for nota in self.texto:
            nota = Nota(nota, self.oitava).obter_valor_midi()

            if nota:
                self.midi.addNote(0, self.canal, nota, self.nota_atual, 1, self.volume)
                self.ultima_nota = nota
                self.nota_atual += 1
                testa_se_pausa(nota, self.nota_atual)
                testa_se_aumenta_volume(nota, self.volume)
                testa_se_novo_instrumento(nota, self.instrumento, self.midi, self.canal, self.nota_atual)
                testa_se_sobe_oitava(nota, self.oitava)
                
            else:
                testa_se_fim(self.nota_atual, self.midi, self.canal, self.ultima_nota, self.volume)

    def salvar_arquivo(self, nome="musica_gerada.mid"):
        with open(nome, "wb") as f:
            self.midi.writeFile(f)
        return nome
