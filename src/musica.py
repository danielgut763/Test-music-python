from midiutil import MIDIFile

from instrumento import Instrumento
from tom import Tom
from padrao_MIDI import *
from random import randint

# Canal e faixa de MIDI escolhidas para tocar a música
CANAL = 0
FAIXA = 0

# Duração escolhida para cada nota mapeada de um caractere do texto
DURACAO_NOTAS = 1

# Limites escolhidos para o valor de BPM
BPM_MINIMO = 40
BPM_MAXIMO = 240

# Nota escolhida para tocar o som de telefone
TELEFONE_TOCANDO_NOTA = 'A'

# Define o mapeamento entre caracteres e notas
MAPA_NOTAS = {
    'A':  NOTA_LA, 'a':  NOTA_LA, 
    'B': NOTA_SI, 'b': NOTA_SI, 
    'C':  NOTA_DO, 'c':  NOTA_DO,
    'D':  NOTA_RE, 'd':  NOTA_RE, 
    'E':  NOTA_MI, 'e': NOTA_MI, 
    'F':  NOTA_FA, 'f':  NOTA_FA,
    'G':  NOTA_SOL, 'g':  NOTA_SOL
}

class Musica:
    # Gera a musica a partir de um texto, um BPM inicial, um instrumento inicial, uma oitava inicial e um volume inicial
    def __init__(self, texto, bpm_inicial, instrumento_inicial, oitava_inicial, volume_inicial):
        self.midi = MIDIFile(1)
        bpm_atual = bpm_inicial
        instrumento_atual = instrumento_inicial
        oitava_atual = oitava_inicial
        volume_atual = volume_inicial
        tempo_atual = 0
        tom_anterior = None
        tom_atual = None

        # Define o instrumento inicial e o tempo no início da música (tempo 0)
        self.midi.addTempo(FAIXA, 0, bpm_atual)
        self.midi.addProgramChange(FAIXA, CANAL, 0, instrumento_atual.obter_valor_midi())

        for (posicao, caractere) in enumerate(texto):
            tom_atual = None

            if caractere in MAPA_NOTAS and texto[posicao:min(len(texto), posicao+4)] != "BPM+":
                nota = MAPA_NOTAS[caractere]
                tom_atual = Tom(nota, oitava_atual)
                self.midi.addNote(FAIXA, CANAL, tom_atual.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                tempo_atual += 1
            elif caractere == " ":
                tempo_atual += 1
            elif caractere == "+":
                if posicao >= 3 and texto[posicao-3:posicao+1] == "BPM+":
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
                if tom_anterior is not None:
                    self.midi.addNote(FAIXA, CANAL, tom_anterior.obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                    tempo_atual += 1
                else:
                    self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, Instrumento(CODIGO_INSTRUMENTO_TELEFONE_TOCANDO).obter_valor_midi())
                    self.midi.addNote(FAIXA, CANAL, Tom(TELEFONE_TOCANDO_NOTA, oitava_atual).obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
                    tempo_atual += 1
                    self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual.obter_valor_midi())
            elif caractere == '?':
                nota_escolhida = ['A', 'B', 'C', 'D', 'E', 'F', 'G'][randint(0, 6)]
                self.midi.addNote(FAIXA, CANAL, Tom(nota_escolhida, oitava_atual).obter_valor_midi(), tempo_atual, DURACAO_NOTAS, volume_atual)
            elif caractere == '\n':
                instrumento_atual.trocar()
                self.midi.addProgramChange(FAIXA, CANAL, tempo_atual, instrumento_atual.obter_valor_midi())
            elif caractere == ';':
                bpm_atual = randint(BPM_MINIMO, BPM_MAXIMO)
                self.midi.addTempo(FAIXA, tempo_atual, bpm_atual)
            
            tom_anterior = tom_atual

    def salvar_arquivo(self, nome="musica_gerada.mid"):
        with open(nome, "wb") as f:
            self.midi.writeFile(f)
        return nome
