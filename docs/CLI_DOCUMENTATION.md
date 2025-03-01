# Documentação do CLI do JAM-Tree

## Visão Geral

O **JAM-Tree** é uma ferramenta de linha de comando que permite:
- Gerar uma árvore completa de diretórios, exibindo a estrutura do projeto (da raiz até os arquivos).
- Exportar a árvore para vários formatos (TXT, MD, JSON).
- Criar a estrutura de um novo projeto a partir de um template JSON.
- Analisar código com IA, gerando resumos concisos (até 64 caracteres) para cada nó (arquivos e diretórios).
- Exibir feedback visual interativo, como mensagens de status e barras de progresso.

## Pré-Requisitos

- **Python 3.10+**
- Instale as dependências:
  ```bash
  pip install -e .
  ```
- Configure a variável de ambiente para a API Gemini:
  ```bash
  export AI_ANALYZER_API_KEY_GEMINI="sua_chave_aqui"
  ```
- (Opcional) Defina o modelo de IA a ser utilizado:
  ```bash
  export AI_ANALYZER_MODEL="gemini-1.5-flash"
  ```

## Sintaxe Básica

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS] [--create ARQUIVO_JSON] [--no-root] [--ai-comments] [--progress]
```

### Descrição das Opções

- **PATH:**  
  Diretório a ser escaneado. Se omitido, usa o diretório atual.

- **--export FORMAT:**  
  Exporta a árvore para um dos formatos: `txt`, `md` ou `json`.

- **--ignore DIRETÓRIOS:**  
  Lista adicional de diretórios a ignorar, separados por vírgula.

- **--create ARQUIVO_JSON:**  
  Cria a estrutura do projeto a partir de um template JSON.

- **--no-root:**  
  Quando usado com `--create`, utiliza o diretório atual como raiz (sem criar uma nova pasta).

- **--ai-comments:**  
  Anexa resumos gerados por IA a cada nó da árvore. Os resumos são concisos (até 64 caracteres).

- **--progress:**  
  Exibe uma barra de progresso durante a análise dos nós (usado junto com `--ai-comments`).

- **Subcomando `analyze`:**  
  ```bash
  jam-tree . analyze caminho/do/arquivo.py
  ```
  Realiza uma análise detalhada do arquivo, retornando uma explicação completa.

## Exemplos de Uso

### 1. Exibir a Árvore do Projeto

```bash
jam-tree .
```

Exibe a árvore completa do projeto (da raiz até os arquivos), ordenada com pastas primeiro e depois arquivos (ambos em ordem alfabética).

### 2. Exibir a Árvore com Resumos AI

```bash
jam-tree --ai-comments
```

Exibe a árvore com resumos gerados pela IA para cada nó.

### 3. Exibir a Árvore com Barra de Progresso

```bash
jam-tree --ai-comments --progress
```

Exibe a árvore com os resumos e uma barra de progresso durante a análise.

### 4. Criar um Projeto a Partir de um Template JSON

```bash
jam-tree --create template.json
```

Cria a estrutura do projeto conforme o template JSON fornecido.

### 5. Analisar Detalhadamente um Arquivo

```bash
jam-tree . analyze caminho/do/arquivo.py
```

Fornece uma análise detalhada do arquivo especificado.

## Notas Adicionais

- **Cache de Análise:**  
  O JAM-Tree utiliza um sistema de cache para evitar análises repetidas, armazenando os resultados em um arquivo persistente `.jam_tree_cache.json`. Resultados de erro (como limites de quota) não são armazenados, permitindo novas tentativas.

- **Feedback Visual:**  
  Mensagens de status e barras de progresso são exibidas durante o escaneamento e análise, melhorando a experiência do usuário.

## Conclusão

Esta documentação cobre as funcionalidades atuais do CLI do JAM-Tree. À medida que o projeto evoluir, novas funcionalidades e melhorias serão adicionadas, e esta documentação será atualizada para refletir essas mudanças.

Para dúvidas, sugestões ou contribuições, abra uma issue no repositório.

---

# Visão Geral do Desenvolvimento do JAM-Tree

### Implementações Concluídas

- **Estrutura e Organização:**  
  Projeto estruturado com pastas para código (jam_tree), documentação (docs), testes (tests) e arquivos de configuração (README.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md).

- **Escaneamento e Geração da Árvore:**  
  O módulo `directory_scanner.py` gera recursivamente a árvore de diretórios, e `output_generator.py` formata a árvore, exibindo pastas antes dos arquivos, em ordem alfabética.

- **Projeto Bootstrapping:**  
  O módulo `project_bootstrap.py` cria a estrutura do projeto a partir de um template JSON.

- **Análise com IA:**  
  O módulo `ai_analyzer.py` integra a API Gemini para gerar resumos concisos (até 64 caracteres) para arquivos e diretórios. Implementamos também cache persistente e tratamento de erros.

- **Integração no CLI:**  
  O CLI (`cli.py`) integra todas as funcionalidades:
  - Fluxo padrão para exibir a árvore completa.
  - Opção `--ai-comments` para anotar a árvore com resumos AI.
  - Opção `--progress` para exibir uma barra de progresso durante a análise.
  - Subcomando `analyze` para uma análise detalhada de arquivos.

- **Feedback Visual:**  
  Mensagens de status e barra de progresso com a biblioteca Rich foram integradas para uma melhor experiência no terminal.

### Próximos Passos

1. **Aprimoramento do AI Analyzer:**  
   - Continuar refinando os prompts para reduzir erros e melhorar os resumos.
   - Implementar cache persistente aprimorado e, possivelmente, retentativas automáticas em caso de erro temporário.

2. **Interface de Configuração:**  
   - Permitir que o usuário configure opções como diretórios a ignorar e modelo de IA via um arquivo de configuração.

3. **Novos Formatos de Exportação:**  
   - Explorar a exportação da árvore em HTML e XML.

4. **Interface Gráfica (GUI):**  
   - Planejar e desenvolver uma interface gráfica para tornar a ferramenta ainda mais interativa.

5. **Testes Automatizados e CI/CD:**  
   - Ampliar a suíte de testes unitários e de integração.
   - Configurar um pipeline CI/CD (por exemplo, com GitHub Actions) para validar o projeto a cada commit.

---
