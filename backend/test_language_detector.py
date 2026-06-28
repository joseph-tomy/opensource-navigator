from analyzers.language_detector import detect_languages

extensions = {
    ".py": 12,
    ".js": 6,
    ".tsx": 3,
    ".md": 2,
    ".xyz": 5
}

languages = detect_languages(extensions)

print(languages)