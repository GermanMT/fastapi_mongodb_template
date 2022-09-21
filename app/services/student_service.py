from bson import ObjectId

from app.services.db.database import student_collection


async def create_student(student_data: dict) -> dict:
    student = student_collection.insert_one(student_data)
    new_student = student_collection.find_one({'_id': student.inserted_id})
    return new_student

async def read_student(student_id: str) -> dict:
    student = student_collection.find_one({'_id': ObjectId(student_id)})
    return student

async def update_student(student_id: str, data: dict) -> bool:
    if len(data) < 1:
        return False
    student = student_collection.find_one({'_id': ObjectId(student_id)})
    if student:
        updated_student = student_collection.update_one({'_id': ObjectId(student_id)}, {'$set': data})
        if updated_student:
            return True
        return False
    return False

async def delete_student(student_id: str) -> bool:
    student_collection.delete_one({'_id': ObjectId(student_id)})