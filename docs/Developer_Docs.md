# Developer Documentation – JAM-Tree

Esta documentação é voltada para contribuidores e desenvolvedores que desejam entender a arquitetura, executar testes e colaborar com o projeto JAM-Tree.

## 1. Visão Geral da Arquitetura

O JAM-Tree é organizado em módulos que se encarregam de funções específicas:

- **jam_tree/ai_analyzer.py:**  
  Integra a API Gemini para gerar resumos concisos e análises detalhadas de código.  
  - **Principais funções:** `analyze_file`, `analyze_node`, `analyze_file_detailed`.
  - **Cache:** Implementado para armazenar resultados e evitar chamadas repetitivas.

- **jam_tree/directory_scanner.py:**  
  Responsável por escanear recursivamente um diretório e gerar um dicionário representando a árvore de diretórios.

- **jam_tree/output_generator.py:**  
  Formata e gera a árvore em formato de texto, garantindo que pastas sejam exibidas antes dos arquivos (ordenação alfabética).  
  - Suporta exportação para TXT, Markdown e JSON.

- **jam_tree/project_bootstrap.py:**  
  Cria a estrutura de um novo projeto a partir de um template JSON.

- **jam_tree/cli.py:**  
  Ponto de entrada da ferramenta, que integra todas as funcionalidades por meio de comandos do Click, incluindo opções de análise com IA e feedback visual.

- **jam_tree/config.py:**  
  Gerencia as configurações do projeto, permitindo a personalização via arquivo `config.json`.

## 2. Configuração do Ambiente de Desenvolvimento

### Requisitos
- Python 3.10+
- Dependências listadas em `requirements.txt`

### Instalação
Clone o repositório e instale o pacote em modo de desenvolvimento:
```bash
git clone https://github.com/GitHubJordan/JAM-Tree.git
cd JAM-Tree
pip install -e .
```
Configure as variáveis de ambiente necessárias:
```bash
export AI_ANALYZER_API_KEY_GEMINI="sua_chave_aqui"
export AI_ANALYZER_MODEL="gemini-1.5-flash"
```
Opcionalmente, crie um arquivo `config.json` para personalizar configurações (veja a seção de Configuração).

## 3. Execução e Testes

### Uso Básico
- Para exibir a árvore do projeto:
  ```bash
  jam-tree .
  ```
- Para exibir a árvore com resumos AI:
  ```bash
  jam-tree --ai-comments
  ```
- Para analisar detalhadamente um arquivo:
  ```bash
  jam-tree analyze caminho/do/arquivo.py --export txt
  ```

### Executando Testes
Os testes unitários estão na pasta `tests/`. Para executá-los, use:
```bash
pytest
```
Certifique-se de que todas as dependências estejam instaladas e que as variáveis de ambiente estejam configuradas.

## 4. Contribuindo

### Diretrizes de Contribuição
- Siga o padrão de código definido no projeto.
- Escreva commits com mensagens claras e descritivas.
- Adicione testes para novas funcionalidades ou correções.
- Verifique se a documentação está atualizada.

Consulte [CONTRIBUTING.md](../CONTRIBUTING.md) para mais detalhes.

## 5. Roadmap

### Funcionalidades Futuras (Versão 0.2.0)
- **Empacotamento e Transporte de Projetos:**  
  Exportar o projeto inteiro para um arquivo compacto (.jtree ou .tree) e permitir a importação.
- **StarBuild – JAM-Tree:**  
  Criação assistida de projetos via IA, gerando templates a partir de prompts.
- **Novos Formatos de Exportação:**  
  Suporte para HTML e XML.
- **Interface Gráfica (GUI):**  
  Desenvolver uma interface visual interativa.
- **Configuração via Arquivo:**  
  Permitir a personalização completa das opções via arquivo (ex.: config.json).
- **Testes Automatizados e CI/CD:**  
  Ampliar a suíte de testes e configurar pipelines de integração contínua.

## 6. Outras Informações

- **Documentação e Suporte:**  
  Consulte a documentação completa em [Read the Docs](https://jam-tree.readthedocs.io/)
- **Comunidade:**  
  Para dúvidas, sugestões ou reportar bugs, abra uma [issue](https://github.com/GitHubJordan/JAM-Tree/issues) no repositório.

---
