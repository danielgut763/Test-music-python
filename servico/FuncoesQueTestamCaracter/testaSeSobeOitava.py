def testa_se_sobe_oitava(nota, oitava):
    if nota in ['.','?']:
        oitava = oitava + 12 if oitava + 12 <= 127 else 0
        return True
    return False