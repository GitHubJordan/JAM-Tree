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
