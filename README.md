<div classe="img_logo" style="background-color:#09152A">
<img src="https://jam-tree.readthedocs.io/pt-br/latest/img/jam-tree_logo_sem_fundo.png" width="400" style="display: block; margin-left: auto; margin-right: auto;" />
</div>

# JAM-Tree
![CI](https://github.com/GitHubJordan/JAM-Tree/actions/workflows/ci.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/jam-tree/badge/?version=latest&style=flat)](ttps://jam-tree.readthedocs.io/pt-br/latest/badge=latest)

**JAM-Tree** é uma ferramenta open-source que gera a árvore completa de diretórios de um projeto – da raiz até as subpastas e arquivos – e a exibe de forma organizada. Além disso, ela permite exportar a estrutura para diversos formatos, criar projetos a partir de um template JSON (bootstrapping) e realizar análises de código com IA para gerar resumos concisos.

A ferramenta foi projetada para atender tanto desenvolvedores finais que precisam documentar e entender a estrutura dos seus projetos, quanto para contribuidores que desejam aprimorar e expandir suas funcionalidades.

---

## Tabela de Conteúdos

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Comandos e Opções](#comandos-e-opções)
  - [Exemplos de Uso](#exemplos-de-uso)
- [Configuração](#configuração)
- [Documentação Completa](#documentação-completa)
- [Contribuindo](#contribuindo)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Licença](#licença)
- [Contato](#contato)

---

## Recursos

- **Árvore Completa de Diretórios:**  
  Escaneia recursivamente o diretório do projeto e exibe sua estrutura completa (pastas, subpastas e arquivos) com ordenação: pastas primeiro e, depois, arquivos – ambos em ordem alfabética.

- **Exportação:**  
  Permite exportar a árvore para os formatos TXT, Markdown (MD) e JSON.

- **Projeto Bootstrapping:**  
  Cria a estrutura de um novo projeto a partir de um template JSON, com a opção de usar o diretório atual ou criar uma nova pasta raiz.

- **Análise com IA:**  
  Utiliza a API Gemini para gerar resumos concisos (até 64 caracteres) para cada nó da árvore (arquivos e diretórios).  
  - **Modo Resumido:** (via opção `--ai-comments`) exibe os resumos junto à árvore.  
  - **Modo Detalhado:** (subcomando `analyze`) gera uma análise completa de um arquivo.

- **Feedback Visual:**  
  Mensagens de status interativas e barra de progresso (opção `--progress`) para informar o usuário durante o escaneamento e análise.

---

## Instalação

### Requisitos

- **Python 3.10+**
- Dependências listadas em `requirements.txt` (inclui `click`, `rich`, `google-generativeai`, etc.)

### Instalação via pip (Modo Desenvolvimento)

```bash
git clone https://github.com/GitHubJordan/JAM-Tree.git
cd JAM-Tree
pip install -e .
```

> **Nota:**  
> Configure a variável de ambiente para a API Gemini:
> ```bash
> export AI_ANALYZER_API_KEY_GEMINI="sua_chave_aqui"
> ```
> Opcionalmente, defina o modelo de IA com:
> ```bash
> export AI_ANALYZER_MODEL="gemini-1.5-flash"
> ```

---

## Uso

A sintaxe básica do JAM-Tree é:

```bash
jam-tree [PATH] [--export FORMAT] [--ignore DIRETÓRIOS] [--create ARQUIVO_JSON] [--no-root] [--ai-comments] [--progress]
```

### Comandos e Opções

- **PATH:**  
  Diretório a ser escaneado. Se omitido, o diretório atual é utilizado.

- **--export FORMAT:**  
  Exporta a árvore para um dos formatos: `txt`, `md` ou `json`.

- **--ignore DIRETÓRIOS:**  
  Lista de diretórios adicionais a ignorar, separados por vírgula.

- **--create ARQUIVO_JSON:**  
  Cria a estrutura do projeto a partir de um template JSON.

- **--no-root:**  
  Quando usado com `--create`, utiliza o diretório atual como raiz, sem criar uma nova pasta.

- **--ai-comments:**  
  Anexa resumos gerados por IA (até 64 caracteres) a cada nó da árvore.

- **--progress:**  
  Exibe uma barra de progresso durante a análise dos nós (deve ser usada junto com `--ai-comments`).

- **Subcomando `analyze`:**  
  ```bash
  jam-tree analyze caminho/do/arquivo.py [--export FORMAT]
  ```
  Gera uma análise detalhada do arquivo e, se a opção `--export` for utilizada, exporta o relatório (por padrão, para `resume_file.txt`).

---

## Exemplos de Uso

### Exibir a Árvore do Projeto

```bash
jam-tree .
```

### Exibir a Árvore com Resumos AI

```bash
jam-tree --ai-comments
```

### Exibir a Árvore com Resumos e Barra de Progresso

```bash
jam-tree --ai-comments --progress
```

### Exportar a Árvore para Markdown

```bash
jam-tree --ai-comments --export md
```

### Criar um Projeto a Partir de um Template

```bash
jam-tree --create template.json
```

### Analisar Detalhadamente um Arquivo e Exportar a Análise

```bash
jam-tree analyze jam_tree/cli.py --export md
```

---

## Configuração

Você pode personalizar opções importantes por meio de um arquivo de configuração (`config.json`). Por exemplo:

**config.json**

```json
{
  "ignore_dirs": [".git", "venv", "__pycache__"],
  "ai_model": "gemini-1.5-flash",
  "export_format": "txt"
}
```

E o módulo `config.py` permite acessar essas configurações:

**jam_tree/config.py**

```python
import json
import os

CONFIG_FILE = "config.json"
_config = {}

def load_config():
    global _config
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                _config = json.load(f)
        except Exception:
            _config = {}

def get_config_option(key: str, default=None):
    return _config.get(key, default)

load_config()
```

Você pode integrar essas configurações no CLI e nos módulos de análise conforme necessário.

---

## Documentação Completa

Para uma documentação mais detalhada, consulte:

- **CLI_DOCUMENTATION.md** – Instruções detalhadas, exemplos de uso e explicação de cada comando.
- **Tutorial.md** – Um tutorial passo a passo que ensina como usar o JAM-Tree para:
  - Gerar a árvore do projeto.
  - Exportar a árvore.
  - Criar novos projetos via template JSON.
  - Analisar código com IA.
- **Developer_Docs.md** – Documentação voltada para contribuidores, com detalhes de arquitetura, instruções para rodar testes, diretrizes de contribuição, etc.

---

## Contribuindo

Contribuições são muito bem-vindas! Para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção.
3. Realize commits com mensagens claras e detalhadas.
4. Envie um pull request com uma descrição completa das mudanças.
5. Consulte [CONTRIBUTING.md](docs/CONTRIBUTING.md) para mais orientações.

---

## Roadmap

### Versão 0.1.x (Funcionalidades Atuais)
- Escaneamento e geração da árvore de diretórios.
- Exportação da árvore em TXT, MD e JSON.
- Projeto Bootstrapping a partir de um template JSON.
- Análise de código com IA (resumos concisos e análise detalhada).
- Feedback visual no CLI (status, barra de progresso).
- Cache persistente para análises com IA.

### Versão 0.2.0 (Funcionalidades Futuras)
- **Empacotamento e Transporte de Projetos:** Exportar o projeto inteiro para um arquivo compacto (.jtree ou .tree) e importar posteriormente.
- **StarBuild – JAM-Tree:** Criação assistida de projetos via IA, com templates dinâmicos gerados a partir de prompts.
- **Novos Formatos de Exportação:** Suporte a exportação para HTML e XML.
- **Configuração via Arquivo:** Permitir definir opções por meio de um arquivo de configuração.
- **Interface Gráfica (GUI):** Desenvolver uma GUI para facilitar a interação.
- **Testes Automatizados e CI/CD:** Ampliar a suíte de testes e configurar pipelines de integração contínua.

---

## FAQ

**Q: Preciso configurar algo antes de usar o JAM-Tree?**  
A: Sim. Configure a variável de ambiente `AI_ANALYZER_API_KEY_GEMINI` com sua chave de API. Opcionalmente, defina também `AI_ANALYZER_MODEL`.

**Q: Como posso exportar a análise detalhada de um arquivo?**  
A: Use o subcomando `analyze` com a opção `--export` para salvar a análise em um arquivo. Por exemplo:
```bash
jam-tree analyze caminho/do/arquivo.py --export md
```

**Q: O que fazer se a análise com IA falhar?**  
A: Se ocorrer um erro (por exemplo, "429 Resource has been exhausted"), o resumo será exibido como "N/A". O sistema não armazenará erros temporários, permitindo novas tentativas em execuções futuras.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue no repositório ou entre em contato via GitHub.

---

## Conclusão

O JAM-Tree é uma ferramenta robusta que já oferece funcionalidades essenciais para escanear, exportar, criar e analisar a estrutura de projetos, com integração de IA e feedback visual interativo. Com essa documentação atualizada, tanto os usuários finais quanto os contribuidores terão acesso a informações detalhadas e tutoriais que facilitam o uso e a manutenção do projeto.

Estamos comprometidos em seguir nosso ciclo de desenvolvimento em cascata e lançar novas funcionalidades na versão 0.2.0, como o empacotamento completo do projeto e o StarBuild – JAM-Tree.

---