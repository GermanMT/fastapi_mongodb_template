from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.models.student_model import StudentModel

from app.services.student_service import (
    read_student,
    create_student,
    update_student,
    delete_student
)

from app.utils.json_encoder import json_encoder


router = APIRouter()


@router.post('/student', response_description='Create student', response_model=StudentModel)
async def create_student_data(student: StudentModel) -> JSONResponse:
    student_json = jsonable_encoder(student)
    if student_json['age'] == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    new_student = await create_student(student_json)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=json_encoder(new_student)
    )


@router.get(
    '/student/{student_id}',
    response_description='Read student',
    response_model=StudentModel
)
async def read_student_data(student_id: str) -> JSONResponse:
    student = await read_student(student_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=json_encoder(student)
    )


@router.put(
    '/student/{student_id}',
    response_description='Update student',
    response_model=dict[str, str]
)
async def update_student_data(student_id: str, student: StudentModel) -> JSONResponse:
    student_json = jsonable_encoder(student)
    await update_student(student_id, student_json)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=json_encoder(
            {'message': f'Student with id {student_id} updated successfully'}
        )
    )


@router.delete(
    '/student/{student_id}',
    response_description='Delete student',
    response_model=dict[str, str]
)
async def delete_student_data(student_id: str) -> JSONResponse:
    await delete_student(student_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=json_encoder(
            {'message': f'Student with id {student_id} deleted successfully'}
        )
    )