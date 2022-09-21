from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.models.student_model import StudentModel

from app.services.student_service import (
    read_student,
    create_student,
    update_student,
    delete_student
)

from app.utils.json_encoder import JSONEncoder


router = APIRouter()

@router.post('/student', response_description = 'Create student', response_model = StudentModel)
async def create_student_data(student: StudentModel = Body(...)):
    student_json = jsonable_encoder(student)
    try:
        new_student = await create_student(student_json)
        return JSONResponse(status_code = status.HTTP_201_CREATED, content = JSONEncoder().encode(new_student))
    except:
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': f'The student cannot be created'})

@router.get('/student/{student_id}', response_description = 'Read student', response_model = StudentModel)
async def read_student_data(student_id: str):
    try:
        student = await read_student(student_id)
        return JSONResponse(status_code = status.HTTP_200_OK, content = JSONEncoder().encode(student))
    except:
        return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content = {'message': f'Student with id {student_id} not found'})

@router.put('/student/{student_id}', response_description = 'Update student', response_model = dict[str, str])
async def update_student_data(student_id: str, student: StudentModel = Body(...)):
    student_json = jsonable_encoder(student)
    try:
        await update_student(student_id, student_json)
        return JSONResponse(status_code = status.HTTP_200_OK, content = {'message': f'Student with id {student_id} updated successfully'})
    except: 
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': 'There was an error updating the student data'})

@router.delete('/student/{student_id}', response_description = 'Delete student', response_model = dict[str, str])
async def delete_student_data(student_id: str):
    try:
        await delete_student(student_id)
        return JSONResponse(status_code = status.HTTP_200_OK, content = {'message': f'Student with id {student_id} deleted successfully'})
    except:
        return JSONResponse(status_code = status.HTTP_400_BAD_REQUEST, content = {'message': f'Student with id {student_id} doesn\'t exist'})