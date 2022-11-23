from fastapi import APIRouter

from app.controllers import student_controller


api_router = APIRouter()
api_router.include_router(student_controller.router, tags=['student'])