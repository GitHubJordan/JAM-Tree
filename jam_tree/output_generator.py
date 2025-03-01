def sort_key(item):
    """
    Retorna uma chave para ordenação:
      - Diretórios (nós que possuem "children") recebem prioridade 0.
      - Arquivos (nós com "type" == "file") recebem prioridade 1.
    A ordenação interna é feita de forma alfabética, ignorando maiúsculas/minúsculas.
    """
    name, value = item
    if isinstance(value, dict):
        if "children" in value:
            return (0, name.lower())
        if "type" in value and value["type"] == "file":
            return (1, name.lower())
        # Caso não esteja anotado, trata como diretório por padrão
        return (0, name.lower())
    return (1, name.lower())

def format_tree(tree: dict, prefix: str = "", is_root: bool = True) -> str:
    """
    Converte recursivamente a estrutura em árvore em uma string formatada.
    
    A estrutura pode ser:
      - Não anotada: diretórios são dicionários e arquivos são representados pela string "file".
      - Anotada: para arquivos, { "type": "file", "comment": <comentário> };
                   para diretórios, { "children": { ... }, "comment": <comentário> }.
    
    Diretórios são listados primeiro (prioridade 0) e, em seguida, os arquivos (prioridade 1),
    ambos em ordem alfabética.
    Se houver um comentário, ele é exibido ao lado do nome do nó.
    """
    lines = []
    items = sorted(tree.items(), key=sort_key)
    
    for index, (name, value) in enumerate(items):
        is_last = (index == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        if isinstance(value, dict):
            if "type" in value and value["type"] == "file":
                # Nó de arquivo anotado
                comment = value.get("comment", "")
                line = f"{prefix}{connector}{name}                # {comment}"
            else:
                # Nó de diretório (anotado ou não)
                comment = value.get("comment", "") if "children" in value else ""
                line = f"{prefix}{connector}{name}/"
                if comment:
                    line += f"                # {comment}"
        else:
            line = f"{prefix}{connector}{name}"
        lines.append(line)
        
        # Se for um diretório, processa recursivamente seus filhos
        if isinstance(value, dict):
            children = value.get("children", value)
            if not (isinstance(value, dict) and "type" in value and value["type"] == "file"):
                extension = "    " if is_last else "│   "
                sub_tree = format_tree(children, prefix + extension, is_root=False)
                if sub_tree:
                    lines.append(sub_tree)
    return "\n".join(lines)

def print_tree(tree: dict, root_name: str = "") -> str:
    """
    Retorna uma string representando a árvore do projeto formatada.
    Se root_name for fornecido, ele é exibido como o diretório principal.
    """
    output = ""
    if root_name:
        output += f"{root_name}/                 # Pasta principal do projeto\n"
    output += format_tree(tree, is_root=True)
    return output

def export_tree(tree: dict, format: str, filename: str = "project_tree", root_name: str = ""):
    """
    Exporta a árvore para um arquivo nos formatos TXT, Markdown ou JSON.
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
