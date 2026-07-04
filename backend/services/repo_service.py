from analyzers.file_scanner import scan_repository
from analyzers.language_detector import detect_languages
from services.github_service import clone_repository


def analyze_repository(repo_path: str) -> dict:
    """
    Analyze either a local repository or a GitHub repository.
    """

    # If user provides a GitHub URL,
    # clone it first.
    if repo_path.startswith("https://github.com"):
        repo_path = clone_repository(repo_path)

    # Scan repository
    report = scan_repository(repo_path)

    # Detect languages
    report["languages"] = detect_languages(
        report["extensions"]
    )

    return report