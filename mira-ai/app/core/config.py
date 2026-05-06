import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "MiraAI")
    VERSION: str = os.getenv("VERSION", "1.0.0")

settings = Settings()