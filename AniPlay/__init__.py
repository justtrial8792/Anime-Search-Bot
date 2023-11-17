import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "25222859")),
    api_hash= os.environ.get("API_HASH", "b76d4fb1f5afc4a797b85c5e34b0f1ca"),
    bot_token= os.environ.get("TOKEN", "6458225530:AAFhj-q7M-EdXi9UcB2r7tcq6vCTVSrE2cQ")
)
