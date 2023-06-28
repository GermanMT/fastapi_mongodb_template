from json import loads

from fastapi import FastAPI, Request, __version__
from fastapi.exceptions import RequestValidationError, ValidationError

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.router import api_router

from app.services.populate_service import students_bulkwrite

from app.utils.json_encoder import json_encoder

DESCRIPTION = '''
A simple template for python projects using FastAPI and MongoDB

## Documentation

Related documentation and links about this template.

[FastAPI](https://fastapi.tiangolo.com/)

[Pydantic](https://pydantic-docs.helpmanual.io/)

[Motor](https://motor.readthedocs.io/en/stable/): Asynchronous Python driver for MongoDB
'''

app = FastAPI(
    title="FastAPI/MongoDB Template",
    description=DESCRIPTION,
    version="1.0.0",
    contact={
        "name": "Antonio Germán Márquez Trujillo",
        "url": "https://github.com/GermanMT",
        "email": "amtrujillo@us.es",
    }
)


@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(
    _: Request,
    exc: ValidationError | RequestValidationError
) -> JSONResponse:
    exc_json = loads(exc.json())
    response: dict[str, list[str]] = {'message': []}
    for error in exc_json:
        response['message'].append(error['loc'][-1] + f": {error['msg']}")

    return JSONResponse(content=json_encoder(response), status_code=422)


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