from json import loads, dumps

from fastapi.testclient import TestClient

import pytest

from app.main import app


client = TestClient(app)


@pytest.mark.asyncio
async def test_create_student_ok(mongo_mock):
    await mongo_mock

    student_data = {
        'name': 'John',
        'surname': 'Doe',
        'age': 24,
        'phone': '619 527 721'
    }

    response = client.post(
        '/student',
        json=student_data
    )

    assert response.status_code == 201
    inserted_student = loads(response.json())
    assert inserted_student['name'] == student_data['name']
    assert inserted_student['surname'] == student_data['surname']
    assert inserted_student['age'] == student_data['age']
    assert inserted_student['phone'] == student_data['phone']


@pytest.mark.asyncio
async def test_create_student_empty_name_surname(mongo_mock):
    await mongo_mock

    student_data = {
        'name': '',
        'surname': '',
        'age': 24,
        'phone': '619 527 721'
    }

    response = client.post(
        '/student',
        json=student_data
    )

    assert response.status_code == 422
    error = loads(response.json())
    assert error['message'][0] == 'name: ensure this value has at least 1 characters'
    assert error['message'][1] == 'surname: ensure this value has at least 1 characters'


@pytest.mark.asyncio
@pytest.mark.parametrize('age', (1, 50, 100))
async def test_create_student_ok_age(mongo_mock, age):
    await mongo_mock

    student_data = {
        'name': 'John',
        'surname': 'Doe',
        'age': age,
        'phone': '619 527 721'
    }

    response = client.post(
        '/student',
        json=student_data
    )

    assert response.status_code == 201
    inserted_student = loads(response.json())
    assert inserted_student['name'] == student_data['name']
    assert inserted_student['surname'] == student_data['surname']
    assert inserted_student['age'] == student_data['age']
    assert inserted_student['phone'] == student_data['phone']


@pytest.mark.asyncio
@pytest.mark.parametrize('age', (-50, -1, 0))
async def test_create_student_bad_age(mongo_mock, age):
    await mongo_mock

    student_data = {
        'name': 'John',
        'surname': 'Doe',
        'age': age,
        'phone': '619 527 721'
    }

    response = client.post(
        '/student',
        json=student_data
    )

    assert response.status_code == 422
    error = loads(response.json())
    assert error['message'][0] == 'age: ensure this value is greater than 0'


@pytest.mark.asyncio
async def test_create_student_bad_phone(mongo_mock):
    await mongo_mock

    student_data = {
        'name': 'John',
        'surname': 'Doe',
        'age': 24,
        'phone': '619 asd 721'
    }

    response = client.post(
        '/student',
        json=student_data
    )

    assert response.status_code == 422
    error = loads(response.json())
    assert error['message'][0] == 'phone: The phone 619 asd 721 is not correct'


@pytest.mark.asyncio
async def test_read_student(mongo_mock):
    await mongo_mock

    response = client.get('/student/6329cd902186c0e6c5fa5eef')
    assert response.status_code == 200
    readed_student = loads(response.json())
    assert readed_student['name'] == 'Myke'
    assert readed_student['surname'] == 'Fernandez'
    assert readed_student['age'] == 38
    assert readed_student['phone'] == '678 340 253'


@pytest.mark.asyncio
async def test_read_student_not_found(mongo_mock):
    await mongo_mock

    response = client.get('/student/632c2636db39c267a803f1ed')
    assert response.status_code == 404
    error = loads(response.json())
    assert error['message'][0] == 'Student with id 632c2636db39c267a803f1ed not found'


@pytest.mark.asyncio
async def test_update_student(mongo_mock):
    await mongo_mock

    updated_student_data = {
        "name": "Myke",
        "surname": "Fernandez",
        "age": 20,
        "phone": "678 340 253"
    }
    response = client.put('/student/6329cd902186c0e6c5fa5eef', data=dumps(updated_student_data))
    assert response.status_code == 200
    response = loads(response.json())
    assert response['message'] == 'Student with id 6329cd902186c0e6c5fa5eef updated successfully'


@pytest.mark.asyncio
async def test_update_student_not_found(mongo_mock):
    await mongo_mock

    updated_student_data = {
        "name": "Myke",
        "surname": "Fernandez",
        "age": 20,
        "phone": "678 340 253"
    }
    response = client.put('/student/632c2636db39c267a803f1ed', data=dumps(updated_student_data))
    assert response.status_code == 404
    error = loads(response.json())
    assert error['message'][0] == 'Student with id 632c2636db39c267a803f1ed not found'


@pytest.mark.asyncio
async def test_delete_employee(mongo_mock):
    await mongo_mock

    response = client.delete('/student/6329cd902186c0e6c5fa5eef')
    assert response.status_code == 200
    response = loads(response.json())
    assert response['message'] == 'Student with id 6329cd902186c0e6c5fa5eef deleted successfully'


@pytest.mark.asyncio
async def test_delete_employee_not_found(mongo_mock):
    await mongo_mock

    response = client.delete('/student/632c2636db39c267a803f1ed')
    assert response.status_code == 404
    error = loads(response.json())
    assert error['message'][0] == 'Student with id 632c2636db39c267a803f1ed not found'