# Trainee Program | Week 4 Progress Report

## Overview
Deployed dlt pipelines on Dagster and containerized with Docker. Built multi-source ETL (GitHub + OpenAQ) with orchestration.

learned about assets , jobs , definitions and sensors
Created two assets and jobs which materializes github and openAQ rest_api 
Created a sensor which triggers a job when an asset is materialize
Wrap everything up in definitons to run the pipeline

## Quick Start

### Prerequisites
- Docker & Docker Compose installed
- `.env` file with dlt credentials (GitHub API key, OpenAQ)

### Run Dockerized Pipeline

```bash
cd github-openq_pipeline/dagster-quickstart
docker-compose up
```
Open **http://localhost:3000** → Dagster UI to trigger or schedule runs.

---

## What Happens

`docker-compose up`:
- PostgreSQL (run & schedule storage)
- Dagster webserver (UI on port 3000)
- Dagster daemon (runs scheduled jobs)
- User code container (your pipeline)

---
## Configuration
### `.env` (dlt credentials)
```
GITHUB_API_KEY=your_github_token
OPENAQ_API_KEY=your_openaq_key
