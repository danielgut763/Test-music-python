def testa_se_novo_instrumento(nota, instrumento, midi, canal, nota_atual):
    if nota in ['!', 'o', 'O', 'i', 'I', 'u', 'U', '/n', ';', ',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        novo_instr = instrumento.trocar(nota, instrumento.valor)
        midi.addProgramChange(0, canal, nota_atual, novo_instr)
        return True
    return False