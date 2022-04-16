import os


SLACK_ASYNC_ALERT_CLI_PATH = f"{os.getenv('HOME')}/.slack_async_alert/bin"
CONFIGURE_PATH = f"{os.getenv('HOME')}/.slack_async_alert/credentials.json"
CONFIGURE_PATH = os.getenv("CONFIGURE_PATH", CONFIGURE_PATH)

CONFIGURE_QUESTIONS = [
    {
        "type": "input",
        "name": "slack_key",
        "message": "What's your slack key?",
    },
    {
        "type": "input",
        "name": "user_id",
        "message": "What's your slack user id?",
    },
    {
        "type": "input",
        "name": "hardware_identifier",
        "message": "Is there any identifier when you receive from this server/computer?",
    },
]
