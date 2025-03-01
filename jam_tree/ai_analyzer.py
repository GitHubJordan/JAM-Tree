import os
import re
import hashlib
import json
import atexit
import google.generativeai as genai
from typing import Dict

# Arquivo de cache persistente (na raiz do projeto)
CACHE_FILE = ".jam_tree_cache.json"
_cache: Dict[str, str] = {}

def load_cache():
    global _cache
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                _cache = json.load(f)
        except Exception:
            _cache = {}

def save_cache():
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(_cache, f)
    except Exception as e:
        print(f"Erro ao salvar cache: {e}")

load_cache()
atexit.register(save_cache)

def get_content_hash(content: str) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def clean_summary(text: str) -> str:
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = " ".join(text.split())
    if len(text) > 64:
        text = text[:61] + "..."
    return text

def get_model(default: str) -> str:
    return os.getenv("AI_ANALYZER_MODEL", default)

def analyze_file(content: str) -> str:
    key = get_content_hash(content)
    # Se o cache já contém um resultado válido, retorne-o.
    if key in _cache:
        cached_result = _cache[key]
        # Se o resultado armazenado é um erro, reanalisar
        if cached_result.startswith("Erro na análise AI"):
            pass
        else:
            return cached_result
    
    api_key = os.getenv("AI_ANALYZER_API_KEY_GEMINI")
    if not api_key:
        return "Chave da API Gemini não configurada."
    
    genai.configure(api_key=api_key)
    model_name = get_model("gemini-1.5-flash")
    model = genai.GenerativeModel(model_name)
    
    try:
        prompt = f"""
        Você é um especialista em análise de código.
        Resuma a funcionalidade principal do seguinte código em uma frase de até 64 caracteres.
        Exemplo:
        Código: def hello_world(): print("Hello, World!")
        Descrição: Função que imprime "Hello, World!".
        Código: {content}
        Descrição:
        """
        response = model.generate_content(prompt)
        if response and hasattr(response, "text") and response.text:
            summary = clean_summary(response.text.strip())
            if summary.startswith("Erro na análise AI") or "429 Resource has been exhausted (e.g. check quota)." in summary:
                summary = "N/A"
        else:
            summary = "Sem resumo."
    except Exception as e:
        summary = f"Erro na análise AI: {e}"
    
    # Só armazena no cache se o resultado não for um erro.
    if not summary.startswith("Erro na análise AI"):
        _cache[key] = summary
    return summary

def analyze_node(name: str, is_dir: bool) -> str:
    key = hashlib.md5(name.encode('utf-8')).hexdigest()
    if key in _cache:
        cached_result = _cache[key]
        if cached_result.startswith("Erro na análise AI"):
            pass
        else:
            return cached_result
    
    api_key = os.getenv("AI_ANALYZER_API_KEY_GEMINI")
    if not api_key:
        return "Chave da API Gemini não configurada."
    
    genai.configure(api_key=api_key)
    model_name = get_model("gemini-1.5-flash")
    model = genai.GenerativeModel(model_name)
    
    try:
        if is_dir:
            prompt = f"""
            Você é um especialista em estruturas de projetos.
            Forneça uma breve descrição (até 64 caracteres) para uma pasta chamada "{name}".
            Descrição:
            """
        else:
            prompt = f"""
            Você é um especialista em análise de código.
            Resuma a funcionalidade principal do arquivo "{name}" em até 64 caracteres.
            Descrição:
            """
        response = model.generate_content(prompt)
        if response and hasattr(response, "text") and response.text:
            summary = clean_summary(response.text.strip())
            if summary.startswith("Erro na análise AI") or "429 Resource has been exhausted (e.g. check quota)." in summary:
                summary = "N/A"
        else:
            summary = "Sem descrição."
    except Exception as e:
        summary = f"Erro na análise AI: {e}"
    
    if not summary.startswith("Erro na análise AI"):
        _cache[key] = summary
    return summary

def analyze_file_detailed(content: str) -> str:
    api_key = os.getenv("AI_ANALYZER_API_KEY_GEMINI")
    if not api_key:
        return "Chave da API Gemini não configurada."
    
    genai.configure(api_key=api_key)
    model_name = get_model("gemini-1.5-pro")
    model = genai.GenerativeModel(model_name)
    
    try:
        prompt = f"""
        Você é um especialista em análise de código.
        Analise o código abaixo e forneça uma explicação detalhada:
        1. O que ele faz?
        2. Principais funções e classes.
        3. Como ele se integra a um projeto maior?
        4. Sugestões de melhorias.
        5. Conclusão.

        Código: {content}
        Explicação:
        """
        response = model.generate_content(prompt)
        if response and hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "Sem explicação."
    except Exception as e:
        return f"Erro na análise AI: {e}"
