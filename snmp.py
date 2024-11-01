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

        out = _map_output(result)
        outputs.append(out)

    return outputs


def _get_toner_level(ip, color):
    arguments = [f"-H", ip, "-t", "consumable", "-o", color]

    script_path = "check_snmp_printer"
    result = subprocess.run(
        ["bash", script_path] + arguments, capture_output=True, text=True
    )
    return result


def _map_output(text):
    logging.info(text)
    return text
