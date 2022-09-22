from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ValidationError

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.router import api_router

from json import loads

app = FastAPI()

@app.exception_handler(RequestValidationError)
@app.exception_handler(ValidationError)
async def validation_exception_handler(_ , exc):
    exc_json = loads(exc.json())
    response = {'message': []}
    for error in exc_json:
        response['message'].append(error['loc'][-1]+f": {error['msg']}")
    
    return JSONResponse(response, status_code = 422)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins = [],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

app.include_router(api_router)