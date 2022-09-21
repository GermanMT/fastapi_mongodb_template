from json import loads, dumps

from fastapi.testclient import TestClient

from app.main import app

import pytest


client = TestClient(app)

@pytest.mark.asyncio
async def test_create_student(mongo_mock):
    await mongo_mock

    student_data = {
        'name': 'John',
        'surname': 'Doe',
        'age': 24,
        'phone': '+34 619 527 721'
    }

    response = client.post(
        '/student',
        json = student_data
    )

    assert response.status_code == 201
    inserted_student = loads(response.json())
    assert inserted_student['name'] == student_data['name']
    assert inserted_student['surname'] == student_data['surname']
    assert inserted_student['age'] == student_data['age']
    assert inserted_student['phone'] == student_data['phone']

@pytest.mark.asyncio
async def test_read_student(mongo_mock):
    await mongo_mock

    response = client.get('/student/6329cd902186c0e6c5fa5eef')
    assert response.status_code == 200
    readed_student = loads(response.json())
    assert readed_student['name'] == 'Myke'
    assert readed_student['surname'] == 'Fernandez'
    assert readed_student['age'] == 38
    assert readed_student['phone'] == '+34 678 340 253'

@pytest.mark.asyncio
async def test_update_student(mongo_mock):
    await mongo_mock

    updated_student_data = {
        "name": "Myke",
        "surname": "Fernandez",
        "age": 20,
        "phone": "+34 678 340 253"
    }
    response = client.put('/student/6329cd902186c0e6c5fa5eef', data = dumps(updated_student_data))
    assert response.status_code == 200
    assert response.json()['message'] == 'Student with id 6329cd902186c0e6c5fa5eef updated successfully'

@pytest.mark.asyncio
async def test_delete_employee(mongo_mock):
    await mongo_mock

    response = client.delete('/student/6329cd902186c0e6c5fa5eef')
    assert response.status_code == 200
    assert response.json()['message'] == 'Student with id 6329cd902186c0e6c5fa5eef deleted successfully'