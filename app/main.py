from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
    unhandled_exception_handler,
)
from app.middleware import log_request_middleware
from app.router import api_router
from app.services import students_bulkwrite

DESCRIPTION = """
A simple template for python projects using FastAPI and MongoDB

## Documentation

Related documentation and links about this template.

[FastAPI](https://fastapi.tiangolo.com/): Modern web framework for building APIs with Python.

[Pydantic](https://pydantic-docs.helpmanual.io/): Data validation library for Python.

[Motor](https://motor.readthedocs.io/en/stable/): Asynchronous Python driver for MongoDB.
"""

@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    await students_bulkwrite()
    yield

app = FastAPI(
    title="FastAPI/MongoDB Template",
    description=DESCRIPTION,
    version="1.5.0",
    contact={
        "name": "Antonio Germán Márquez Trujillo",
        "url": "https://github.com/GermanMT",
        "email": "amtrujillo@us.es",
    },
    license_info={
        "name": "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
    lifespan=lifespan,
)


app.middleware("http")(log_request_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


app.include_router(api_router)
