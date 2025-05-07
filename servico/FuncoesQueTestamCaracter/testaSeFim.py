def testa_se_fim(notaAtual, midi, canal, ultimaNota, volume):
  if ultimaNota:
    midi.addNote(0, canal, ultimaNota, notaAtual, 1, volume)
  else:
    notaAtual += 1