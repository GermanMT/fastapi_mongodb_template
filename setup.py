from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'fastapi_mongodb_template',
    version = '1.1.0',
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
        'wheel==0.37.1',
        'fastapi[all]==0.85.0',
        'motor==3.0.0',
        'motor-stubs==1.7.1',
        'python-dotenv==0.21.0',
        'requests==2.28.1',
        'types-requests==2.28.11.2',
        'types-setuptools==65.4.0'
    ],
    tests_require=[
        'pytest==7.1.3',
        'pytest-asyncio==0.19.0',
        'mongomock-motor==0.0.12',
        'prospector[with_everything]==1.7.7',
        'mypy==0.982'
    ]
)