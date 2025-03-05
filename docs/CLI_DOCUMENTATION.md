# Documentação do CLI do JAM-Tree

## Visão Geral

O **JAM-Tree** é uma ferramenta de linha de comando que permite:
- Gerar a árvore completa de diretórios de um projeto (da raiz até os arquivos).
- Exportar a árvore para formatos TXT, Markdown (MD) e JSON.
- Criar a estrutura de um novo projeto a partir de um template JSON.
- Analisar código com IA para gerar resumos concisos (até 64 caracteres) para cada nó (arquivos e diretórios).
- Exibir feedback visual interativo, como mensagens de status e barras de progresso.

## Sintaxe Básica

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS] [--create ARQUIVO_JSON] [--no-root] [--ai-comments] [--progress]
```

## Comandos e Opções

### Fluxo Padrão
- **Descrição:**  
  Escaneia o diretório especificado (ou o diretório atual, se não informado) e exibe a árvore completa.
- **Exemplo:**
  ```bash
  jam-tree .
  ```

### Opção `--export FORMAT`
- **Descrição:**  
  Exporta a árvore para um arquivo no formato especificado.  
  - **Formatos disponíveis:** `txt`, `md`, `json`.
- **Exemplo:**
  ```bash
  jam-tree --export md
  ```

### Opção `--ignore DIRETÓRIOS`
- **Descrição:**  
  Especifica uma lista de diretórios adicionais a serem ignorados, separados por vírgula.
- **Exemplo:**
  ```bash
  jam-tree --ignore node_modules,dist
  ```

### Opção `--create ARQUIVO_JSON`
- **Descrição:**  
  Cria a estrutura do projeto com base no template JSON fornecido.
- **Exemplo:**
  ```bash
  jam-tree --create template.json
  ```

### Opção `--no-root`
- **Descrição:**  
  Quando usada com `--create`, utiliza o diretório atual como raiz, sem criar uma nova pasta.
- **Exemplo:**
  ```bash
  jam-tree --create template.json --no-root
  ```

### Opção `--ai-comments`
- **Descrição:**  
  Anexa resumos gerados por IA a cada nó (pastas e arquivos) da árvore.
- **Exemplo:**
  ```bash
  jam-tree --ai-comments
  ```

### Opção `--progress`
- **Descrição:**  
  Exibe uma barra de progresso durante a análise com IA (utilizada juntamente com `--ai-comments`).
- **Exemplo:**
  ```bash
  jam-tree --ai-comments --progress
  ```

### Subcomando `analyze`
- **Descrição:**  
  Realiza uma análise detalhada de um arquivo, retornando uma explicação completa.  
  Se a opção `--export` for utilizada, salva o relatório em um arquivo.
- **Exemplo:**
  ```bash
  jam-tree analyze jam_tree/cli.py --export md
  ```

## Considerações

- **Feedback Visual:**  
  O JAM-Tree utiliza a biblioteca **Rich** para exibir mensagens de status e barras de progresso.
- **Cache e Tratamento de Erros:**  
  A ferramenta implementa um mecanismo de cache persistente e tratamento de exceções para minimizar chamadas repetitivas e informar o usuário sobre erros (ex.: limites de quota).

---
