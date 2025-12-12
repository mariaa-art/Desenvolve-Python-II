import time
from rich.console import Console
from rich.progress import track

console = Console()

def _ler_texto(texto: str, is_arquivo: bool) -> str:
    if is_arquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return "Erro."
    return texto

def barra_progresso(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    for _ in track(range(10), description="Processando..."):
        time.sleep(0.2) 
    console.print(conteudo)

def spinner_status(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    with console.status("[bold green]Lendo dados...") as status:
        time.sleep(2)
        console.print(f"[bold]Conteúdo:[/]\n{conteudo}")