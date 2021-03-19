import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [349368261]
moderators = [349368261]
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")

channel = os.getenv("CHANNEL")
chat = os.getenv("CHAT")
link_channel = os.getenv("LINK_CHANNEL")
link_chat = os.getenv("LINK_CHAT")
logs_admins_channel = os.getenv("LOGS_ADMIN_CHANNEL")
logs_users_channel = os.getenv("LOGS_USERS_CHANNEL")

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
