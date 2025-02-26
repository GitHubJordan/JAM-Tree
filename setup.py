from setuptools import setup, find_packages

setup(
    name="jam-tree",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "jam-tree=jam_tree.cli:main",
        ],
    },
    author="Jordan Adelino",
    description="Ferramenta para gerar árvore de diretórios com análise de IA",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GitHubJordan/jam-tree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
