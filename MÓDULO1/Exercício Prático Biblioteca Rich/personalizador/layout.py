from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

def _ler_texto(texto: str, is_arquivo: bool) -> str:
    if is_arquivo:
        try:
            with open(texto, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: Arquivo não encontrado."
    return texto

def dividir_colunas(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    
    layout = Layout()
    layout.split_row(
        Layout(Panel(conteudo, title="Original")),
        Layout(Panel(conteudo[::-1], title="Invertido"))
    )
    console.print(layout)

def layout_centralizado(texto: str, is_arquivo: bool):
    conteudo = _ler_texto(texto, is_arquivo)
    
    layout = Layout()
    layout.split_column(
        Layout(name="topo"),
        Layout(Panel(conteudo, title="Centralizado"), size=10),
        Layout(name="base")
    )
    console.print(layout)