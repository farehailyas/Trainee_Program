import time
import logging
import requests
import dlt

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logging.getLogger("dlt").setLevel(logging.INFO)
logger = logging.getLogger(__name__)


SORTS = {
    "users": "modified",
    "questions": "activity",
    "answers": "activity",
    "comments": "creation",
    "tags": "popular",
    "badges": "rank",
}

MAX_PAGES = 25


def fetch_resource(endpoint, from_date=None, historical=False):
    page = 1

    while True:
        params = {
            "site": "stackoverflow",
            "sort": SORTS[endpoint],
            "order": "desc",
            "pagesize": 100,
            "page": page,
        }

        # for incremental
        if not historical and from_date is not None:
            params["fromdate"] = int(from_date)

        response = requests.get(
            f"https://api.stackexchange.com/2.3/{endpoint}",
            params=params,
        )

        if response.status_code == 400:
            logger.info(f"{endpoint}: stopping at page {page}")
            break

        response.raise_for_status()

        data = response.json()

        yield from data["items"]

        if "backoff" in data:
            logger.info(f"{endpoint}: sleeping {data['backoff']} seconds...")
            time.sleep(data["backoff"])

        if not data.get("has_more", False):
            break

        if page >= MAX_PAGES:
            logger.info(f"{endpoint}: reached anonymous page limit.")
            break

        page += 1


@dlt.resource(
    name="users",
    primary_key="user_id",
    write_disposition="merge",
)
def users(
    historical=False,
    creation_date=dlt.sources.incremental(
        "creation_date",
        initial_value=0,
    ),
):
    yield from fetch_resource(
        "users",
        from_date=creation_date.last_value,
        historical=historical,
    )


@dlt.resource(
    name="questions",
    primary_key="question_id",
    write_disposition="merge",
)
def questions(
    historical=False,
    last_activity=dlt.sources.incremental(
        "last_activity_date",
        initial_value=0,
    ),
):
    yield from fetch_resource(
        "questions",
        from_date=last_activity.last_value,
        historical=historical,
    )


@dlt.resource(
    name="answers",
    primary_key="answer_id",
    write_disposition="merge",
)
def answers(
    historical=False,
    last_activity=dlt.sources.incremental(
        "last_activity_date",
        initial_value=0,
    ),
):
    yield from fetch_resource(
        "answers",
        from_date=last_activity.last_value,
        historical=historical,
    )


@dlt.resource(
    name="comments",
    primary_key="comment_id",
    write_disposition="merge",
)
def comments(
    historical=False,
    last_creation=dlt.sources.incremental(
        "creation_date",
        initial_value=0,
    ),
):
    yield from fetch_resource(
        "comments",
        from_date=last_creation.last_value,
        historical=historical,
    )


@dlt.resource(
    name="tags",
    primary_key="name",
    write_disposition="merge",
)
def tags(historical=False):
    yield from fetch_resource(
        "tags",
        historical=historical,
    )


@dlt.resource(
    name="badges",
    primary_key="badge_id",
    write_disposition="merge",
)
def badges(historical=False):
    yield from fetch_resource(
        "badges",
        historical=historical,
    )


@dlt.source
def stack_exchange_source(load_mode="incremental"):
    historical = load_mode == "historical"

    yield users(historical=historical)
    yield questions(historical=historical)
    yield answers(historical=historical)
    yield comments(historical=historical)
    yield tags(historical=historical)
    yield badges(historical=historical)