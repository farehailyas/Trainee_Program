# Trainee Program | Week 4 Progress Report

## Overview
Deployed dlt pipelines on Dagster and containerized with Docker. Built multi-source ETL (GitHub + OpenAQ) with orchestration.

## Topics Covered

### Dagster Integration
- Assets (`@dlt_asset`), jobs, schedules, sensors using dlt resources
- Asset definitions 
- Dagster UI for pipeline monitoring

### Pipeline Orchestration
- GitHub source: repos → events, stargazers, reactions
- OpenAQ source: locations → sensors → measurements
- Merge strategy for historical loads
- Snowflake destination with schema management

### Dockerization
- Multi-container setup: user code, webserver, daemon, PostgreSQL
- `Dockerfile_user_code`: packages pipeline code + dependencies
- `Dockerfile_dagster`: Dagster orchestration layer
- `docker-compose.yaml`: container orchestration
- `dagster.yaml`: PostgreSQL run storage, schedule storage, DockerRunLauncher
- `workspace.yaml`: code location registration

### Deployment Configuration
- Environment variables for Snowflake credentials (user, password, account, warehouse, database)
- dlt credentials via `.env`
- Module-based code loading (`-m src.dagster_quickstart.definitions`)
- Dynamic path resolution for multi-package imports

## Projects
- Full GitHub + OpenAQ ETL pipeline
- Scheduled runs with Dagster daemon
- Docker containers for dev/prod parity
- Web UI monitoring on port 3000

## Approach
Debugged Dockerfile path issues, module imports, environment variable loading, and submodule dependencies through live Docker execution.
# Trainee Program | Week 3 Progress Report

## Overview
Built 4 dlt pipeline projects ingesting APIs (OpenAQ, GitHub) into Snowflake.

## Topics Covered

### dlt Basics
- `@dlt.resource` decorators, pipeline execution, write dispositions (`append`, `replace`, `merge`), state management , increamental loading

### Verified Connectors
- GitHub connector with multi-level dependencies (repos → events/stargazers)

### Data Ingestion
- Single-source (OpenAQ), multisource (GitHub + OpenAQ), nested JSON flattening
- Incremental loading, foreign key mechanics (`_dlt_id`, `_dlt_parent_id`)
- Data quality checks (null audits, duplicates, freshness)

### Projects
- Day 1: OpenAQ single-source pipeline
- Day 2: GitHub verified connector
- Day 3: Incremental loading with state
- Day 4: Multi-source merge strategy

