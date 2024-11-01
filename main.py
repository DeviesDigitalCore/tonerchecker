import logging
import os
import dotenv
import glob


def configure():
    logging.basicConfig(level=logging.DEBUG)
    for env_file in glob.glob(".env*"):
        dotenv.load_dotenv(env_file)


configure()

slack_url = os.getenv("SLACK_URL")
assert slack_url is not None, "SLACK_URL not configured"

logging.debug(f"Using {slack_url}")
