from musica import Musica
from instrumento import Instrumento

# texto = open("doremifa.txt").read()
texto = open("halloween.txt").read()
# texto = input("Digite o texto para transformar em música:\n")


bpm_inicial_input = input("Digite o BPM inicial desejado (padrão = 120): ")
if bpm_inicial_input == '':
    bpm_inicial = 120  # fallback caso digitem errado
else:
    try:
        bpm_inicial = int(bpm_inicial_input)
    except ValueError:
        print("BPM inválido")
        exit(1)

codigo_instrumento_inicial_input = input("Digite o código do instrumento inicial desejado (padrão = 1, Acoustic Grand Piano): ")
if codigo_instrumento_inicial_input == '':
    instrumento_inicial = Instrumento(1) # fallback caso digitem errado
else:
    try:
        instrumento_inicial = Instrumento(int(codigo_instrumento_inicial_input))
    except ValueError:
        print("Código de instrumento inválido")
        exit(1)

oitava_inicial_input = input("Digite a oitava inicial desejada (padrão = 3): ")
if oitava_inicial_input == '':
    oitava_inicial = 3 # fallback caso digitem errado
else:
    try:
        oitava_inicial = int(oitava_inicial_input)
    except ValueError:
        print("Oitava inválida")
        exit(1)

volume_inicial_input = input("Digite o volume inicial desejado (padrão = 100): ")
try:
    volume_inicial = int(volume_inicial_input)
except ValueError:
    volume_inicial = 100 # fallback caso digitem errado

try:
    musica = Musica(texto, bpm_inicial, instrumento_inicial, oitava_inicial, volume_inicial)
except ValueError as excecao:
    print("Arquivo de música inválido:", end='')
    if excecao.args == ("Tom inválido"):
        print(": tenta gerar um uma nota com oitava inválida", end='')
    elif excecao.args == ("Instrumento inválido"):
        print(": tenta gerar um uma nota com oitava inválida", end='')
    else:
        print("erro desconhecido")
    
    print()
    exit(1)

arquivo = musica.salvar_arquivo()

print(f"\n🎶 Arquivo gerado com sucesso: {arquivo}")
print("Faça o download e toque em qualquer player MIDI.")