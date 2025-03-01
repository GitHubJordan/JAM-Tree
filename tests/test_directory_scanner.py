import os
import shutil
from pathlib import Path
import pytest
from jam_tree.directory_scanner import scan_directory

@pytest.fixture
def temp_project(tmp_path):
    # Cria uma estrutura temporária para testar
    project = tmp_path / "TestProject"
    project.mkdir()
    (project / "file1.txt").write_text("Conteúdo 1")
    (project / "dir1").mkdir()
    (project / "dir1" / "file2.txt").write_text("Conteúdo 2")
    # Cria um diretório que deve ser ignorado
    (project / "venv").mkdir()
    (project / "venv" / "ignore.txt").write_text("Ignore this")
    return project

def test_scan_directory(temp_project):
    # Testa se a função ignora "venv" e lê a estrutura corretamente
    tree = scan_directory(temp_project, ignore_dirs=["venv"])
    # Verifica se "file1.txt" está presente e "venv" foi ignorado
    assert "file1.txt" in tree
    assert "venv" not in tree
    # Verifica se o diretório "dir1" contém "file2.txt"
    assert "dir1" in tree
    assert tree["dir1"].get("file2.txt") == "file"
