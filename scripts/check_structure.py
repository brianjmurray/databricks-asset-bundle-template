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
print(f"PASS: {len(notebooks)} notebooks parse; code cells compile; seven template prompts")
