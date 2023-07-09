from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from app.router import api_router
from app.services.populate_service import students_bulkwrite

DESCRIPTION = '''
A simple template for python projects using FastAPI and MongoDB

## Documentation

Related documentation and links about this template.

[FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python

[Pydantic](https://pydantic-docs.helpmanual.io/): Data validation library for Python.

[Motor](https://motor.readthedocs.io/en/stable/): Asynchronous Python driver for MongoDB.
'''

app = FastAPI(
    title="FastAPI/MongoDB Template",
    description=DESCRIPTION,
    version="1.4.0",
    contact={
        "name": "Antonio Germán Márquez Trujillo",
        "url": "https://github.com/GermanMT",
        "email": "amtrujillo@us.es",
    }
)


@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)


@app.on_event("startup")
async def startup_event() -> None:
    await students_bulkwrite()


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(api_router)