import logging
import os
from snmp import TonerStatus, check_toner_status
import dotenv
import glob
from slack import post_to_slack


def configure():
    logging.basicConfig(level=logging.DEBUG)
    for env_file in glob.glob(".env*"):
        dotenv.load_dotenv(env_file)


def levels_to_message(levels: list[TonerStatus]):
    message = "The follow toner levels are low:"
    for level in levels:
        message += f"\n{level.color}: {level.level}%"

    return message


low_level = int(os.getenv("LOW_LEVEL", 0))

configure()

statuses = check_toner_status()
low_statuses = [s for s in statuses if s.level <= low_level]

if any(low_statuses):
    message = levels_to_message(low_statuses)
    post_to_slack(message)
