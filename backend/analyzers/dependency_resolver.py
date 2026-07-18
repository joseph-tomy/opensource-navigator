"""
dependency_resolver.py

Resolves imported modules into actual
repository file dependencies.
"""

from pathlib import Path

from analyzers.import_analyzer import analyze_dependencies


def resolve_dependencies(repo_path: str) -> dict:
    """
    Resolve imports into local and external dependencies.

    Args:
        repo_path (str): Repository path.

    Returns:
        dict: Dependency resolution report.
    """

    repo = Path(repo_path)

    if not repo.exists():
        raise FileNotFoundError(f"Repository not found: {repo_path}")

    # Get imports from import analyzer
    dependency_report = analyze_dependencies(repo_path)

    # ------------------------------------
    # Build lookup table
    # ------------------------------------
    module_lookup = {}

    for python_file in repo.rglob("*.py"):
        module_lookup[python_file.stem] = python_file.name

    # ------------------------------------
    # Resolve dependencies
    # ------------------------------------
    resolved_report = {}

    for file_name, data in dependency_report.items():

        local_dependencies = []
        external_dependencies = []

        for module in data["imports"]:

            if module in module_lookup:

                local_dependencies.append(
                    module_lookup[module]
                )

            else:

                external_dependencies.append(module)

        resolved_report[file_name] = {

            "local_dependencies": local_dependencies,

            "external_dependencies": external_dependencies

        }

    return resolved_report