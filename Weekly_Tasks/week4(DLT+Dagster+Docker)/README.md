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
