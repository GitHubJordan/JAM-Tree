from setuptools import setup, find_packages
import pathlib

root = pathlib.Path(__file__).parent.resolve()
long_description_path = (root / "README.md").read_text(encoding="utf-8")

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
    author_email="jordanadelino.info@gmail.com",
    description="Ferramenta para gerar árvore de diretórios com análise de IA",
    long_description=long_description_path,
    long_description_content_type="text/markdown",
    url="https://github.com/GitHubJordan/jam-tree",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="jam-tree, setuptools, development",
    project_urls={
        "Bug Reports": "https://github.com/GitHubJordan/JAM-Tree/issues",
        "Funding": "https://airtm.me/jordan_adelino",
        "Say Thanks!": "https://jordanadelino.info",
        "Source": "https://github.com/GitHubJordan/JAM-Tree/",
    },
)
