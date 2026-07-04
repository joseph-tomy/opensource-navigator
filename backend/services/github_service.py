"""
github_service.py

Handles GitHub repository cloning.
"""

from pathlib import Path

from git import Repo

from config import REPOSITORIES_DIR


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository.

    Args:
        repo_url (str): GitHub repository URL.

    Returns:
        str: Local repository path.
    """

    # Example:
    # https://github.com/pallets/flask.git
    # Repository name becomes "flask"

    repo_name = repo_url.rstrip("/").split("/")[-1]

    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    local_path = REPOSITORIES_DIR / repo_name

    # Don't clone again if already exists
    if local_path.exists():
        print(f"{repo_name} already exists.")
        return str(local_path)

    print(f"Cloning {repo_name}...")

    Repo.clone_from(repo_url, local_path)

    print("Clone complete.")

    return str(local_path)