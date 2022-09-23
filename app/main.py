from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ValidationError

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.router import api_router

from app.utils.json_encoder import JSONEncoder

from json import loads

description = '''
A simple template for python projects using FastAPI and MongoDB

## Documentation

[FastAPI](https://fastapi.tiangolo.com/)

[Pydantic](https://pydantic-docs.helpmanual.io/)
'''

app = FastAPI(
    title = "FastAPI/MongoDB Template",
    description = description,
    version = "1.0.0",
    contact = {
        "name": "Antonio Germán Márquez Trujillo",
        "url": "https://github.com/GermanMT",
        "email": "amtrujillo@us.es",
    }
)

@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(_ , exc):
    exc_json = loads(exc.json())
    response = {'message': []}
    for error in exc_json:
        response['message'].append(error['loc'][-1]+f": {error['msg']}")
    
    return JSONResponse(content = JSONEncoder().encode(response), status_code = 422)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins = [],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(api_router)