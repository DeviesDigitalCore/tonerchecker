# Tonerchecker

Ever been the one to order toner for the printer when it’s running low? Now, __everyone__ asks you when it’s about to run out...

Introducing **Tonerchecker**! With Tonerchecker, you can automatically send a Slack message when the toner reaches a critical level.

Docker image available at: [deviesdevelopment/tonerchecker on Docker Hub](https://hub.docker.com/repository/docker/deviesdevelopment/tonerchecker)


## Usage

### Running the Official Docker Image

To run the script using the latest official Docker image:

```bash
docker run deviesdevelopment/tonerchecker --slack-url {YOUR_SLACK_URL} --printer-ip {YOUR_PRINTER_IP}
```

### Running with Python

To run directly with Python:

```
usage: main.py [-h] --slack-url SLACK_URL --printer-ip PRINTER_IP [--low-level LOW_LEVEL]

Configuration for application

options:
  -h, --help            show this help message and exit
  --slack-url SLACK_URL
                        Slack Webhook URL (required)
  --printer-ip PRINTER_IP
                        Printer IP address (required)
  --low-level LOW_LEVEL
                        Low level threshold (default: 10)
```

## Development

This project works by running a shell script through Python, formatting the output, and posting it to a designated Slack channel. You can run the Python script directly via [main.py](main.py).

### Docker

To build and push a new Docker image, run the following commands:

```
docker build -t deviesdevelopment/tonerchecker .
docker push deviesdevelopment/tonerchecker
```

## Feature Requests:

- Add support for custom Slack messages