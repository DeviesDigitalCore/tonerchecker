import glob
import logging
import os

import dotenv

from slack import post_to_slack
from snmp import TonerStatus, check_toner_status


def configure():
    logging.basicConfig(level=logging.WARNING)
    for env_file in glob.glob(".env*"):
        dotenv.load_dotenv(env_file)


def levels_to_message(levels: list[TonerStatus]):
    message = "The follow toner levels are low:"
    for level in levels:
        message += f"\n{level.consumable}: {level.level}%"

    return message


configure()

low_level_str = os.getenv("LOW_LEVEL")
assert low_level_str is not None, "LOW_LEVEL not configured"
low_level = int(low_level_str)


statuses = check_toner_status()
low_statuses = [s for s in statuses if s.level <= low_level]

if any(low_statuses):
    message = levels_to_message(low_statuses)
    post_to_slack(message)
