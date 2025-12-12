import argparse
from personalizador import layout, painel, progresso, estilo

MODULOS = {
    'layout': layout,    '1': layout,
    'painel': painel,    '2': painel,
    'progresso': progresso, '3': progresso,
    'estilo': estilo,    '4': estilo
}

FUNCOES = {
    'layout': {
        '1': layout.dividir_colunas, 'colunas': layout.dividir_colunas,
        '2': layout.layout_centralizado, 'central': layout.layout_centralizado
    },
    'painel': {
        '1': painel.painel_simples, 'simples': painel.painel_simples,
        '2': painel.painel_pesado, 'pesado': painel.painel_pesado
    },
    'progresso': {
        '1': progresso.barra_progresso, 'barra': progresso.barra_progresso,
        '2': progresso.spinner_status, 'spinner': progresso.spinner_status
    },
    'estilo': {
        '1': estilo.estilo_negrito_azul, 'azul': estilo.estilo_negrito_azul,
        '2': estilo.estilo_emoji, 'emoji': estilo.estilo_emoji
    }
}

def main():
    parser = argparse.ArgumentParser(description="Formatador de texto com Rich")
    parser.add_argument("texto", help="Texto ou caminho do arquivo para imprimir.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica se o texto é um caminho de arquivo.")
    parser.add_argument("-m", "--modulo", default="estilo", 
                        help="Escolha: layout(1), painel(2), progresso(3), estilo(4)")
    parser.add_argument("-f", "--funcao", default="1", 
                        help="Escolha a função: 1 ou 2 (nomes variam por módulo)")
    args = parser.parse_args()

    if args.modulo in MODULOS:
        modulo_selecionado = MODULOS[args.modulo]
        nome_modulo = modulo_selecionado.__name__.split('.')[-1]
        
        funcs_disponiveis = FUNCOES.get(nome_modulo)
        
        if funcs_disponiveis and args.funcao in funcs_disponiveis:
            funcao_escolhida = funcs_disponiveis[args.funcao]
            funcao_escolhida(args.texto, args.arquivo)
        else:
            print(f"Função '{args.funcao}' não encontrada no módulo '{nome_modulo}'.")
            print(f"Opções: {list(funcs_disponiveis.keys())}")
    else:
        print(f"Módulo '{args.modulo}' não encontrado.")

if __name__ == "__main__":
    main()