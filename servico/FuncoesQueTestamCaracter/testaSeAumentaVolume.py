def testa_se_aumenta_volume(nota, volume):
  if nota == ' ':
    volume = min(127, volume * 2)
    return True
  return False