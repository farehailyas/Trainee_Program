# Trainee Program | Week 3 Progress Report

## Overview
Built dlt pipeline projects ingesting APIs (OpenAQ, GitHub) into Snowflake.

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

