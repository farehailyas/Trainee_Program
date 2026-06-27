# Data Quality Checks - Snowflake dlt Pipeline

## Overview
This project loads data from two sources (Stripe and REST API) into Snowflake using dlt, then applies quality validation checks on GitHub verified data sources.

## Data Sources
- **Stripe** - Payment and transaction data
- **REST API** - External API data  (https://api.restcountries.com/countries/v5)
- **GitHub** - Issues and events data (quality verified)

## Quality Checks Performed

### ISSUES Table
- **Primary Key Validation**: NUMBER column is unique with no duplicates
- **Null Check**: NUMBER column has no null values - suitable as primary key
- **State Validation**: All issues have valid states (OPEN or CLOSED)
- **Repository Association**: All issues are linked to valid repositories (URL not null)
- **Author Verification**: Every issue has an associated author (AUTHOR__LOGIN not null)
- **Timestamp Consistency**: 
  - Closed issues always have a CLOSED_AT timestamp
  - Open issues never have a CLOSED_AT timestamp

### PUSH_EVENT Table
- **Primary Key Validation**: ID column is unique with no duplicates
- **Null Checks**:
  - All events have an ID
  - All events have an actor (ACTOR__LOGIN not null)
  - All events are associated with a repository (REPO__ID not null)
- **Organization Check**: Identifies events without organization association
- **Actor Data Consistency**: Ensures ACTOR__ID and ACTOR__LOGIN are both present or both absent (no mismatches)

## Result Summary
✓ All primary key constraints validated  
✓ All  necessary check for nulls
✓ Checks for wrong data types
