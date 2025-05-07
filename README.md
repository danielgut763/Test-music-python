# 🎼 Gerador de Música a Partir de Texto

Transforme texto comum em música! Este projeto em Python gera arquivos `.mid` (MIDI) com base em um texto qualquer, seguindo regras que mapeiam letras e símbolos para notas, pausas, instrumentos e efeitos musicais.

> 💡 Feito para a disciplina **INF01120 – Técnicas de Construção de Programas** – UFRGS

---

## 🚀 Como Rodar o Projeto

### ✅ Pré-requisitos

- Python 3.7 ou superior instalado
- Git (ou baixe o `.zip` do repositório)

---

### 📥 Passo 1: Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

---

### 🧪 Passo 2: (Opcional) Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

---

### 📦 Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

> Se não existir `requirements.txt`, crie com:
```bash
pip install pygame MIDIUtil
pip freeze > requirements.txt
```

---

### 🖥️ Passo 4: Rodar o programa (modo terminal)

```bash
python gerar_musica_simples.py
```

- Digite seu texto musical quando solicitado
- Escolha o BPM (velocidade)
- Será gerado um arquivo `musica_gerada.mid`

🎧 **Toque o arquivo em:**
- Players MIDI (VLC, Windows Media Player, etc)
- DAWs (como LMMS, FL Studio)

---

## ⚠️ Dica para GitHub Codespaces

Como ambientes remotos não suportam áudio nem interface gráfica, use **apenas** o arquivo `gerar_musica_simples.py` para gerar `.mid`, e depois baixe o arquivo pelo menu lateral.

---

## 🔤 Mapeamento de Caracteres

| Caractere        | Ação Musical                                |
|------------------|---------------------------------------------|
| A – G (maiúsculo)| Notas musicais (A = Lá, B = Si, etc)        |
| H                | Si bemol (Bb)                               |
| a – g (minúsculo)| Pausa/silêncio                              |
| Espaço (` `)     | Aumenta o volume                            |
| `!`              | Instrumento 24 (Bandoneon)                  |
| `oOiIuU`         | Instrumento 110 (Gaita de Foles)            |
| Dígito par       | Soma ao instrumento atual                   |
| Dígito ímpar / `;` | Instrumento 15 (Tubular Bells)           |
| `,`              | Instrumento 114 (Agogô)                     |
| `.` ou `?`       | Sobe uma oitava (ou reinicia)               |
| `\n` (nova linha)| Instrumento 123 (Ondas do Mar)              |
| Outro            | Repete última nota ou pausa                 |

---

## 🎵 Exemplos de Texto Musical

### 🔹 Exemplo basico

```
E E a E a C E G a G a
G A G F E C E A B H A
```
