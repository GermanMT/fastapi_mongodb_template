from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'fastapi_mongodb_template',
    version = '1.2.0',
    author = 'Antonio Germán Márquez Trujillo',
    author_email = 'amtrujillo@us.es',
    description = 'Template using FastAPI and MongoDB',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/GermanMT/fastapi_mongodb_template',
    classifiers = [
        'Programming Language :: Python :: 3.10'
    ],
    python_requires = '>=3.10',
    install_requires = [
        'wheel==0.38.4',
        'fastapi[all]==0.88.0',
        'motor==3.1.1',
        'python-dotenv==0.21.0',
        'requests==2.28.1'
    ],
    tests_require=[
        'pytest==7.2.0',
        'pytest-asyncio==0.20.3',
        'mongomock-motor==0.0.13',
        'prospector[with_everything]==1.8.3',
        'mypy==0.991',
        'motor-stubs==1.7.1',
        'types-requests==2.28.11.2',
        'types-setuptools==65.6.0.2'
    ]
)