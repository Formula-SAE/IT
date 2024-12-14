import os
from dotenv import load_dotenv, find_dotenv

token: str = ""
isTesting: str = ""


def LoadConfigs() -> None:
    """Load configs from env file"""

    load_dotenv(find_dotenv())

    global token, isTesting

    token = os.environ.get("BOT_TOKEN")
    isTesting = os.environ.get("IS_TESTING")

    return None


def get_token() -> str: return token

def get_is_testing() -> str: return isTesting
