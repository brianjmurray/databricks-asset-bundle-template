# Custom template source

This is the template root for **Declarative Automation Bundles (formerly Databricks Asset Bundles)**.

From the repository root:

```sh
databricks bundle init ./templates
```

Or from GitHub:

```sh
databricks bundle init https://github.com/brianjmurray/databricks-asset-bundle-template --template-dir templates
```

`databricks_template_schema.json` defines seven prompts; `template/` contains generated-file sources. Output includes one job, one SDP pipeline, one configuration-only starter notebook, a scratch notebook and an Azure DevOps example. It does not generate separate bronze/silver/gold notebooks or dashboard resources.

The Azure DevOps example depends on an external `dbx.build` template repository and variable groups. See the [root README](../README.md) for the output tree, target names and prerequisites.
