import dlt
from dlt.sources.sql_database import sql_database

def load_from_postgres():
    
    source = sql_database(
        "postgresql://postgres:mysecret@localhost:5433/chinook"
    ).with_resources("artist", "album" , "customer" , "employee" , "genre" , "invoice" , "invoice_line" , "media_type" , "playlist" , "playlist_track" ,"track")
    
    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_duckdb",
        destination="duckdb",  # ADD THIS BACK
        dataset_name="chinook_data"
    )
    
    load_info = pipeline.run(source)
    print(load_info)

load_from_postgres()