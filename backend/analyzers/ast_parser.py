"""
ast_parser.py

Parses Python source code using Python's built-in AST module.
"""

import ast
from pathlib import Path


def parse_python_file(file_path: str) -> dict:
    """
    Parse a Python file and extract:

    - Imports
    - Classes
    - Functions
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    report = {
        "file_name": file_path.name,
        "imports": [],
        "classes": [],
        "functions": []
    }

    for node in ast.walk(tree):

        # import os
        if isinstance(node, ast.Import):
            for module in node.names:
                report["imports"].append(module.name)

        # from pathlib import Path
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                report["imports"].append(node.module)

        # class User:
        elif isinstance(node, ast.ClassDef):
            report["classes"].append(node.name)

        # def login():
        elif isinstance(node, ast.FunctionDef):
            report["functions"].append(node.name)

    return report