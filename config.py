import argparse
import glob
import os
import re
from dataclasses import dataclass

import dotenv
import logging


@dataclass
class Config:
    slack_url: str
    printer_ip: str
    low_level: int

    def __post_init__(self):
        # Validate slack_url format
        slack_url_pattern = re.compile(
            r"^https://hooks\.slack\.com/services/[A-Za-z0-9_/-]+$"
        )
        if not slack_url_pattern.match(self.slack_url):
            raise ValueError("`slack_url` must be a valid Slack Webhook URL.")

        # Validate printer_ip format
        ip_pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if not ip_pattern.match(self.printer_ip):
            raise ValueError("`printer_ip` must be a valid IP address.")

        # Validate low_level range
        if not (0 <= self.low_level <= 100):
            raise ValueError("`low_level` must be between 0 and 100.")


class ConfigLoader:

    def __init__(self):
        # Parse arguments
        self.args = self.parse_arguments()

        # Initialize Config with parsed arguments to enforce type-safety and validation
        self.config = Config(
            slack_url=self.args.slack_url,
            printer_ip=self.args.printer_ip,
            low_level=self.args.low_level,
        )

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Configuration for application")

        parser.add_argument(
            "--slack-url",
            required=True,
            help="Slack Webhook URL (required)",
        )

        parser.add_argument(
            "--printer-ip",
            required=True,
            help="Printer IP address (required)",
        )

        parser.add_argument(
            "--low-level",
            type=int,
            default=10,
            help="Low level threshold (default: 10)",
        )

        return parser.parse_args()

    def get_config(self) -> Config:
        return self.config

    def __str__(self):
        return (
            f"Slack URL: {self.config.slack_url}, Printer IP: {self.config.printer_ip}, "
            f"Low Level: {self.config.low_level}"
        )
