# JAM-Tree

JAM-Tree é uma ferramenta open-source que gera uma árvore de diretórios de um projeto, facilitando a visualização da estrutura do código. Em futuras versões, o JAM-Tree integrará funcionalidades de análise via IA para descrever automaticamente as funcionalidades dos arquivos e oferecerá uma interface gráfica (GUI).

## Tabela de Conteúdos

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Opções do CLI](#opções-do-cli)
- [Documentação](#documentação)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [Licença](#licença)
- [Contato](#contato)

## Recursos

- **Geração de Árvore de Diretórios:**  
  Exibe a estrutura do projeto, listando primeiro os diretórios (em ordem alfabética) e depois os arquivos.

- **Exportação de Resultados:**  
  Permite exportar a árvore para os formatos:
  - **TXT**
  - **Markdown (MD)**
  - **JSON**

- **Ignoração de Diretórios Indesejados:**  
  Por padrão, o JAM-Tree ignora diretórios como `.git`, `venv`, `__pycache__` e diretórios que terminam com `.egg-info`. É possível adicionar diretórios adicionais via CLI.

- **Interface de Linha de Comando (CLI):**  
  Uso simples e intuitivo com o comando `jam-tree` e opções customizáveis.

- **(Futuro) Análise via IA:**  
  Integração de IA para analisar e descrever automaticamente os arquivos.

- **(Futuro) Interface Gráfica (GUI):**  
  Uma interface visual para facilitar a interação com a ferramenta.

## Instalação

### Requisitos

- **Python 3.10+**
- Bibliotecas: `click` e `rich`

### Instalação via pip (Modo Desenvolvimento)

Clone o repositório e instale o JAM-Tree em modo de desenvolvimento:

```bash
git clone https://github.com/GitHubJordan/jam-tree.git
cd jam-tree
pip install -e .
```

## Uso

Após a instalação, o comando principal para executar o JAM-Tree é:

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS]
```

### Opções do CLI

- **PATH** (argumento posicional)  
  Define o caminho do projeto a ser escaneado.  
  - *Exemplo:* `jam-tree .` (escaneia o diretório atual).  
  - Se não especificado, o diretório atual (`.`) é utilizado.

- **--export FORMAT**  
  Exporta a árvore gerada para um arquivo. Formatos disponíveis:
  - `txt` — Arquivo de texto.
  - `md` — Arquivo Markdown.
  - `json` — Arquivo JSON.  
  *Exemplo:*  
  ```bash
  jam-tree . --export md
  ```

- **--ignore DIRETÓRIOS**  
  Permite acrescentar diretórios adicionais a serem ignorados. Os diretórios informados são somados à lista padrão (que já inclui `.git`, `venv` e `__pycache__`).  
  *Exemplo:*  
  ```bash
  jam-tree . --ignore node_modules,dist
  ```

- **--help**  
  Exibe a mensagem de ajuda do CLI.

### Exemplos de Uso

- **Exibir a árvore do diretório atual:**

  ```bash
  jam-tree .
  ```

- **Exportar a árvore para Markdown:**

  ```bash
  jam-tree . --export md
  ```

- **Ignorar diretórios adicionais:**

  ```bash
  jam-tree . --ignore node_modules,dist
  ```

## Documentação

A documentação detalhada do CLI encontra-se no arquivo:  
`docs/CLI_DOCUMENTATION.md`

## Contribuindo

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção.
3. Realize os commits com mensagens claras e descritivas.
4. Envie um pull request com uma descrição detalhada das mudanças.
5. Verifique se os seus commits seguem as boas práticas do projeto e que os testes estão passando.

Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para mais informações.

## Roadmap

Os próximos passos planejados para o projeto incluem:

- **Integração de IA:**  
  Desenvolver o módulo de análise via IA para descrever automaticamente a funcionalidade dos arquivos.

- **Interface Gráfica (GUI):**  
  Criar uma GUI utilizando frameworks como Flet ou PyQt para melhorar a experiência do usuário.

- **Melhorias no CLI:**  
  Acrescentar novas opções para filtragem e ordenação da árvore, entre outras melhorias.

- **Testes Automatizados:**  
  Implementar uma suíte de testes para garantir a qualidade e estabilidade do código.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue no repositório ou entre em contato através do GitHub.

---

JAM-Tree é um projeto em constante evolução. Agradecemos sua contribuição e feedback para tornar essa ferramenta ainda melhor!