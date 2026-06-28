"""
language_detector.py

Converts file extensions collected by the file scanner
into human-readable programming languages.
"""

EXTENSION_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "JavaScript (React)",
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".h": "C/C++ Header",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".json": "JSON",
    ".xml": "XML",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".sql": "SQL",
    ".md": "Markdown",
    ".txt": "Text",
    ".sh": "Shell",
    ".bat": "Batch",
    ".dockerfile": "Docker"
}


def detect_languages(extensions: dict) -> dict:
    """
    Convert file extensions into programming language counts.

    Args:
        extensions (dict):
            Example:
            {
                ".py": 15,
                ".js": 8
            }

    Returns:
        dict:
            Example:
            {
                "Python": 15,
                "JavaScript": 8
            }
    """

    languages = {}

    for extension, count in extensions.items():

        language = EXTENSION_MAP.get(extension, "Unknown")

        languages[language] = (
            languages.get(language, 0) + count
        )

    return languages