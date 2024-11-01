import logging
import os

import requests


def post_to_slack(message):
    post_to_slack = os.getenv("SLACK_POST", False)
    if post_to_slack:
        _post_to_slack(message)
    else:
        logging.info("Would post to slack but is configured not to.")


def _post_to_slack(message):
    slack_url = os.getenv("SLACK_URL")
    assert slack_url is not None, "SLACK_URL not configured"

    requests.post(slack_url, json={"text": message})
