import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7283682714:AAFnVmikIg2mgnmw7Vjze3bfM-Ew6wb8bMk")
    API_ID = int(os.getenv("API_ID", "21218274"))
    API_HASH = os.getenv("API_HASH", "3474a18b61897c672d315fb330edb213")
    DB_URI = os.getenv("DB_URI", "sqlite:///bot.db")

    # MongoDB Settings
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb+srv://sufyan532011:5042@auctionbot.5ms20.mongodb.net/?retryWrites=true&w=majority&appName=AuctionBot"
    )
    DB_NAME = os.getenv("DB_NAME", "auctionbot")