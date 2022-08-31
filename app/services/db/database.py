import motor.motor_asyncio

from app.config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)

db = client.depex

student_collection = db.get_collection('students')