# JAM-Tree

**JAM-Tree** é uma ferramenta open-source que gera a árvore completa de diretórios de um projeto – da raiz até as subpastas e arquivos – e a exibe de forma organizada. Além disso, a ferramenta permite:

- **Exportação:**  
  Exporta a árvore para formatos TXT, Markdown (MD) ou JSON.

- **Criação de Projetos (Bootstrapping):**  
  Cria a estrutura de um novo projeto a partir de um template JSON, com opção de usar o diretório atual como raiz.

- **Análise com IA:**  
  Utiliza a API Gemini para gerar resumos concisos (até 64 caracteres) para cada arquivo e diretório. Esses resumos são integrados à árvore, oferecendo uma visão rápida da funcionalidade de cada nó.
  - O modo **AI Comments** (ativado com `--ai-comments`) anexa automaticamente os resumos a cada nó da árvore.
  - O subcomando `analyze` realiza uma análise detalhada de um arquivo.

- **Feedback Visual e Barra de Progresso:**  
  Durante a análise (quando ativada a opção `--progress`), são exibidas mensagens de status e uma barra de progresso para melhorar a experiência do usuário.

## Tabela de Conteúdos

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Comandos e Opções do CLI](#comandos-e-opções-do-cli)
- [Documentação Completa](#documentação-completa)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [Licença](#licença)
- [Contato](#contato)

## Recursos

- **Árvore Completa de Diretórios:**  
  Escaneia recursivamente o diretório do projeto e exibe a estrutura completa, com as pastas listadas antes dos arquivos (em ordem alfabética).

- **Exportação da Árvore:**  
  Permite exportar a árvore para os formatos TXT, MD ou JSON.

- **Criação de Projetos (Bootstrapping):**  
  Cria a estrutura de um novo projeto a partir de um template JSON.

- **Análise com IA:**  
  Gera resumos concisos (até 64 caracteres) para cada nó da árvore utilizando a API Gemini.  
  - **Modo Resumido:** Exibe os resumos na árvore (opção `--ai-comments`).
  - **Modo Detalhado:** Utiliza o subcomando `analyze` para obter uma explicação completa de um arquivo.

- **Feedback Visual:**  
  Mensagens de status e uma barra de progresso (opção `--progress`) fornecem feedback interativo durante o escaneamento e análise.

## Instalação

### Requisitos

- **Python 3.10+**
- Dependências listadas em `requirements.txt` (inclui `click`, `rich`, `google-generativeai`, etc.)

### Instalação via pip (Modo Desenvolvimento)

```bash
git clone https://github.com/GitHubJordan/jam-tree.git
cd jam-tree
pip install -e .
```

> **Nota:** Configure a variável de ambiente para a API Gemini:
> ```bash
> export AI_ANALYZER_API_KEY_GEMINI="sua_chave_aqui"
> ```
> Opcionalmente, você pode definir o modelo de IA a ser utilizado com:
> ```bash
> export AI_ANALYZER_MODEL="gemini-1.5-flash"
> ```

## Uso

A sintaxe básica do JAM-Tree é:

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS] [--create ARQUIVO_JSON] [--no-root] [--ai-comments] [--progress]
```

### Comandos e Opções do CLI

- **Fluxo Padrão (Escaneamento):**  
  ```bash
  jam-tree .
  ```
  Exibe a árvore completa do projeto, da raiz até as subpastas e arquivos.

- **Opção `--export FORMAT`:**  
  Exporta a árvore para `txt`, `md` ou `json`.

- **Opção `--ignore DIRETÓRIOS`:**  
  Permite ignorar diretórios adicionais (além dos padrões).

- **Opção `--create ARQUIVO_JSON`:**  
  Cria a estrutura do projeto a partir de um template JSON.  
  Exemplo de template:
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

- **Opção `--no-root`:**  
  Quando usada com `--create`, utiliza o diretório atual como raiz, sem criar uma nova pasta.

- **Opção `--ai-comments`:**  
  Adiciona resumos gerados por IA a cada nó (arquivos e diretórios) da árvore, conforme a estrutura definida.

- **Opção `--progress`:**  
  Exibe uma barra de progresso durante a análise dos nós (usada em conjunto com `--ai-comments`).

- **Subcomando `analyze`:**  
  ```bash
  jam-tree . analyze caminho/do/arquivo.py
  ```
  Realiza uma análise detalhada do arquivo, retornando uma explicação completa.

## Documentação Completa

Consulte a [CLI_DOCUMENTATION.md](docs/CLI_DOCUMENTATION.md) para detalhes completos sobre os comandos, opções e exemplos de uso.

## Contribuindo

Contribuições são bem-vindas! Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para informações sobre como colaborar.

## Roadmap

Próximos passos planejados:
- **Aprimoramento do AI Analyzer:**  
  Refinar os prompts, melhorar o tratamento de erros (e evitar cache de erros) e implementar um cache persistente.
- **Desenvolvimento de Interface Gráfica (GUI):**  
  Criar uma GUI para facilitar a visualização e análise de projetos.
- **Testes Automatizados e CI/CD:**  
  Ampliar a suíte de testes e configurar pipelines de integração contínua.
- **Exportação para Novos Formatos:**  
  Explorar a exportação para HTML e XML.
- **Integração de Configuração via Arquivo:**  
  Permitir definir opções (como diretórios a ignorar e modelo de IA) através de um arquivo de configuração.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue no repositório ou entre em contato via GitHub.

---

JAM-Tree é um projeto em constante evolução. Agradecemos seu feedback e contribuições para tornar essa ferramenta cada vez melhor!

---
