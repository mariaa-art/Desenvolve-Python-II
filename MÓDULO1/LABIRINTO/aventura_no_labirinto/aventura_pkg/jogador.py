def iniciar_jogador(labirinto: list) -> list:
    for l, linha in enumerate(labirinto):
        for c, item in enumerate(linha):
            if item == 'S':
                return [l, c]
    return [1, 1] # Padrão se não achar

def mover(posicao_atual: list, direcao: str, labirinto: list) -> list:
    l, c = posicao_atual
    novo_l, novo_c = l, c
    match direcao:
        case 'w': novo_l -= 1
        case 's': novo_l += 1
        case 'a': novo_c -= 1
        case 'd': novo_c += 1
        case _: return posicao_atual # Tecla inválida, não mEXE

    if labirinto[novo_l][novo_c] != '#':
        return [novo_l, novo_c]
    
    return posicao_atual