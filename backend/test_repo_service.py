from services.repo_service import analyze_repository
from pprint import pprint

report = analyze_repository(".")

pprint(report)