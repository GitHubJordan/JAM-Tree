# FAQ – Perguntas Frequentes

## 1. O que é o JAM-Tree?
**JAM-Tree** é uma ferramenta de linha de comando que gera a árvore completa de diretórios de um projeto, permite exportá-la em diversos formatos, cria estruturas de projetos a partir de templates JSON e integra a análise de código com IA para fornecer resumos concisos.

## 2. Quais são os principais formatos de exportação suportados?
Atualmente, o JAM-Tree suporta a exportação da árvore de diretórios para os seguintes formatos:
- TXT
- Markdown (MD)
- JSON

## 3. Como posso criar a estrutura de um novo projeto?
Você pode utilizar a opção `--create` seguida do caminho para um arquivo JSON que define a estrutura do projeto. Por exemplo:
```bash
jam-tree --create template.json
```
Se desejar utilizar o diretório atual como raiz, adicione a opção `--no-root`.

## 4. O que são os resumos gerados pela análise com IA?
A análise com IA gera resumos concisos (até 64 caracteres) que descrevem a funcionalidade principal de cada arquivo ou diretório. Esses resumos são exibidos ao lado dos nomes na árvore quando você utiliza a opção `--ai-comments`.

## 5. Como funciona a análise detalhada de um arquivo?
Para uma análise detalhada, use o subcomando `analyze` seguido do caminho do arquivo. Por exemplo:
```bash
jam-tree analyze caminho/do/arquivo.py
```
Você também pode exportar o relatório de análise para um arquivo, usando a opção `--export`.

## 6. E se a análise com IA falhar?
Se ocorrer um erro (por exemplo, devido a limites de quota ou problemas de rede), a ferramenta exibirá "N/A" como resumo para aquele nó. O sistema de cache não armazenará erros temporários, permitindo que a análise seja reexecutada em futuras execuções.

## 7. Como posso personalizar as configurações do JAM-Tree?
Você pode personalizar configurações importantes (como diretórios a ignorar ou o modelo de IA) utilizando um arquivo de configuração chamado `config.json`. Consulte a seção de Configuração da documentação para mais detalhes.

## 8. Onde posso obter suporte ou contribuir para o projeto?
Para suporte, sugestões ou reportar bugs, abra uma issue no [repositório do JAM-Tree](https://github.com/GitHubJordan/JAM-Tree/issues). Se desejar contribuir, consulte as diretrizes em [CONTRIBUTING.md](../CONTRIBUTING.md).

---

*Se sua dúvida não foi respondida aqui, sinta-se à vontade para abrir uma issue ou entrar em contato via GitHub.*

---
