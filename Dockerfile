FROM python:3.11

WORKDIR /fastapi_mongodb_template

COPY ./requirements.txt /fastapi_mongodb_template/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./ /fastapi_mongodb_template/

EXPOSE 8000

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000