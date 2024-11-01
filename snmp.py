import logging
import os


def check_toner_status():

    printer_ip = os.getenv("PRINTER_IP")

    assert printer_ip is not None, "PRINTER_IP not configured."
    logging.info(f"Using printer IP {printer_ip}")
