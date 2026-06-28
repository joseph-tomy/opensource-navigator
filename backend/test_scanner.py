from analyzers.file_scanner import scan_repository

report = scan_repository(".")

print(report)