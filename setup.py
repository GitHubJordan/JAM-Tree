from setuptools import setup, find_packages
import pathlib

root = pathlib.Path(__file__).parent.resolve()
long_description_path = (root / "README.md").read_text(encoding="utf-8")

setup(
    name="jam-tree",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.8",
        "rich>=13.9.4",
        "google-genai>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "jam-tree=jam_tree.cli:cli",
        ],
    },
    author="Jordan Adelino",
    author_email="jordanadelino.info@gmail.com",
    description="Ferramenta para gerar árvore de diretórios com análise de IA",
    long_description=long_description_path,
    long_description_content_type="text/markdown",
    url="https://github.com/GitHubJordan/JAM-Tree",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools :: Framework",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="jam-tree, setuptools, development",
    project_urls={
        "Documentation": "",
        "Bug Reports": "https://github.com/GitHubJordan/JAM-Tree/issues",
        "Funding": "https://airtm.me/jordan_adelino",
        "Say Thanks!": "https://jordanadelino.info",
        "Source": "https://github.com/GitHubJordan/JAM-Tree/",
    },
)
