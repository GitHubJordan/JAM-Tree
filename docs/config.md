# Configuração do JAM-Tree

Este documento descreve como configurar o JAM-Tree por meio de um arquivo de configuração (`config.json`). Essa abordagem permite que você personalize diversas opções da ferramenta sem precisar modificar o código-fonte, tornando o uso do JAM-Tree mais flexível e adaptável ao seu fluxo de trabalho.

## Estrutura do Arquivo de Configuração

O arquivo de configuração deve ser nomeado `config.json` e estar localizado na raiz do projeto. Um exemplo de estrutura é:

```json
{
  "ignore_dirs": [".git", "venv", "__pycache__"],
  "ai_model": "gemini-1.5-flash",
  "export_format": "txt"
}
```

## Opções Disponíveis

### `ignore_dirs`
- **Descrição:**  
  Lista de diretórios que serão ignorados durante o escaneamento da estrutura do projeto.
- **Exemplo:**
  ```json
  "ignore_dirs": [".git", "venv", "__pycache__"]
  ```

### `ai_model`
- **Descrição:**  
  Define o modelo de IA a ser utilizado para gerar resumos e análises de código.
- **Valor Padrão:** `"gemini-1.5-flash"`
- **Exemplo:**
  ```json
  "ai_model": "gemini-1.5-flash"
  ```

### `export_format`
- **Descrição:**  
  Define o formato padrão para exportação da árvore de diretórios.
- **Opções:** `"txt"`, `"md"`, `"json"`
- **Exemplo:**
  ```json
  "export_format": "txt"
  ```

## Como o JAM-Tree Utiliza o Arquivo de Configuração

O módulo `config.py` do JAM-Tree é responsável por carregar automaticamente as configurações definidas no `config.json` ao iniciar o projeto. Você pode acessar essas opções usando a função `get_config_option(key, default)`, permitindo que as configurações sejam integradas facilmente aos demais módulos (como no AI Analyzer e no CLI).

## Personalizando sua Configuração

Você pode editar o `config.json` conforme suas necessidades. Por exemplo, se desejar ignorar diretórios adicionais, basta incluir os nomes na lista:

```json
```json
{
  "ignore_dirs": [".git", "venv", "__pycache__"],
  "ai_model": {
    "default": "gemini-1.5-flash",
    "models": [
      {
        "nome": "gemini-1.5-pro",
        "configuracoes": {
          "temperature": 0.7,
          "max_output_tokens": 1024,
          "top_k": 40,
          "top_p": 0.95
        },
        "disponibilidade": "Google One AI Premium",
        "descricao": "Tarefas de raciocínio complexas."
      },
      {
        "nome": "gemini-1.5-flash",
        "configuracoes": {
          "temperature": 0.5,
          "max_output_tokens": 512,
          "top_k": 20,
          "top_p": 0.8
        },
        "disponibilidade": "Gratuito",
        "descricao": "Respostas rápidas e versáteis."
      },
      {
        "nome": "gemini-2.0-flash",
        "configuracoes": {
          "temperature": 0.6,
          "max_output_tokens": 768,
          "top_k": 30,
          "top_p": 0.9
        },
        "disponibilidade": "Gratuito",
        "descricao": "Geração multimodal e recursos avançados."
      },
      {
        "nome": "gemini-2.0-flash-lite",
        "configuracoes": {
          "temperature": 0.4,
          "max_output_tokens": 256,
          "top_k": 10,
          "top_p": 0.75
        },
        "disponibilidade": "Gratuito",
        "descricao": "Baixa latência e custo eficiente."
      }
    ]
  },
  "export_format": "txt"
}
```

Após salvar as alterações, o JAM-Tree lerá as novas configurações na próxima execução.

## Conclusão

Utilizar um arquivo de configuração permite uma personalização simples e centralizada do JAM-Tree, facilitando a adaptação da ferramenta ao seu ambiente e fluxo de trabalho. Mantenha o `config.json` atualizado conforme necessário para aproveitar ao máximo as funcionalidades do JAM-Tree.
