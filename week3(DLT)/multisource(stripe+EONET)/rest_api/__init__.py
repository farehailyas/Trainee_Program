import dlt
import requests


@dlt.resource
def top_story_ids():
    print("Fetching stories ids")
    ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()

    for story_id in ids:
        yield {"id": story_id}


@dlt.resource
def stories():
    print("Fetching stories..")
    ids = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json"
    ).json()
    count = 0
    for story_id in ids:

        data = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        ).json()
        print("inside loop" , count)
        count+=1 
        yield data