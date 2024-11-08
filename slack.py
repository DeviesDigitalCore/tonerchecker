import os

import requests


def post_to_slack(message):
    slack_url = os.getenv("SLACK_URL")
    assert slack_url is not None, "SLACK_URL not configured"

    requests.post(slack_url, json={"text": message})
