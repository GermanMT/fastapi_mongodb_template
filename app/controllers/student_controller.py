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
    try:
        new_student = await create_student(student_json)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=json_encoder(new_student)
        )
    except HTTPException as error:
        return JSONResponse(
            status_code=error.status_code,
            content=json_encoder({'message': error.detail}))


@router.get(
    '/student/{student_id}',
    response_description='Read student',
    response_model=StudentModel
)
async def read_student_data(student_id: str) -> JSONResponse:
    try:
        student = await read_student(student_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json_encoder(student)
        )
    except HTTPException as error:
        return JSONResponse(
            status_code=error.status_code,
            content=json_encoder({'message': error.detail})
        )


@router.put(
    '/student/{student_id}',
    response_description='Update student',
    response_model=dict[str, str]
)
async def update_student_data(student_id: str, student: StudentModel) -> JSONResponse:
    student_json = jsonable_encoder(student)
    try:
        await update_student(student_id, student_json)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json_encoder(
                {'message': f'Student with id {student_id} updated successfully'}
            )
        )
    except HTTPException as error:
        return JSONResponse(
            status_code=error.status_code,
            content=json_encoder({'message': error.detail})
        )


@router.delete(
    '/student/{student_id}',
    response_description='Delete student',
    response_model=dict[str, str]
)
async def delete_student_data(student_id: str) -> JSONResponse:
    try:
        await delete_student(student_id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=json_encoder(
                {'message': f'Student with id {student_id} deleted successfully'}
            )
        )
    except HTTPException as error:
        return JSONResponse(
            status_code=error.status_code,
            content=json_encoder({'message': error.detail})
        )