# FastAPI and MongoDB Template

[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/germanmt/fastapi_mongodb_template?label=dockerhub&logo=docker&sort=semver)](https://hub.docker.com/repository/docker/germanmt/fastapi_mongodb_template) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GermanMT/fastapi_mongodb_template?color=green&logo=github)](https://github.com/GermanMT/fastapi_mongodb_template/releases)

## Documentation

Related documentation and links about this template.

[FastAPI](https://fastapi.tiangolo.com/)

[Pydantic](https://pydantic-docs.helpmanual.io/)

[Motor](https://motor.readthedocs.io/en/stable/): Asynchronous Python driver for MongoDB

## Deployment with docker

1. Create a .env file from template.env

2. Run command 'docker compose up --build'

3. Enter [here](http://0.0.0.0:8000/docs)

## Testing

1. Create a virtual enviroment with command 'python3 -m venv tutorial-env' and python 3.10

2. Execute the enviroment with command 'source tutorial-env/bin/activate'

3. Install production requirements with command 'pip install -r requirements.txt'

4. Install develop requirements with command 'pip install -r requirements_dev.txt'

5. Run tests with command 'pytest test/'

## Analyse code

You can analyse your code best practices after install develop requirements with commands 'mypy app' and 'prospector' in the root folder of the project.
