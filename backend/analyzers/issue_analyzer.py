"""
issue_analyzer.py

Simple keyword-based issue analyzer.

Version 1:
Matches issue keywords against
file names, function names and class names.
"""

import re
from pathlib import Path

from analyzers.ast_parser import parse_python_file


def analyze_issue(repo_path: str, issue: str) -> dict:
    """
    Analyze a GitHub issue and find
    relevant files.

    Args:
        repo_path (str): Repository path
        issue (str): GitHub issue title/description

    Returns:
        dict
    """

    repo = Path(repo_path)

    if not repo.exists():
        raise FileNotFoundError(f"Repository not found: {repo_path}")

    # ----------------------------------------
    # Convert issue into keywords
    # ----------------------------------------

    keywords = re.findall(r"\w+", issue.lower())

    report = []

    # ----------------------------------------
    # Analyze every Python file
    # ----------------------------------------

    for python_file in repo.rglob("*.py"):

        ast_report = parse_python_file(str(python_file))

        score = 0

        searchable_text = []

        # filename
        searchable_text.append(
            python_file.stem.lower()
        )

        # functions
        searchable_text.extend(
            name.lower()
            for name in ast_report["functions"]
        )

        # classes
        searchable_text.extend(
            name.lower()
            for name in ast_report["classes"]
        )

        # imports
        searchable_text.extend(
            name.lower()
            for name in ast_report["imports"]
        )

        # Count keyword matches
        for keyword in keywords:

            for item in searchable_text:

                if keyword in item:
                    score += 1

        report.append({

            "file": python_file.name,

            "score": score

        })

    # Highest score first
    report.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {

        "issue": issue,

        "keywords": keywords,

        "matches": report

    }