from midiutil import MIDIFile

from instrumento import Instrumento
from nota import Nota

# Canal e faixa de MIDI em que a música vai tocar
CANAL = 0
FAIXA = 0

# Duração de cada nota mapeada de um caractere do texto
DURACAO_NOTAS = 1

# Definidos pelo padrão MIDI
OITAVA_MAXIMA = 8
VOLUME_MAXIMO = 127

class Musica:
    # Gera a musica a partir de um texto, um BPM inicial, um instrumento inicial, uma oitava inicial e um volume inicial
    def __init__(self, texto, bpm_inicial, instrumento_inicial, oitava_inicial, volume_inicial):
        self.midi = MIDIFile(1)
        bpm_atual = bpm_inicial
        instrumento_atual = instrumento_inicial
        oitava_atual = oitava_inicial
        volume_atual = volume_inicial
        tempo_atual = 0
        nota_anterior = None
        nota_atual = None

        # Define o instrumento inicial e o tempo no início da música (tempo 0)
        self.midi.addTempo(FAIXA, 0, bpm_atual)
        self.midi.addProgramChange(FAIXA, CANAL, 0, instrumento_atual)

        for caractere in texto:
            nota_atual = None

            if caractere in "ABCDEFGH":
                nota_atual = Nota(caractere, oitava_atual)
                self.midi.addNote(FAIXA, CANAL, nota_atual.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                tempo_atual += 1
            elif caractere in "abcdefgh":
                tempo_atual += 1
            elif caractere == " ":
                volume_atual *= 2
                if volume_atual > VOLUME_MAXIMO:
                    volume_atual = VOLUME_MAXIMO
            elif caractere == "!":
                instrumento_atual = 24
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            elif caractere in "OoIiUu":
                instrumento_atual = 110
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            elif caractere in "02468":
                # TODO limite
                instrumento_atual += int(caractere)
            elif caractere in "?.":
                oitava_atual += 1
                if oitava_atual > OITAVA_MAXIMA:
                    oitava_atual = oitava_inicial
            elif caractere == '\n':
                instrumento_atual = 123
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            elif caractere in ";13579":
                instrumento_atual = 15
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            elif caractere == ',':
                instrumento_atual = 114
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            else:
                if nota_anterior is not None:
                    self.midi.addNote(FAIXA, CANAL, nota_anterior.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                tempo_atual += 1
            
            nota_anterior = nota_atual

    def salvar_arquivo(self, nome="musica_gerada.mid"):
        with open(nome, "wb") as f:
            self.midi.writeFile(f)
        return nome
