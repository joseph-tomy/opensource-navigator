from pprint import pprint

from analyzers.dependency_resolver import resolve_dependencies

report = resolve_dependencies(".")

pprint(report)