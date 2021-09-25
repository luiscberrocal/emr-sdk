import os
from pathlib import Path

import slack
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env/.slack'

load_dotenv(dotenv_path=env_path)


def send_message():
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    client.chat_postMessage(channel="#emr-consulting", text="Bot message")


if __name__ == '__main__':
    send_message()
