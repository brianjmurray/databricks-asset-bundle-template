# template

The 'template' project is a template for other databricks asset bundles projects. It helps automate setup of DAB projects.

## Getting started

1. Install the Databricks CLI from https://docs.databricks.com/dev-tools/cli/databricks-cli.html

2. Create a databricks asset bundle using this template:
    ```
   mkdir my-test-bundle
   cd my-test-bundle
   databricks bundle init ../template

    ```
    
3. Install the Databricks extension for Visual Studio Code from
   https://docs.databricks.com/dev-tools/vscode-ext.html.

4. For documentation on the Databricks asset bundles format used
   for this project, and for CI/CD configuration, see
   https://docs.databricks.com/dev-tools/bundles/index.html.

## Project Structure
```plaintext
ProjectName/
├── resources/
│   ├── dlt_pipeline.yml 
│   ├── ProjectName_job.yml
├── scratch/
|   ├── exploration.ipynb
├── src/
│   ├── ProjectName_SilverToGoldDim.ipynb
│   ├── ProjectName_SilverToGoldFact.ipynb
│   ├── ProjectName_BronzeToSilver.ipynb
│   ├── ProjectName_DatalakeToBronze.ipynb
├── databricks.yml
├── ProjectName-pipeline.yml
├── README.md
```

## Explanation of Structure

### resources
The `resources` folder contains YAML files that define jobs and DLT pipelines. If a project is simple all pipelines and jobs can be defined in a single file (I would still separate pipelines from jobs to have at least 2 files.) As the project grows it can be easier to create a file per object. These pipelines orchestrate the data processing tasks and ensure that data flows smoothly from one stage to another. Key pipeline files include:

- `ProjectName_pipeline.yml`: Defines the Delta Live Tables pipeline.
- `ProjectName_job.yml`: Contains job configurations for the main data processing tasks.

### scratch
- `exploration.ipynb`: This is a notebook that can be used to retrieve data for research. Write queries for verifying data. It's meant to provide a space in the project for AD-HOC analysis with out having to leave the project.

### src

The `src` directory contains Jupyter notebooks that define source code for the data transformation process:

- `ProjectName_SilverToGoldDim.ipynb`: Processes data to create gold dimension tables.
- `ProjectName_SilverToGoldFact.ipynb`: Transforms silver-level data into gold-level fact data.
- `ProjectName_BronzeToSilver.ipynb`: Converts raw bronze-level data into cleaned silver-level data.
- `ProjectName_DatalakeToBronze.ipynb`: Ingests data from the data lake and converts it into bronze-level data.

### databricks.yml
This file specifies configuration for the project. Targets are the workspaces we deploy to and how to configure the Workflows. Variables that can be shared across the project such as values that can change across workspaces.

### *-pipeline.yml
This is the configuration file for the CI\CD pipeline that will deploy the project to workspaces. It passes parameters to a template pipeline in the dbx.build repo. This the main logic of deploying Databricks Asset Bundles projects is in one pipeline and if logic needs to be changed it can be managed in one file.

### README.md
Documentation for a specific project. An overview of the project and any info relevant to contributing or understanding the project.
