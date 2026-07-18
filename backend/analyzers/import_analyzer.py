"""
dependency_analyzer.py

Analyzes dependencies between Python files by
extracting imported modules.
"""

from pathlib import Path

from analyzers.ast_parser import parse_python_file


def analyze_dependencies(repo_path: str) -> dict:
    """
    Analyze dependencies for every Python file
    in a repository.

    Args:
        repo_path (str): Repository path.

    Returns:
        dict: Dependency report.
    """

    repo = Path(repo_path)

    if not repo.exists():
        raise FileNotFoundError(f"Repository not found: {repo_path}")

    dependency_report = {}

    # Search every Python file
    for python_file in repo.rglob("*.py"):

        ast_report = parse_python_file(str(python_file))

        dependency_report[python_file.name] = {
            "imports": ast_report["imports"]
        }

    return dependency_report