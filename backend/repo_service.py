"""
repo_service.py

Coordinates all repository analyzers and returns
a single repository report.
"""

from analyzers.file_scanner import scan_repository
from analyzers.language_detector import detect_languages


def analyze_repository(repo_path: str) -> dict:
    """
    Perform complete repository analysis.

    Args:
        repo_path (str): Path to the repository.

    Returns:
        dict: Combined repository report.
    """

    # Step 1: Scan the repository
    report = scan_repository(repo_path)

    # Step 2: Detect programming languages
    languages = detect_languages(report["extensions"])

    # Step 3: Add languages to report
    report["languages"] = languages

    return report