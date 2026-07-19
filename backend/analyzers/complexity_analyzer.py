"""
complexity_analyzer.py

Version 1

Calculates simple code metrics for every Python file.
"""

from pathlib import Path

from analyzers.ast_parser import parse_python_file


def analyze_complexity(repo_path: str) -> dict:
    """
    Analyze repository complexity.

    Args:
        repo_path (str): Repository path

    Returns:
        dict
    """

    repo = Path(repo_path)

    if not repo.exists():
        raise FileNotFoundError(f"Repository not found: {repo_path}")

    report = {}

    for python_file in repo.rglob("*.py"):

        ast_report = parse_python_file(str(python_file))

        with open(
            python_file,
            "r",
            encoding="utf-8"
        ) as file:

            lines = file.readlines()

        total_lines = len(lines)

        blank_lines = 0
        comment_lines = 0

        for line in lines:

            stripped = line.strip()

            if stripped == "":
                blank_lines += 1

            elif stripped.startswith("#"):
                comment_lines += 1

        report[python_file.name] = {

            "lines": total_lines,

            "blank_lines": blank_lines,

            "comment_lines": comment_lines,

            "functions": len(ast_report["functions"]),

            "classes": len(ast_report["classes"]),

            "imports": len(ast_report["imports"])
        }

    return report