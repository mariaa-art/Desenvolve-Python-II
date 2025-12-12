from rich.console import Console
from rich.panel import Panel

console = Console()

def criar_labirinto() -> list:
    """
    A matriz usa:
    '#' = Parede (Bloco)
    ' ' = Caminho Livre
    'S' = Início (Start)
    'E' = Fim (End/Saída)
    
    """
   
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', '#', 'E', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    return labirinto

def gerar_painel_labirinto(labirinto: list, jogador_pos: list, cor_parede: str) -> Panel:
    texto_saida = ""
    
    # Percorre a matriz (l = linha, c = coluna)
    for l, linha in enumerate(labirinto):
        for c, item in enumerate(linha):
            
            if l == jogador_pos[0] and c == jogador_pos[1]:
                texto_saida += "[bold yellow]☺[/] " # O Jogador
            
            elif item == '#':
                texto_saida += f"[{cor_parede}]█[/] " # Parede com cor dinâmica
            
    
            elif item == 'S':
                texto_saida += "[green]S[/] "
            elif item == 'E':
                texto_saida += "[bold red]E[/] "
       
            else:
                texto_saida += "  " 
                
        texto_saida += "\n" 
    
    return Panel(texto_saida, title="Labirinto", expand=False)