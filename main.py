import logging
from snmp import check_toner_status
import dotenv
import glob
from slack import post_to_slack


def configure():
    logging.basicConfig(level=logging.DEBUG)
    for env_file in glob.glob(".env*"):
        dotenv.load_dotenv(env_file)


configure()

check_toner_status()
post_to_slack()
