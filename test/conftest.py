import pytest

import mongomock

from bson import ObjectId


@pytest.fixture()
def mongo_mock(monkeypatch):
    client = mongomock.MongoClient()
    db = client.get_database('TestStudentDB')
    collection = db.get_collection('Students')

    student_data = {
        '_id': ObjectId('6329cd902186c0e6c5fa5eef'),
        'name': 'Myke',
        'surname': 'Fernandez',
        'age': 38,
        'phone': '+34 678 340 253'
    }

    collection.insert_one(student_data)

    monkeypatch.setattr('app.services.student_service.student_collection', collection)