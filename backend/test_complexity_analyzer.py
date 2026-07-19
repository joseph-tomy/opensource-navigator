from pprint import pprint

from analyzers.complexity_analyzer import analyze_complexity

report = analyze_complexity(".")

pprint(report)