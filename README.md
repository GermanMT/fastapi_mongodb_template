# FastAPI and MongoDB Template

## Deployment with docker

1. Create a .env file from template.env

2. Run command 'docker-compose up --build'

3. Enter [here](http://0.0.0.0:8000/docs)

## Testing

1. Create a virtual enviroment with command 'python3 -m venv tutorial-env' and python 3.10

2. Execute the enviroment with command 'source tutorial-env/bin/activate'

3. Install production requirements with command 'pip install -r requirements.txt'

4. Install develop requirements with command 'pip install -r requirements_dev.txt'

5. Run tests with command 'pytest test/'

## Analyse code

You can analyse your code best practices after install develop requirements with commands 'mypy app' and 'prospector' in the root folder of the project.