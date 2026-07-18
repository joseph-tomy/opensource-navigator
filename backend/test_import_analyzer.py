from pprint import pprint

from analyzers.import_analyzer import analyze_dependencies

report = analyze_dependencies(".")

pprint(report)