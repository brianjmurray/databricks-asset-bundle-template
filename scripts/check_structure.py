"""Offline source checks; does not authenticate, deploy, or execute Spark."""
import ast
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
notebooks = list(root.rglob("*.ipynb"))
for path in notebooks:
    nb = json.loads(path.read_text())
    assert nb["nbformat"] == 4, path
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            ast.parse("".join(cell["source"]))
schema = json.loads((root / "templates/databricks_template_schema.json").read_text())
assert len(schema["properties"]) == 7
assert (root / "templates/template/src/{{.project_name}}_{{.data_source}}ToGold.ipynb").is_file()
readme_path = root / "templates/template/README.md.tmpl"
readme = readme_path.read_text()
assert not (root / "templates/README.md").exists(), "Redundant README"
assert not (root / "templates/template/README.md").exists(), "Untemplated README"
import re
fields = set(re.findall(r"{{\.([a-z_]+)}}", readme))
assert fields == set(schema["properties"]), fields
assert len(re.findall(r"{{", readme)) == len(re.findall(r"{{\.[a-z_]+}}", readme))
for section in ("Project structure", "Daily development workflow", "Review and promotion", "Azure DevOps integration"):
    assert f"## {section}" in readme, section
print(f"PASS: {len(notebooks)} notebooks parse; code cells compile; seven template prompts; README structure and template fields checked")
