import logging
import os
import dotenv
import glob


def configure():
    logging.basicConfig(level=logging.DEBUG)
    for env_file in glob.glob(".env*"):
        dotenv.load_dotenv(env_file)


def POST_TO_SLACK():
    slack_url = os.getenv("SLACK_URL")
    assert slack_url is not None, "SLACK_URL not configured"

    logging.debug(f"Using {slack_url}")


configure()


post_to_slack = os.getenv("SLACK_POST", False)
if post_to_slack:
    POST_TO_SLACK()
