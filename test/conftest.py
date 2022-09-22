import pytest

from mongomock_motor import AsyncMongoMockClient

from bson import ObjectId

from app.models.student_model import StudentModel


@pytest.fixture()
async def mongo_mock(monkeypatch):
    client = AsyncMongoMockClient()
    db = client.get_database('TestStudentDB')
    collection = db.get_collection('students')

    student_data: StudentModel = {
        '_id': ObjectId('6329cd902186c0e6c5fa5eef'),
        'name': 'Myke',
        'surname': 'Fernandez',
        'age': 38,
        'phone': '678 340 253'
    }

    await collection.insert_one(student_data)

    monkeypatch.setattr('app.services.student_service.student_collection', collection)