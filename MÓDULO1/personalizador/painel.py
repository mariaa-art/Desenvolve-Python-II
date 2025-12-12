from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def _ler_texto(texto: str, is_arquivo: bool) -> str:
    if is_arquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Erro ao ler arquivo: {e}"
    return texto

def painel_simples(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    console.print(Panel(conteudo, title="Painel Simples", subtitle="Fim da mensagem"))

def painel_pesado(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    console.print(Panel(conteudo, box=box.DOUBLE, style="red", title="IMPORTANTE"))