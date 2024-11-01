from dataclasses import dataclass
import logging
import os
import subprocess


def check_toner_status():

    printer_ip = os.getenv("PRINTER_IP")

    assert printer_ip is not None, "PRINTER_IP not configured."
    logging.info(f"Using printer IP {printer_ip}")

    outputs = []
    for color in [
        "black",
        "cyan",
        "magenta",
        "yellow",
        "drum",
    ]:
        result = _get_toner_level(printer_ip, color)
        try:
            out = _map_output(result, color)
            outputs.append(out)
        except Exception:
            logging.warn(f"Could not get status for color {color}")

    return outputs


def _get_toner_level(ip, color):
    arguments = [f"-H", ip, "-t", "consumable", "-o", color]

    script_path = "check_snmp_printer"
    result = subprocess.run(
        ["bash", script_path] + arguments, capture_output=True, text=True
    )
    return result.stdout


def _map_output(text: str, color):
    level = text.split("%")[0].split(" ")[-1]

    try:
        level_value = int(level)
    except Exception as e:
        logging.warn(f"Could not parse {level} as an integer. Full text: {text}")
        raise e

    return TonerStatus(color=color, level=100 - level_value)


@dataclass
class TonerStatus:
    color: str
    level: int
