from midiutil import MIDIFile
from nota import Nota
from instrumento import Instrumento

class GeradorMusical:
    def __init__(self, texto):
        self.texto = texto
        self.midi = MIDIFile(1)
        self.tempo = 120
        self.canal = 0
        self.volume = 100
        self.oitava = 0
        self.instrumento = Instrumento()
        self.tempo_atual = 0
        self.ultima_nota = None

        self.midi.addTempo(0, 0, self.tempo)
        self.midi.addProgramChange(0, self.canal, 0, self.instrumento.valor)

    def processar(self):
        for c in self.texto:
            nota = Nota(c, self.oitava).obter_valor_midi()

            if nota:
                self.midi.addNote(0, self.canal, nota, self.tempo_atual, 1, self.volume)
                self.ultima_nota = nota
                self.tempo_atual += 1

            elif c in 'abcdefg':
                self.tempo_atual += 1

            elif c == ' ':
                self.volume = min(127, self.volume * 2)

            elif c in '!oOiIuU\n;,0123456789':
                novo_instr = self.instrumento.trocar(c, self.instrumento.valor)
                self.midi.addProgramChange(0, self.canal, self.tempo_atual, novo_instr)

            elif c in '.?':
                self.oitava = self.oitava + 12 if self.oitava + 12 <= 127 else 0

            else:
                if self.ultima_nota:
                    self.midi.addNote(0, self.canal, self.ultima_nota, self.tempo_atual, 1, self.volume)
                else:
                    self.tempo_atual += 1

    def salvar_arquivo(self, nome="musica_gerada.mid"):
        with open(nome, "wb") as f:
            self.midi.writeFile(f)
        return nome
