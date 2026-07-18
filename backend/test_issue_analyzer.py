from pprint import pprint
from analyzers.issue_analyzer import analyze_issue

print("Starting test...")

report = analyze_issue(
    ".",
    "Login fails after password reset"
)

print("Analysis complete")

pprint(report)