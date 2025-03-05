import click
from pathlib import Path
from rich.console import Console
from rich.progress import Progress
from rich.status import Status
from .config import get_config_option
from .directory_scanner import scan_directory
from .output_generator import print_tree, export_tree
from .project_bootstrap import bootstrap_project
from .ai_analyzer import analyze_file, analyze_node, analyze_file_detailed

DEFAULT_IGNORE = get_config_option("ignore_dirs",["jenv", ".jenv", ".github", ".pytest_cache"])

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
@click.pass_context
def cli(ctx, path, export, ignore, create, no_root, ai_comments):
    """
    JAM-Tree: Gera a árvore completa de diretórios do projeto, exporta para diversos formatos,
    cria a estrutura do projeto a partir de um template JSON e analisa código com IA.

    Exemplos:
      jam-tree                             # Exibe a árvore do diretório atual.
      jam-tree --create template.json          # Cria a estrutura do projeto a partir do template.
      jam-tree --ai-comments                   # Exibe a árvore com resumos AI em cada nó.
      jam-tree --ai-comments --export md       # Exporta a árvore com resumos para Markdown.
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
        # Se desejado, podemos também integrar a barra de progresso (opcional, veja versão anterior)
        with console.status("[bold blue]Analisando nós com IA... 🤖[/bold blue]"):
            tree = annotate_tree(tree, p)

    root_name = p.resolve().name
    console.print(print_tree(tree, root_name))
    
    if export:
        export_tree(tree, export, root_name=root_name)
        console.print(f"[bold green]\nÁrvore exportada para o formato {export} com sucesso.[/bold green]")

@cli.command()
@click.argument('file', type=click.Path(exists=True, dir_okay=False))
@click.option('--export', type=click.Choice(['txt', 'md', 'json']), help="Exporta a análise detalhada para um arquivo")
def analyze(file, export):
    """
    Analisa detalhadamente um arquivo e retorna uma explicação completa.
    
    Se a opção --export for utilizada, salva a análise em um arquivo (por padrão, resume_file.txt).
    
    Exemplo:
      jam-tree analyze jam_tree/cli.py --export
    """
    console = Console()
    p = Path(file)
    with p.open("r", encoding="utf-8") as f:
        content = f.read()
    console.print("[bold blue]Analisando arquivo...🔍[/bold blue]")
    result = analyze_file_detailed(content)
    console.print("[bold blue]Análise detalhada do arquivo:[/bold blue]")
    console.print(result)
    
    if export:
        # Define o nome padrão do arquivo de exportação
        export_format = export
        if export_format == "txt":
            filename = "resume_file.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(result)
        elif export_format == "md":
            filename = "resume_file.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("# 🔍 Análise Detalhada do Arquivo\n\n")
                f.write(result)
        elif export_format == "json":
            filename = "resume_file.json"
            import json
            with open(filename, "w", encoding="utf-8") as f:
                json.dump({"analysis": result}, f, indent=2)
        console.print(f"[bold green]Análise exportada para {filename}.[/bold green]")

if __name__ == '__main__':
    cli()
