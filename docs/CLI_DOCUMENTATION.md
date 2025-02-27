# Documentação do CLI do JAM-Tree

## Visão Geral

O **JAM-Tree** é uma ferramenta de linha de comando que gera a árvore de diretórios de um projeto, com suporte para exportação em diferentes formatos, filtragem de diretórios indesejados e, agora, para a criação automática (bootstrapping) de novos projetos a partir de um arquivo JSON definido pelo usuário.

## Pré-requisitos

- **Python 3.10+**
- **Pacotes instalados:**
  - `click`
  - `rich`

Para instalar o JAM-Tree localmente (modo desenvolvimento), execute:

```bash
pip install -e .
```

## Comando Base

A sintaxe básica para executar o JAM-Tree é:

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS] [--create ARQUIVO_JSON] [--no-root]
```

### Parâmetros e Opções

- **PATH** (argumento posicional)  
  Define o caminho do projeto a ser escaneado.
  - **Exemplo:** `jam-tree .`  
    Escaneia o diretório atual.
  - Se não for especificado, o diretório atual (`.`) é usado por padrão.

- **--export FORMAT**  
  Exporta a árvore gerada para um arquivo no formato especificado. Os formatos disponíveis são:
  - `txt` — Arquivo de texto.
  - `md` — Arquivo Markdown.
  - `json` — Arquivo JSON.  
  **Exemplo:**  
  ```bash
  jam-tree . --export md
  ```  
  Exporta a árvore para um arquivo (por padrão, salvo como `project_tree.<ext>`).

- **--ignore DIRETÓRIOS**  
  Permite adicionar diretórios adicionais a serem ignorados na análise. Essa lista é somada à lista padrão (que já inclui: `.git`, `venv`, `__pycache__`, entre outros).
  - Os diretórios devem ser informados separados por vírgula.
  **Exemplo:**  
  ```bash
  jam-tree . --ignore node_modules,dist
  ```

- **--create ARQUIVO_JSON**  
  Cria a estrutura de um novo projeto a partir de um arquivo JSON que define a estrutura desejada.  
  - **Formato esperado do JSON:**
    ```json
    {
      "nome_projeto": "MeuProjeto",
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
    ```
  **Exemplo:**  
  ```bash
  jam-tree --create bootstrap.json
  ```
  Neste exemplo, se o campo `"nome_projeto"` estiver definido, uma nova pasta com esse nome será criada contendo a estrutura especificada.

- **--no-root**  
  Quando utilizado com `--create`, indica que a estrutura deverá ser criada diretamente no diretório atual, sem criar uma pasta raiz baseada no campo `"nome_projeto"` do arquivo JSON.
  **Exemplo:**  
  ```bash
  jam-tree --create bootstrap.json --no-root
  ```

- **--help**  
  Exibe a mensagem de ajuda com informações sobre o uso do comando e suas opções.

## Exemplos de Uso

### 1. Exibir a Árvore do Diretório Atual

```bash
jam-tree .
```

**Saída esperada:**

```
<nome_do_projeto>/                 # Pasta principal do projeto
│── <subdiretório ou arquivo>
│   ├── <arquivo>
│   └── <outro_arquivo>
│── <outro_arquivo>
```

### 2. Exportar a Árvore para um Arquivo Markdown

```bash
jam-tree . --export md
```

Será gerado um arquivo `project_tree.md` contendo a estrutura do projeto.

### 3. Ignorar Diretórios Adicionais

```bash
jam-tree . --ignore node_modules,dist
```

Neste exemplo, além dos diretórios padrão, serão ignorados `node_modules` e `dist`.

### 4. Criar um Projeto a partir de um Arquivo JSON (com Pasta Raiz)

```bash
jam-tree --create bootstrap.json
```

Se o arquivo `bootstrap.json` define `"nome_projeto": "MeuProjeto"`, o projeto será criado dentro de uma nova pasta chamada `MeuProjeto`.

### 5. Criar um Projeto a partir de um Arquivo JSON (Usando o Diretório Atual como Raiz)

```bash
jam-tree --create bootstrap.json --no-root
```

Neste caso, a estrutura será criada diretamente no diretório atual, sem criar uma pasta raiz separada.

## Notas Adicionais

- **Ordem de Exibição:**  
  A árvore é exibida com os diretórios listados primeiro (em ordem alfabética), seguidos pelos arquivos.

- **Ignorar Diretórios Indesejados:**  
  Além dos diretórios padrão (`.git`, `venv`, `__pycache__`, etc.), o JAM-Tree ignora diretórios que terminam com `.egg-info` para evitar listagens desnecessárias.

## Conclusão

Esta documentação cobre os principais aspectos do CLI do JAM-Tree, agora incluindo a funcionalidade de bootstrapping para criação automática de projetos. Futuras atualizações poderão adicionar novas funcionalidades, como a integração de IA e o desenvolvimento de uma interface gráfica (GUI).  
Para dúvidas, sugestões ou contribuições, sinta-se à vontade para abrir uma issue no repositório.

---
