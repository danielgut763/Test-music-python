import os
import pygame
import tkinter as tk
from tkinter import messagebox
from gerador_musical import GeradorMusical

midi_path = None

def gerar_musica():
    texto = texto_input.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite algum texto.")
        return

    gerador = GeradorMusical(texto)
    gerador.processar()
    global midi_path
    midi_path = gerador.salvar_arquivo()
    messagebox.showinfo("Sucesso", f"Arquivo salvo: {midi_path}")

def tocar_musica():
    if not midi_path or not os.path.exists(midi_path):
        messagebox.showerror("Erro", "Arquivo MIDI não encontrado.")
        return

    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(midi_path)
        pygame.mixer.music.play()
        messagebox.showinfo("Reproduzindo", "Música sendo tocada...")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao tocar: {e}")

# Interface com Tkinter
root = tk.Tk()
root.title("Gerador de Música a partir de Texto")
root.geometry("600x400")

label = tk.Label(root, text="Digite o texto:")
label.pack()

texto_input = tk.Text(root, height=12, width=70)
texto_input.pack(pady=5)

botao_gerar = tk.Button(root, text="🎼 Gerar Música", command=gerar_musica)
botao_gerar.pack(pady=10)

botao_tocar = tk.Button(root, text="▶️ Tocar Música", command=tocar_musica)
botao_tocar.pack()

root.mainloop()
