import time
import requests
import dlt


import time
import requests
import dlt
import logging
logger = logging.getLogger(__name__)

SORTS = {
    "users": "modified",
    "questions": "activity",
    "answers": "activity",
    "comments": "creation",
    "tags": "popular",
    "badges": "rank",
}

def fetch_resource(endpoint):
    page = 1

    while True:
        response = requests.get(
            f"https://api.stackexchange.com/2.3/{endpoint}",
            params={
                "site": "stackoverflow",
                "sort": SORTS[endpoint],
                "order": "desc",
                "pagesize": 100,
                "page": page,
            },
        )

        if response.status_code == 400:
            print(f"{endpoint}: stopping at page {page}")
            logger.info(f"{endpoint}: stopping at page {page}")
            break

        response.raise_for_status()

        data = response.json()

        yield from data["items"]
        
        if page > 25 :      # Anonymous API limit
            break
        if "backoff" in data:
            print(f"{endpoint}: sleeping {data['backoff']} seconds...")
            logger.info(f"{endpoint}: sleeping {data['backoff']} seconds...")
            time.sleep(data["backoff"])

        if not data.get("has_more", False):
            break


        page += 1


@dlt.resource(
    name="users",
    primary_key="user_id",
    write_disposition="merge",
)
def users():
    yield from fetch_resource("users")


@dlt.resource(
    name="questions",
    primary_key="question_id",
    write_disposition="merge",
)
def questions():
    yield from fetch_resource("questions")


@dlt.resource(
    name="answers",
    primary_key="answer_id",
    write_disposition="merge",
)
def answers():
    yield from fetch_resource("answers")


@dlt.resource(
    name="comments",
    primary_key="comment_id",
    write_disposition="merge",
)
def comments():
    yield from fetch_resource("comments")


@dlt.resource(
    name="tags",
    primary_key="name",
    write_disposition="merge",
)
def tags():
    yield from fetch_resource("tags")


@dlt.resource(
    name="badges",
    primary_key="badge_id",
    write_disposition="merge",
)
def badges():
    yield from fetch_resource("badges")


@dlt.source
def stack_exchange_source():
    yield users()
    yield questions()
    yield answers()
    yield comments()
    yield tags()
    yield badges()


def load_stackexchange():
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_stackexchange",
        destination="duckdb",
        dataset_name="raw_stackexchange",
    )

    load_info = pipeline.run(stack_exchange_source())
    print(load_info)

# def get_stack_exchange():
#     return load_stackexchange()


if __name__ == "__main__":
    load_stackexchange()