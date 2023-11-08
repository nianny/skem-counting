from dotenv import load_dotenv
import os

load_dotenv()
discord_api_token = os.getenv("skem_counting_token")
user_id = os.getenv("user_id")