import argparse
import sys
import time
from pynput import keyboard
from rich.console import Console
from rich.live import Live  
from aventura_pkg import labirinto, jogador, utils

console = Console()
estado = {
    "posicao": [1, 1],
    "labirinto": [],
    "jogando": True,
    "vitoria": False,
    "cor": "blue"
}

def on_release(key):
    global estado
    try:
        if key == keyboard.Key.esc:
            estado["jogando"] = False
            return False 

        char = key.char.lower()
        if char in ['w', 'a', 's', 'd']:
            nova_pos = jogador.mover(estado["posicao"], char, estado["labirinto"])
            estado["posicao"] = nova_pos
            
            l, c = nova_pos
            if estado["labirinto"][l][c] == 'E':
                estado["vitoria"] = True
                estado["jogando"] = False
                return False 
    except AttributeError:
        pass

def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do Jogador")
    parser.add_argument("--color", default="blue", help="Cor das paredes")
    args = parser.parse_args()
    estado["cor"] = args.color

    while True:
        utils.exibir_menu_inicial(args.name)
        opcao = input("Escolha: ")
        if opcao == '1': break
        elif opcao == '2': 
            utils.limpar_tela()
            utils.imprimir_instrucoes("instrucoes.txt") 
            input("Enter para voltar...")
        elif opcao == '3': sys.exit()

    # Preparação
    utils.limpar_tela()
    utils.contagem_regressiva(3)
    
    estado["labirinto"] = labirinto.criar_labirinto()
    estado["posicao"] = jogador.iniciar_jogador(estado["labirinto"])
    
    print("\nUse W, A, S, D para mover. ESC para sair.")

    painel_inicial = labirinto.gerar_painel_labirinto(estado["labirinto"], estado["posicao"], estado["cor"])
    
    listener = keyboard.Listener(on_release=on_release)
    listener.start()

    with Live(painel_inicial, refresh_per_second=10, screen=True) as live_view:
        while estado["jogando"]:
            painel = labirinto.gerar_painel_labirinto(estado["labirinto"], estado["posicao"], estado["cor"])
            live_view.update(painel)
            time.sleep(0.05) 

    listener.join()

    utils.limpar_tela()
    if estado["vitoria"]:
        console.print(f"[bold green]PARABÉNS {args.name}! VOCÊ VENCEU![/]")
    else:
        console.print("[bold red]Jogo encerrado.[/]")

if __name__ == "__main__":
    main()