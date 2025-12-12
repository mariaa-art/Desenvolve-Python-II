import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_instrucoes(caminho_arquivo: str):
   
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            texto = f.read()
        console.print(Panel(texto, title="Instruções", style="bold cyan"))
    except FileNotFoundError:
        console.print("[red]Arquivo de instruções não encontrado![/]")

def contagem_regressiva(n: int):
    if n <= 0:
        console.print("[bold green]VAI![/]")
        time.sleep(1)
        return
    
    console.print(f"[bold yellow]{n}...[/]")
    time.sleep(1)
    contagem_regressiva(n - 1) # CVhama a si mesma

def exibir_menu_inicial(nome_jogador: str):
    limpar_tela()
    console.print(Panel(f"Olá, [bold magenta]{nome_jogador}[/]!\nBem-vindo à Aventura no Labirinto", style="green"))
    print("\n1. Jogar")
    print("2. Instruções")
    print("3. Sair")