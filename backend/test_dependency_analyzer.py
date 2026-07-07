from pprint import pprint

from analyzers.dependency_analyzer import analyze_dependencies

report = analyze_dependencies(".")

pprint(report)