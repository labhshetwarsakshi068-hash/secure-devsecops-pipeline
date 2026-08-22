import json
import html

with open("trivy-report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for result in data.get("Results", []):
    target = result.get("Target", "")
    for vuln in result.get("Vulnerabilities", []) or []:
        rows.append({
            "target": target,
            "id": vuln.get("VulnerabilityID", ""),
            "package": vuln.get("PkgName", ""),
            "severity": vuln.get("Severity", ""),
            "installed": vuln.get("InstalledVersion", ""),
            "fixed": vuln.get("FixedVersion", "")
        })

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Trivy Security Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #eee; }
    </style>
</head>
<body>
<h1>Trivy Security Report</h1>
<table>
<tr>
<th>Target</th>
<th>Vulnerability ID</th>
<th>Package</th>
<th>Severity</th>
<th>Installed Version</th>
<th>Fixed Version</th>
</tr>
"""

for row in rows:
    html_content += f"""
<tr>
<td>{html.escape(row["target"])}</td>
<td>{html.escape(row["id"])}</td>
<td>{html.escape(row["package"])}</td>
<td>{html.escape(row["severity"])}</td>
<td>{html.escape(row["installed"])}</td>
<td>{html.escape(row["fixed"])}</td>
</tr>
"""

html_content += """
</table>
</body>
</html>
"""

with open("trivy-report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML report generated successfully: trivy-report.html")