"""
ranking_engine.py

Combines results from multiple analyzers
to rank repository files.
"""

from analyzers.issue_analyzer import analyze_issue
from analyzers.dependency_resolver import resolve_dependencies
from analyzers.complexity_analyzer import analyze_complexity


def rank_repository(repo_path: str, issue: str) -> list:
    """
    Rank repository files for a given issue.

    Args:
        repo_path (str): Repository path.
        issue (str): GitHub issue.

    Returns:
        list
    """

    issue_report = analyze_issue(repo_path, issue)
    dependency_report = resolve_dependencies(repo_path)
    complexity_report = analyze_complexity(repo_path)

    ranking = []

    for match in issue_report["matches"]:

        file_name = match["file"]

        issue_score = match["score"]

        dependency_score = len(
            dependency_report.get(
                file_name,
                {}
            ).get(
                "local_dependencies",
                []
            )
        )

        complexity_score = complexity_report.get(
            file_name,
            {}
        ).get(
            "functions",
            0
        )

        final_score = (
            issue_score * 5 +
            dependency_score * 2 +
            complexity_score
        )

        ranking.append({

            "file": file_name,

            "issue_score": issue_score,

            "dependency_score": dependency_score,

            "complexity_score": complexity_score,

            "final_score": final_score

        })

    ranking.sort(

        key=lambda x: x["final_score"],

        reverse=True

    )

    return ranking