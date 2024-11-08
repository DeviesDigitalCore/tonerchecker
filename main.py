import logging

from config import ConfigLoader
from slack import post_to_slack
from snmp import TonerStatus, check_toner_status


def configure():
    logging.basicConfig(level=logging.WARNING)

    try:
        config_loader = ConfigLoader()
        config = config_loader.get_config()
        logging.info(f"Using config {config}")
        return config
    except ValueError as e:
        logging.error(f"Configuration error: {e}")
        raise


def levels_to_message(levels: list[TonerStatus]):
    message = "The follow toner levels are low:"
    for level in levels:
        message += f"\n{level.consumable}: {level.level}%"

    return message


config = configure()


statuses = check_toner_status(config)
low_statuses = [s for s in statuses if s.level <= config.low_level]

if any(low_statuses):
    message = levels_to_message(low_statuses)
    post_to_slack(message, config)
