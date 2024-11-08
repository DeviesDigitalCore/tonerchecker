import logging
import os
import subprocess
from dataclasses import dataclass

from config import Config


def check_toner_status(config: Config):

    outputs = []
    for consumable in [
        "black",
        "cyan",
        "magenta",
        "yellow",
        "drum",
    ]:
        result = _get_toner_level(config.printer_ip, consumable)
        try:
            out = _map_output(result, consumable)
            outputs.append(out)
        except Exception:
            logging.warn(f"Could not get status for consumable {consumable}")

    return outputs


def _get_toner_level(ip, consumable):
    arguments = [f"-H", ip, "-t", "consumable", "-o", consumable]

    script_path = "check_snmp_printer"
    result = subprocess.run(
        ["bash", script_path] + arguments, capture_output=True, text=True
    )
    return result.stdout


def _map_output(text: str, consumable):
    level = text.split("%")[0].split(" ")[-1].strip()

    try:
        level_value = int(level)
    except Exception as e:
        logging.warn(
            f"Could not parse {level} as an integer. Full text: {text.strip()}"
        )
        raise e

    return TonerStatus(consumable=consumable, level=100 - level_value)


@dataclass
class TonerStatus:
    consumable: str
    level: int
