from rich.console import Console

console = Console()

def _ler_texto(texto: str, is_arquivo: bool) -> str:
    if is_arquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return "Erro de leitura."
    return texto

def estilo_negrito_azul(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    console.print(f"[bold blue on white]{conteudo}[/]")

def estilo_emoji(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    console.print(f":snake: [italic green]{conteudo}[/] :snake:")