from servico.gerador_musical import GeradorMusical


texto = input("Digite o texto para transformar em música:\n")
bpm_input = input("Digite o BPM desejado (padrão = 120): ")

try:
    bpm = int(bpm_input)
except ValueError:
    bpm = 120  # fallback caso digitem errado

gerador = GeradorMusical(texto, bpm)
gerador.processar()
arquivo = gerador.salvar_arquivo()

print(f"\n🎶 Arquivo gerado com sucesso: {arquivo}")
print("Faça o download e toque em qualquer player MIDI.")