-- table = duckdb_issues
-- checking primary key 
-- this query gave no results as there are no duplicates in this coloumn (NUMBER)
SELECT NUMBER, COUNT(*) as primary_key_duplicates
FROM ISSUES
GROUP BY NUMBER
HAVING COUNT(*) > 1;

-- check for null values
-- this query gave no results as there are no NULL VALUES in this coloumn (NUMBER)

SELECT NUMBER, COUNT(*) as primary_key_null
FROM ISSUES
GROUP BY NUMBER
HAVING NUMBER IS NULL;
-- """NUMBER colom can be choosen as primary as it is unique and donot have any null vlaues """

SELECT table_name ,column_name , data_type
FROM information_schema.columns
WHERE table_schema = 'DUCKDB_ISSUES' and table_name = 'ISSUES';

-- Check issues state
-- query gave result two states (open and close) which is correct
SELECT STATE
FROM ISSUES
GROUP BY STATE;

-- CHECK IF Repository is null or not
-- query gave no result which means every issues is associated with valid repo 
SELECT URL
FROM ISSUES
WHERE URL IS NULL;

-- check if author login is null 
-- query gave no result as there is no issue having no author associated
SELECT AUTHOR__LOGIN
FROM ISSUES
WHERE AUTHOR__LOGIN IS NULL

-- check if issue is closed then closed_
-- query gave no result means closed issues have closing timestampe 

SELECT STATE
FROM ISSUES
WHERE STATE = 'CLOSED'AND CLOSED_AT IS NULL;

-- CHECK IF issue is open then it should be null in closing time
-- no result as open issues have not closing timestamp specified. 
SELECT STATE
FROM ISSUES
WHERE STATE = 'OPEN'AND CLOSED_AT IS NOT NULL;



-- table = push_events
-- check data types
SELECT table_name ,column_name , data_type
FROM information_schema.columns 
WHERE table_schema = 'AIRFLOW_EVENTS' AND table_name = 'PUSH_EVENT';
-- check primary key (Id should be unique)
-- no results means I is unique and can be primary key

SELECT ID, COUNT(*) as id_duplicates
FROM PUSH_EVENT
GROUP BY ID
HAVING COUNT(*) > 1;

-- check if ID has null values
-- no results means all events have ID
SELECT COUNT(*) as null_id_count
FROM PUSH_EVENT
WHERE ID IS NULL;

-- check if ACTORLOGIN is null
-- no results means every event has an actor
SELECT COUNT(*) as null_actor_count
FROM PUSH_EVENT
WHERE ACTOR__LOGIN IS NULL;

-- check if REPOID is null
-- no results means every event is associated with a repository
SELECT COUNT(*) as null_repo_count
FROM EVENTS
WHERE REPO__ID IS NULL;


-- check if ORG_ID is null
-- shows how many events have no organization
SELECT COUNT(*) as null_org_count
FROM PUSH_EVENT
WHERE ORG__ID IS NULL;


-- check if actor id and its login present at same time or not
SELECT COUNT(*) as actor_mismatch
FROM PUSH_EVENT
WHERE (ACTOR__ID IS NULL AND ACTOR__LOGIN IS NOT NULL)
   OR (ACTOR__ID IS NOT NULL AND ACTOR__LOGIN IS NULL);