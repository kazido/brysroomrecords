import os

from dotenv import load_dotenv

# Load our environment variables for bot token etc.
load_dotenv()

# Paths
BOT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(BOT_DIR, os.pardir))

# Grab the bot token from the .env file using the load_dotenv function from the dotenv package
TOKEN = os.getenv("BOT_TOKEN")

# Same deal, grab the URI for the MongoDB database
URI = os.getenv("URI")
