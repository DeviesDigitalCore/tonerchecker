import logging
import os

import requests


def post_to_slack():
    post_to_slack = os.getenv("SLACK_POST", False)
    if post_to_slack:
        _post_to_slack()
    else:
        logging.info("Would post to slack but is configured not to.")


def _post_to_slack():
    slack_url = os.getenv("SLACK_URL")
    assert slack_url is not None, "SLACK_URL not configured"

    logging.debug(f"Using {slack_url}")

    requests.post(slack_url, json={"text": "Hello, world."})
