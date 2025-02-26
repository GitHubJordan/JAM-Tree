# jam_tree/output_generator.py
from rich.console import Console

def format_tree(tree: dict, prefix: str = "", is_root: bool = True) -> str:
    """
    Converte recursivamente a estrutura em árvore (dicionário) em uma string formatada,
    listando primeiro os diretórios e depois os arquivos.
    
    :param tree: Dicionário representando a árvore.
    :param prefix: Prefixo para indentação.
    :param is_root: Flag para identificar se estamos no primeiro nível.
    :return: String com a árvore formatada.
    """
    lines = []
    # Ordena: diretórios primeiro (valor é dict) e, depois, arquivos; em ordem alfabética.
    items = sorted(tree.items(), key=lambda item: (0 if isinstance(item[1], dict) else 1, item[0].lower()))
    
    for index, (name, content) in enumerate(items):
        is_last = (index == len(items) - 1)
        if is_root:
            # No primeiro nível, usamos o prefixo "│── " conforme desejado.
            line = f"│── {name}" + ("/" if isinstance(content, dict) else "")
        else:
            connector = "└── " if is_last else "├── "
            line = prefix + connector + name + ("/" if isinstance(content, dict) else "")
        lines.append(line)
        if isinstance(content, dict):
            extension = "    " if is_last else "│   "
            sub_tree = format_tree(content, prefix + extension, is_root=False)
            if sub_tree:
                lines.append(sub_tree)
    return "\n".join(lines)

def print_tree(tree: dict, root_name: str = "") -> str:
    """
    Retorna uma string representando a árvore do projeto formatada.
    
    Se root_name for fornecido, ele será exibido como o diretório principal.
    """
    output = ""
    if root_name:
        output += f"{root_name}/                 # Pasta principal do projeto\n"
    output += format_tree(tree, is_root=True)
    return output

def export_tree(tree: dict, format: str, filename: str = "project_tree", root_name: str = ""):
    """
    Exporta a árvore para um arquivo nos formatos TXT, Markdown ou JSON.
    
    :param tree: Estrutura em árvore (dicionário).
    :param format: Formato de exportação ('txt', 'md', 'json').
    :param filename: Nome base do arquivo exportado.
    :param root_name: Nome do diretório principal.
    """
    tree_str = print_tree(tree, root_name)
    if format == "txt":
        with open(f"{filename}.txt", "w", encoding="utf-8") as f:
            f.write(tree_str)
    elif format == "md":
        with open(f"{filename}.md", "w", encoding="utf-8") as f:
            f.write("# Estrutura do Projeto\n\n")
            f.write("```\n" + tree_str + "\n```\n")
    elif format == "json":
        import json
        with open(f"{filename}.json", "w", encoding="utf-8") as f:
            json.dump(tree, f, indent=2)
