from pprint import pprint

from analyzers.ast_parser import parse_python_file

report = parse_python_file("app.py")

pprint(report)