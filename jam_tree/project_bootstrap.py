import json
from pathlib import Path

def create_structure(base_path: Path, structure: dict):
    """
    Cria recursivamente pastas e arquivos conforme a estrutura definida.
    Se o valor for um dicionário, trata-se de um diretório.
    Se o valor for uma string (mesmo que vazia), trata-se de um arquivo.
    """
    for name, content in structure.items():
        path = base_path / name
        if isinstance(content, dict):
            path.mkdir(exist_ok=True)
            create_structure(path, content)
        else:
            # Cria o arquivo somente se ele não existir
            if not path.exists():
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

def bootstrap_project(json_file: str, create_root: bool = True) -> Path:
    """
    Cria a estrutura do projeto a partir do arquivo JSON fornecido.
    
    :param json_file: Caminho para o arquivo JSON que define a estrutura do projeto.
                        O JSON deve ter a seguinte estrutura:
                        {
                          "nome_projeto": "MeuProjeto",       // Nome do projeto (opcional)
                          "estrutura": {
                            "src": {
                              "main.py": "",
                              "utils": {}
                            },
                            "docs": {},
                            "tests": {},
                            "README.md": "# MeuProjeto\n\nDescrição do projeto..."
                          }
                        }
    :param create_root: Se True, cria uma pasta raiz com base no campo "nome_projeto".
                        Se False, utiliza o diretório atual como raiz.
    :return: O caminho da raiz onde a estrutura foi criada.
    """
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    project_name = data.get("nome_projeto", "")
    structure = data.get("estrutura", {})

    if create_root and project_name:
        root_path = Path(project_name)
        root_path.mkdir(exist_ok=True)
    else:
        root_path = Path(".")
    
    create_structure(root_path, structure)
    return root_path
