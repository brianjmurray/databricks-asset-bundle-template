# Generated Databricks bundle

This Declarative Automation Bundle is a starting scaffold, not a complete ingestion implementation.

## Development

1. Create a feature branch in your own repository.
2. Authenticate the Databricks CLI to your intended workspace with a named profile.
3. Review catalogs, schemas, permissions and workspace targets in `databricks.yml`.
4. Implement transformations in the single `src/*ToGold.ipynb` starter notebook.
5. Check configuration with `databricks bundle validate -t dev --profile YOUR_PROFILE`.
6. Review resource settings before deploying or running anything.

Targets: `dev` is personal development, `rc` is staging in development mode, and `prod` is production mode. The job has an hourly schedule; review before production deployment.

`resources/` defines the job and pipeline. `scratch/` is for exploration but is not explicitly excluded from synchronization.

## CI/CD example

The Azure DevOps `*-pipeline.yml` depends on the external `dbx.build` repository, its shared pipeline template, and `dbxDev`, `dbxStaging`, and `dbxProd` variable groups. Supply or replace these, review path filters and working directories, and configure authentication/approvals. Initialization does not create approval gates or CI/CD infrastructure.
