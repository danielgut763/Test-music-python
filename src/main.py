from musica import Musica

texto = input("Digite o texto para transformar em música:\n")
bpm_inicial_input = input("Digite o BPM inicial desejado (padrão = 120): ")
instrumento_inicial_input = input("Digite o código do instrumento inicial desejado (padrão = 1, Acoustic Grand Piano): ")
oitava_inicial_input = input("Digite a oitava inicial desejada (padrão = 3): ")
volume_inicial_input = input("Digite o volume inicial desejado (padrão = 100): ")


try:
    bpm_inicial = int(bpm_inicial_input)
except ValueError:
    bpm_inicial = 120  # fallback caso digitem errado

try:
    instrumento_inicial = int(instrumento_inicial_input)
except ValueError:
    instrumento_inicial = 1 # fallback caso digitem errado

try:
    oitava_inicial = int(oitava_inicial_input)
except ValueError:
    oitava_inicial = 3 # fallback caso digitem errado

try:
    volume_inicial = int(volume_inicial_input)
except ValueError:
    volume_inicial = 100 # fallback caso digitem errado

musica = Musica(texto, bpm_inicial, instrumento_inicial, oitava_inicial, volume_inicial)
arquivo = musica.salvar_arquivo()

print(f"\n🎶 Arquivo gerado com sucesso: {arquivo}")
print("Faça o download e toque em qualquer player MIDI.")