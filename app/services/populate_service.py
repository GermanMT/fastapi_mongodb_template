from app.services.db.database import student_collection

from json import load


async def students_bulkwrite() -> None:
    file = open('app/services/db/db_files/students.json', encoding = 'utf-8')
    students = load(file)
    await student_collection.insert_many(students)