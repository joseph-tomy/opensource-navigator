from pathlib import Path


def scan_repository(repo_path: str) -> dict:
    """
    Scan a repository and collect basic statistics.

    Args:
        repo_path (str): Path to the repository.

    Returns:
        dict: Repository statistics.
    """

    repo = Path(repo_path)

    # Check whether the path exists
    if not repo.exists():
        raise FileNotFoundError(f"Repository not found: {repo_path}")

    report = {
        "repository_name": repo.name,
        "repository_path": str(repo.resolve()),
        "total_files": 0,
        "total_directories": 0,
        "total_size_bytes": 0,
        "extensions": {}
    }

    # Walk through every file and folder
    for item in repo.rglob("*"):

        if item.is_dir():
            report["total_directories"] += 1

        elif item.is_file():

            report["total_files"] += 1

            # File size
            report["total_size_bytes"] += item.stat().st_size

            # File extension
            extension = item.suffix.lower()

            if extension == "":
                extension = "No Extension"

            report["extensions"][extension] = (
                report["extensions"].get(extension, 0) + 1
            )

    return report