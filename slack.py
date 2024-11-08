import requests

from config import Config


def post_to_slack(message, config: Config):
    requests.post(config.slack_url, json={"text": message})
