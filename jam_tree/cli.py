import click
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from rich.status import Status
from .directory_scanner import scan_directory
from .output_generator import print_tree, export_tree
from .project_bootstrap import bootstrap_project
from .ai_analyzer import analyze_file, analyze_node, analyze_file_detailed

DEFAULT_IGNORE = [".git", "venv", ".venv", "jenv", ".jenv", "__pycache__", ".github", ".pytest_cache"]

def annotate_tree(tree: dict, base_path: Path) -> dict:
    annotated = {}
    for name, subtree in tree.items():
        full_path = base_path / name
        if full_path.is_file():
            comment = analyze_file(full_path.read_text(encoding="utf-8"))
            annotated[name] = {"type": "file", "comment": comment}
        elif full_path.is_dir():
            comment = analyze_node(name, True)
            children = annotate_tree(subtree, full_path)
            annotated[name] = {"children": children, "comment": comment}
        else:
            annotated[name] = subtree
    return annotated

def annotate_tree_with_progress(tree: dict, base_path: Path, progress: Progress, task_id) -> dict:
    annotated = {}
    items = list(tree.items())
    for name, subtree in items:
        progress.update(task_id, advance=1)
        full_path = base_path / name
        if full_path.is_file():
            comment = analyze_file(full_path.read_text(encoding="utf-8"))
            annotated[name] = {"type": "file", "comment": comment}
        elif full_path.is_dir():
            comment = analyze_node(name, True)
            children = annotate_tree_with_progress(subtree, full_path, progress, task_id)
            annotated[name] = {"children": children, "comment": comment}
        else:
            annotated[name] = subtree
    return annotated

@click.group(invoke_without_command=True)
@click.argument('path', type=click.Path(exists=True, file_okay=False), default='.')
@click.option('--export', type=click.Choice(['txt', 'md', 'json']), help="Exporta a árvore para o formato especificado")
@click.option('--ignore', type=str, default="", help="Diretórios adicionais a ignorar, separados por vírgula")
@click.option('--create', type=click.Path(exists=True), help="Arquivo JSON com a estrutura inicial do projeto")
@click.option('--no-root', is_flag=True, default=False, help="Não criar a pasta raiz; utiliza o diretório atual como raiz do projeto")
@click.option('--ai-comments', is_flag=True, default=False, help="Anexa breves descrições AI aos nós da árvore")
@click.option('--progress', is_flag=True, default=False, help="Exibe barra de progresso durante a análise AI")
@click.pass_context
def cli(ctx, path, export, ignore, create, no_root, ai_comments, progress):
    """
    JAM-Tree: Gera a árvore de diretórios do projeto, exporta para diversos formatos,
    cria a estrutura do projeto a partir de um template JSON e analisa código com IA.

    Exemplos:

      jam-tree .
      jam-tree --create template.json
      jam-tree --ai-comments
      jam-tree --ai-comments --progress
    """
    console = Console()
    if ctx.invoked_subcommand is not None:
        return

    if create:
        console.print("[bold green]Criando a estrutura do projeto... 🚀[/bold green]")
        root_path = bootstrap_project(create, create_root=not no_root)
        console.print(f"[bold green]Estrutura criada em:[/bold green] {root_path.resolve()}")
        return

    p = Path(path)
    ignore_list = DEFAULT_IGNORE.copy()
    if ignore:
        ignore_list.extend([d.strip() for d in ignore.split(',') if d.strip()])

    with console.status("[bold green]Escaneando diretórios... 🔍[/bold green]"):
        tree = scan_directory(p, ignore_dirs=ignore_list)

    if ai_comments:
        if progress:
            with Progress() as prog:
                task_id = prog.add_task("[bold blue]Analisando nós...[/bold blue]", total=len(tree))
                tree = annotate_tree_with_progress(tree, p, prog, task_id)
        else:
            with console.status("[bold blue]Analisando nós...🤖[/bold blue]"):
                tree = annotate_tree(tree, p)

    root_name = p.resolve().name
    console.print(print_tree(tree, root_name))

    if export:
        export_tree(tree, export, root_name=root_name)
        console.print(f"[bold green]\nÁrvore exportada para o formato {export} com sucesso.[/bold green]")

@cli.command()
@click.argument('file', type=click.Path(exists=True, dir_okay=False))
def analyze(file):
    """
    Analisa detalhadamente um arquivo e retorna uma explicação completa.

    Exemplo:
      jam-tree analyze caminho/do/arquivo.py
    """
    console = Console()
    p = Path(file)
    with p.open("r", encoding="utf-8") as f:
        content = f.read()
    console.print("[bold blue]Analisando arquivo...🔍[/bold blue]")
    result = analyze_file_detailed(content)
    console.print("[bold blue]Análise detalhada do arquivo:[/bold blue]")
    console.print(result)

if __name__ == '__main__':
    cli()
