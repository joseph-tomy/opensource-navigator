from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

REPOSITORIES_DIR = BASE_DIR / "repositories"

MAX_REPOSITORY_SIZE_MB = 500

SUPPORTED_LANGUAGES = [
    ".py",
    ".js",
    ".ts",
    ".java"
]