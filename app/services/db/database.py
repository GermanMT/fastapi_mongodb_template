from motor.motor_asyncio import AsyncIOMotorClient

from app.config import settings


client = AsyncIOMotorClient(settings.DATABASE_URL)

db = client.students

student_collection = db.get_collection('students')