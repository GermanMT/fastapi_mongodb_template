from typing import Any

import pytest
from bson import ObjectId
from mongomock_motor import AsyncMongoMockClient


@pytest.fixture()
async def mongo_mock(monkeypatch: Any) -> None:
    client = AsyncMongoMockClient()
    database = client.get_database('TestStudentDB')
    collection = database.get_collection('students')

    student_data: dict[str, Any] = {
        '_id': ObjectId('6329cd902186c0e6c5fa5eef'),
        'name': 'Myke',
        'surname': 'Fernandez',
        'age': 38,
        'phone': '678 340 253'
    }

    await collection.insert_one(student_data)

    monkeypatch.setattr('app.services.student_service.student_collection', collection)
