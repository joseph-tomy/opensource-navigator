from services.github_service import clone_repository

path = clone_repository(
    "https://github.com/pallets/flask.git"
)

print(path)