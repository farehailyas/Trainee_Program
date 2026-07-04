# ELT Mini Project: Stack Exchange Data Pipeline

## Setup

→ Clone repo & enter directory
```bash
git clone https://github.com/farehailyas/Trainee_Program
cd MiniProjects_Excercises/ELT_Mini_Project
```

→ Create virtual environment
```bash
uv venv
```

→ Activate (Linux)
```bash
source .venv/bin/activate
```

→ Install dependencies
```bash
uv pip install -r requirements.txt
```

→ Run Dagster
```bash
dagster dev -m dagster_project.definitions
```

→ Open `localhost:3000` in browser

---

## Architecture

```
Stack Exchange API
        ↓
    dlt Source (6 resources: users, questions, answers, comments, tags, badges)
        ↓
    DuckDB (raw_stackexchange schema)
        ↓
    Dagster Assets (historical & incremental loads)
        ↓
    dbt Transforms (staging → intermediate → mart)
        ↓
    Analytics Models
```

---

## Pipeline Modes

### Historical Load (One-time)
→ Fetches all data from Stack Exchange API  
→ Asset: `stack_exchange_historical`  
→ Run manually via Dagster UI (click play button on historical asset)  
→ Then dbt transforms execute (`dbt build`)

### Incremental Load (Scheduled)
→ Fetches only new/updated records since last run  
→ Asset: `stack_exchange_incremental`  
→ **Schedule:** 6:30 PM PKT (`18:30 Asia/Karachi`) daily  
→ Automatically triggers dbt transforms after load  
→ Uses dlt's `incremental()` tracking per resource

---

## Jobs & Scheduling

| Job | Trigger | Assets |
|-----|---------|--------|
| `stack_exchange_historical_job` | Manual | historical asset + dbt |
| `stack_exchange_incremental_job` | Daily 6:30 PM PKT | incremental asset + dbt |

→ View schedule in Dagster UI → Schedules tab  
→ All jobs run both dlt load + dbt transforms together

---

## dbt Models (Business Questions)

### Model Count Guideline

**Staging**

One staging model is created for each raw source (including nested tables)

Responsibilities include:
- column renaming
- timestamp conversion
- preserving source grain

**Intermediate**

Intermediate models encapsulate reusable business logic, such as:
- question-tag mapping
- first answer per question
- engagement metrics
- user badge totals
- daily entity counts

These models are reused across multiple marts to avoid duplicating transformations.

**Mart**

Each business question is answered by a dedicated mart model.

| Business Question | Model |
|-------------------|-------|
| Which tags generate the highest engagement (views, answers, comments per question)? | `dim_question_engagement` |
| Who are the top contributing users by reputation, badges earned, and accepted-answer rate? | `dim_user_contribution` |
| What is the average time-to-first-answer per tag, and how does it trend over time? | `dim_furst_answer_time` |
| What is the daily/weekly volume of new questions, answers, comments, and badges? | `dim_daily_volume` |
| Which high-view questions remain unanswered or have a low answer-to-view ratio? | `dim_unanswered_question` |
| What is the distribution of badge classes (gold/silver/bronze) awarded per day? | `fct_badge_distrubution` |

---

## Example: Tag Engagement Mart Model

**Which tags generate the highest engagement?**

**Flow:**
```
stg_questions + stg_questions_tags
       ↓
  int_question_tag
       ↓
stg_questions + stg_comments
       ↓
  int_question_engagement
       ↓
int_question_tag + int_question_engagement
       ↓
  int_tag_engagement
       ↓
  dim_question_engagement (ranks tags by views, answers, comments)
```

---

## Data Limitations

→ Have 25 pages with anonymous key  
→ Per page have 100 size  
→ In model (fct_badge_distrubution) cannot find distribution over day as it is fixed metadata resource not the changing one
→ Data is static and not changing so did not add incremental materialization in dbt modeling
---

## Schema & Documentation

### Schema Audit
→ schema_audit.txt is added to understand raw data structure

### dbt Docs & Lineage Graph
Further to see lineage graph:
```bash
cd dbt_project
dbt docs generate
dbt docs serve
```