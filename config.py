from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BG_IMAGE = getenv("BG_IMAGE")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", "LCFRHC-RMFNVM-UYPIRF-XJDZTV-ARQ")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "MutualanVibes")
OWNER = getenv("OWNER", "raflyskuy")

BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/2a7533f21bf36924560ea.jpg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . , - : ; !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
