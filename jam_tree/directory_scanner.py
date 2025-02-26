from pathlib import Path
from typing import Dict, Union, List

def scan_directory(path: Path, ignore_dirs: List[str] = None) -> Dict[str, Union[str, dict]]:
    """
    Percorre recursivamente o diretório e gera uma estrutura em árvore.

    :param path: Caminho inicial para escanear.
    :param ignore_dirs: Lista de nomes de diretórios a serem ignorados.
                        Padrão: [".git", "venv", "__pycache__"]
                        Diretórios que terminam com ".egg-info" também são ignorados.
    :return: Dicionário representando a árvore do projeto.
    """
    if ignore_dirs is None:
        ignore_dirs = [".git", "venv", "__pycache__", ".jenv"]
    structure = {}
    for item in path.iterdir():
        # Ignorar diretórios especificados ou que terminem com ".egg-info"
        if item.is_dir() and (item.name in ignore_dirs or item.name.endswith('.egg-info')):
            continue
        if item.is_dir():
            structure[item.name] = scan_directory(item, ignore_dirs)
        else:
            structure[item.name] = "file"
    return structure

# Exemplo de uso direto (para testes):
if __name__ == "__main__":
    import json, sys
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    tree = scan_directory(p)
    print(json.dumps(tree, indent=2))
