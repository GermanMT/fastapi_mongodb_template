from json import load

from app.services.db.database import get_collection


async def students_bulkwrite() -> None:
    student_collection = get_collection('students')
    file = open('app/services/db/db_files/students.json', encoding='utf-8')
    students = load(file)
    await student_collection.insert_many(students)
