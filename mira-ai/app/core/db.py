from pymongo import MongoClient

from app.core.config import settings


_client: MongoClient | None = None


def get_client() -> MongoClient:
    """Return a singleton MongoClient.

    Using a single client instance is recommended by PyMongo.
    """
    global _client
    if _client is None:
        _client = MongoClient(settings.MONGODB_URI)
    return _client


def get_memory_collection():
    db = get_client()[settings.MONGODB_DB]
    return db[settings.MONGODB_COLLECTION]
