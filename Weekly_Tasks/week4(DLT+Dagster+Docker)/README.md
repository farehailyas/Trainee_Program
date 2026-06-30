# GitHub + OpenAQ ETL Pipeline | Dagster & Docker

Multi-source ETL pipeline orchestrated with Dagster, containerized with Docker, and deployed to Snowflake.

**Topics:** dlt assets, Dagster orchestration, GitHub + OpenAQ sources, Docker, Snowflake.

---

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

`docker-compose up` spins up:
- ✅ PostgreSQL (run & schedule storage)
- ✅ Dagster webserver (UI on port 3000)
- ✅ Dagster daemon (runs scheduled jobs)
- ✅ User code container (your pipeline)

---
## Configuration
### `.env` (dlt credentials)
```
GITHUB_API_KEY=your_github_token
OPENAQ_API_KEY=your_openaq_key

### Orchestration
- **Jobs:** Materialize all assets on schedule
- **Schedules:** Daily (or custom interval)
- **Sensors:** Event-driven triggers (optional)

### Destination
- **Snowflake:** Schema per source (github_data, openaq_data)
- **Merge Strategy:** Historical + incremental loads

---

## Running Pipelines

### Option 1: Docker (Production)
```bash
docker-compose up
```
Then trigger from Dagster UI (http://localhost:3000).
