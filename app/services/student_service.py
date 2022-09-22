from fastapi import HTTPException

from bson import ObjectId

from app.services.db.database import student_collection


async def create_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({'_id': student.inserted_id})
    return new_student

async def read_student(student_id: str) -> dict:
    student = await student_collection.find_one({'_id': ObjectId(student_id)})
    if student:
        return student
    raise HTTPException(status_code = 404, detail = [f'Student with id {student_id} not found'])

async def update_student(student_id: str, data: dict) -> None:
    student = await student_collection.find_one({'_id': ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code = 404, detail = [f'Student with id {student_id} not found'])
    await student_collection.update_one({'_id': ObjectId(student_id)}, {'$set': data})

async def delete_student(student_id: str) -> None:
    student = await student_collection.find_one({'_id': ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code = 404, detail = [f'Student with id {student_id} not found'])
    await student_collection.delete_one({'_id': ObjectId(student_id)})