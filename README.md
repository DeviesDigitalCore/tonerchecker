# Tonerchecker

Ever been the one to order toner for the printer when it’s running low? Now, __everyone__ asks you when it’s about to run out...

Introducing Tonerchecker! With Tonerchecker, you can automatically send a Slack message when the toner reaches a critical level.

Docker image available at: [deviesdevelopment/tonerchecker on Docker Hub](https://hub.docker.com/repository/docker/deviesdevelopment/tonerchecker)

## Development

This project works by running a shell script through Python, with the output formatted and posted to a designated Slack channel.

If you start the application without any environment variables set, it will log the required variables. A list of all possible environment variables can be found in the [.env file](.env).

To get the application up and running, use:
```bash
docker compose up --build
```

Alternatively, you can run the Python script directly: [main.py](main.py).

## Requested Features:

- Add support for custom Slack messages.
