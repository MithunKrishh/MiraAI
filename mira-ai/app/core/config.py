import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "MiraAI")
    VERSION: str = os.getenv("VERSION", "1.0.0")

    # MongoDB settings
    MONGODB_URI: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    MONGODB_DB: str = os.getenv("MONGODB_DB", "miraai")
    MONGODB_COLLECTION: str = os.getenv("MONGODB_COLLECTION", "memory")

settings = Settings()