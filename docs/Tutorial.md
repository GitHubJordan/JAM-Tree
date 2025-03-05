# Tutorial JAM-Tree

Este tutorial passo a passo irá guiá-lo por todas as funcionalidades principais do JAM-Tree.

## 1. Gerando a Árvore do Projeto

### Passo 1: Abrir o Terminal
Certifique-se de estar no diretório do seu projeto ou no diretório onde o JAM-Tree está instalado.

### Passo 2: Executar o Comando Básico
Para exibir a árvore completa do projeto:
```bash
jam-tree .
```
Você verá uma saída semelhante a:
```
JAM-Tree/                 # Pasta principal do projeto
├── docs/
│   └── CLI_DOCUMENTATION.md
├── jam_tree/
│   ├── __init__.py
│   ├── ai_analyzer.py
│   ├── cli.py
│   ├── directory_scanner.py
│   ├── output_generator.py
│   └── project_bootstrap.py
├── tests/
│   ├── bootstrap.json
│   ├── test_directory_scanner.py
│   ├── test_output_generator.py
│   └── test_project_bootstrap.py
├── .env
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 2. Exportando a Árvore

Você pode exportar a árvore para diferentes formatos. Por exemplo:
```bash
jam-tree --export md
```
Isso gerará um arquivo `project_tree.md` com a estrutura do seu projeto.

## 3. Criando um Projeto a Partir de um Template

Crie um arquivo JSON (ex.: `template.json`) com a estrutura desejada:
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
Para criar a estrutura:
```bash
jam-tree --create template.json
```
Para criar a estrutura no diretório atual, sem criar uma nova pasta:
```bash
jam-tree --create template.json --no-root
```

## 4. Análise de Código com IA

### Resumo Conciso na Árvore
Para adicionar resumos gerados por IA a cada nó:
```bash
jam-tree --ai-comments
```

### Análise Detalhada de um Arquivo
Para analisar um arquivo e obter uma explicação completa:
```bash
jam-tree analyze caminho/do/arquivo.py
```
Você também pode exportar a análise:
```bash
jam-tree analyze caminho/do/arquivo.py --export txt
```
Isso salvará a análise em `resume_file.txt` (ou em outro formato, se especificado).

## 5. Feedback Visual e Barra de Progresso

Para ver uma barra de progresso durante a análise com IA:
```bash
jam-tree --ai-comments --progress
```
Isso exibirá uma barra de progresso enquanto os nós são analisados.

---

## Conclusão do Tutorial

O JAM-Tree oferece uma maneira prática e interativa de visualizar, exportar e analisar a estrutura de projetos, além de criar novos projetos a partir de templates. Experimente as diferentes opções e descubra como essa ferramenta pode facilitar seu fluxo de trabalho!

---
