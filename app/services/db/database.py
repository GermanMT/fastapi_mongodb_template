from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.config import settings

@lru_cache
def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(settings.DB_URI)
    match collection_name:
        case 'students':
            return client.students.get_collection('students')
        case _:
            raise Exception('Is not a valid collection of the database!')
