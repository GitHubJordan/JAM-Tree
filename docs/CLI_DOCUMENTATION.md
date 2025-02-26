# Documentação do CLI do JAM-Tree

## Visão Geral

O **JAM-Tree** é uma ferramenta de linha de comando que gera a árvore de diretórios de um projeto, com suporte para exportação em diferentes formatos e filtragem de diretórios indesejados. Este documento apresenta os comandos e opções disponíveis na versão CLI do JAM-Tree.

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
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS]
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
  Exporta a árvore para um arquivo Markdown (por padrão, salvo como `project_tree.md`).

- **--ignore DIRETÓRIOS**  
  Permite adicionar diretórios adicionais a serem ignorados na análise. Essa lista é adicionada à lista padrão de diretórios indesejados (que já inclui: `.git`, `venv` e `__pycache__`).  
  - Os diretórios devem ser informados separados por vírgula.  
  **Exemplo:**  
  ```bash
  jam-tree . --ignore node_modules,dist
  ```  
  Neste caso, além dos diretórios padrão, serão ignorados os diretórios `node_modules` e `dist`.

- **--help**  
  Exibe uma mensagem de ajuda com informações sobre o uso do comando e suas opções.

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

### 2. Exibir a Árvore de um Projeto Específico

```bash
jam-tree /caminho/para/o/projeto
```

### 3. Exportar a Árvore para um Arquivo Markdown

```bash
jam-tree . --export md
```

Será gerado um arquivo `project_tree.md` contendo a estrutura do projeto.

### 4. Ignorar Diretórios Adicionais

```bash
jam-tree . --ignore node_modules,dist
```

Neste exemplo, os diretórios `node_modules` e `dist` serão ignorados, além dos diretórios padrão.

### 5. Combinar Exportação e Filtragem de Diretórios

```bash
jam-tree /caminho/para/o/projeto --export json --ignore node_modules,dist
```

A árvore do projeto será exportada em formato JSON e os diretórios `node_modules` e `dist` serão ignorados.

## Notas Adicionais

- **Ordem de Exibição:**  
  A árvore é exibida com os diretórios listados primeiro (em ordem alfabética), seguidos pelos arquivos.

- **Ignorar Diretórios Indesejados:**  
  Por padrão, além de `.git`, `venv` e `__pycache__`, diretórios que terminam com `.egg-info` também são ignorados para evitar listagens indesejadas.

## Conclusão

Esta documentação cobre os principais aspectos do CLI do JAM-Tree. Futuras atualizações poderão adicionar novas funcionalidades ou opções, e este documento será revisado conforme necessário.

Para dúvidas, sugestões ou contribuições, sinta-se à vontade para abrir uma issue no repositório do projeto.

---