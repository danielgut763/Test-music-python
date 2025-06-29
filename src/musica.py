from midiutil import MIDIFile

from instrumento import Instrumento
from nota import Nota
from random import randint

# Canal e faixa de MIDI em que a música vai tocar
CANAL = 0
FAIXA = 0

# Duração de cada nota mapeada de um caractere do texto
DURACAO_NOTAS = 1

# Definidos pelo padrão MIDI
INSTRUMENTO_MINIMO = 0
INSTRUMENTO_MAXIMO = 127
OITAVA_MINIMA = -2
OITAVA_MAXIMA = 8
VOLUME_MAXIMO = 127

# Limite para o valor de BPM
BPM_MINIMO = 40
BPM_MAXIMO = 240

# Definições para o som de telefone
TELEFONE_TOCANDO_INSTRUMENTO = 125
TELEFONE_TOCANDO_NOTA = "A"

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

        for (posicao, caractere) in enumerate(texto):
            nota_atual = None

            if caractere in "AaBbCcDdEeFfGg" and texto[posicao:min(len(texto), posicao+4)] != "BPM+":
                nota_atual = Nota(caractere, oitava_atual)
                self.midi.addNote(FAIXA, CANAL, nota_atual.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                tempo_atual += 1
            elif caractere == " ":
                tempo_atual += 1
            elif caractere == "+":
                if posicao >= 3 and texto[posicao-3:posicao]:
                    bpm_atual += 80
                    if bpm_atual > BPM_MAXIMO:
                        bpm_atual = BPM_MAXIMO
                    self.midi.addTempo(FAIXA, tempo_atual, bpm_atual)
                if posicao >= 1 and texto[posicao-1] == 'R':
                    oitava_atual += 1
                    if oitava_atual > OITAVA_MAXIMA:
                        oitava_atual = OITAVA_MAXIMA
                else:
                    volume_atual *= 2
                    if volume_atual > VOLUME_MAXIMO:
                        volume_atual = VOLUME_MAXIMO
            elif caractere == "-":
                if posicao >= 1 and texto[posicao-1] == 'R':
                    oitava_atual -= 1
                    if oitava_atual < OITAVA_MINIMA:
                        oitava_atual = OITAVA_MINIMA
                else:
                    volume_atual = volume_inicial
            elif caractere in "OoIiUu":
                if nota_anterior is not None:
                    self.midi.addNote(FAIXA, CANAL, nota_anterior.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                    tempo_atual += 1
                else:
                    self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, TELEFONE_TOCANDO_INSTRUMENTO)
                    self.midi.addNote(FAIXA, CANAL, Nota(TELEFONE_TOCANDO_NOTA, oitava_atual).obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                    tempo_atual += 1
                    self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual)
            elif caractere == '?':
                nota_escolhica = ['A', 'B', 'C', 'D', 'E', 'F', 'G'][randint(0, 6)]
                self.midi.addNote(FAIXA, CANAL, Nota(nota_escolhica, oitava_atual).obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
            elif caractere == '\n':
                instrumento_atual += 1
                if instrumento_atual > INSTRUMENTO_MAXIMO:
                    instrumento_atual = INSTRUMENTO_MINIMO
            elif caractere == ';':
                bpm_atual = randint(BPM_MINIMO, BPM_MAXIMO)
                self.midi.addTempo(FAIXA, tempo_atual, bpm_atual)
            
            nota_anterior = nota_atual

    def salvar_arquivo(self, nome="musica_gerada.mid"):
        with open(nome, "wb") as f:
            self.midi.writeFile(f)
        return nome
