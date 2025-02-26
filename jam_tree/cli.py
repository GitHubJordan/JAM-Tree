import click
from pathlib import Path
from .directory_scanner import scan_directory
from .output_generator import print_tree, export_tree

# Lista padrão de diretórios a ignorar
DEFAULT_IGNORE = [".git", "venv", ".venv", "jenv", ".jenv", "__pycache__"]

@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False), default='.')
@click.option('--export', type=click.Choice(['txt', 'md', 'json']), help="Exporta a árvore para o formato especificado")
@click.option('--ignore', type=str, default="", help="Diretórios adicionais a ignorar, separados por vírgula (ex: node_modules,dist)")
def main(path, export, ignore):
    """
    JAM-Tree: Gerador de árvore de diretórios com análise de IA (versão CLI).

    PATH: Caminho do projeto a ser escaneado (padrão: diretório atual).
    """
    p = Path(path)
    
    # Cria a lista de ignorados com os padrões e acrescenta os fornecidos pelo usuário
    ignore_list = DEFAULT_IGNORE.copy()
    if ignore:
        additional_ignore = [d.strip() for d in ignore.split(',') if d.strip()]
        ignore_list.extend(additional_ignore)
    
    tree = scan_directory(p, ignore_dirs=ignore_list)
    root_name = p.resolve().name
    click.echo(print_tree(tree, root_name))
    
    if export:
        export_tree(tree, export, root_name=root_name)
        click.echo(f"\nÁrvore exportada para o formato {export} com sucesso.")

if __name__ == '__main__':
    main()
