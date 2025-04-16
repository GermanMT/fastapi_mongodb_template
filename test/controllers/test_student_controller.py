from json import dumps
from typing import Any

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_create_student_ok(mongo_mock: Any) -> None:
    student_data = {
        "name": "John",
        "surname": "Doe",
        "age": 24,
        "phone": "619 527 721"
    }

    response = client.post(
        "/student",
        json=student_data
    )

    assert response.status_code == 201
    inserted_student = response.json()
    assert inserted_student["name"] == student_data["name"]
    assert inserted_student["surname"] == student_data["surname"]
    assert inserted_student["age"] == student_data["age"]
    assert inserted_student["phone"] == student_data["phone"]


@pytest.mark.asyncio
async def test_create_student_empty_name_surname(mongo_mock: Any) -> None:
    student_data = {
        "name": "",
        "surname": "",
        "age": 24,
        "phone": "619 527 721"
    }

    response = client.post(
        "/student",
        json=student_data
    )

    assert response.status_code == 422
    error = response.json()
    assert error["detail"][0]["loc"][1] == "name"
    assert error["detail"][0]["msg"] == "String should have at least 1 character"
    assert error["detail"][1]["loc"][1] == "surname"
    assert error["detail"][1]["msg"] == "String should have at least 1 character"


@pytest.mark.asyncio
@pytest.mark.parametrize("age", (1, 50, 100))
async def test_create_student_ok_age(mongo_mock: Any, age: int) -> None:
    student_data = {
        "name": "John",
        "surname": "Doe",
        "age": age,
        "phone": "619 527 721"
    }

    response = client.post(
        "/student",
        json=student_data
    )

    assert response.status_code == 201
    inserted_student = response.json()
    assert inserted_student["name"] == student_data["name"]
    assert inserted_student["surname"] == student_data["surname"]
    assert inserted_student["age"] == student_data["age"]
    assert inserted_student["phone"] == student_data["phone"]


@pytest.mark.asyncio
@pytest.mark.parametrize("age", (-50, -1, 0))
async def test_create_student_bad_age(mongo_mock: Any, age: int) -> None:
    student_data = {
        "name": "John",
        "surname": "Doe",
        "age": age,
        "phone": "619 527 721"
    }

    response = client.post(
        "/student",
        json=student_data
    )

    assert response.status_code == 422
    error = response.json()
    print(error)
    assert error["detail"][0]["loc"][1] == "age"
    assert error["detail"][0]["msg"] == "Input should be greater than 0"


@pytest.mark.asyncio
async def test_create_student_bad_phone(mongo_mock: Any) -> None:
    student_data = {
        "name": "John",
        "surname": "Doe",
        "age": 24,
        "phone": "619 asd 721"
    }

    response = client.post(
        "/student",
        json=student_data
    )

    assert response.status_code == 422
    error = response.json()
    assert error["detail"][0]["loc"][1] == "phone"
    assert error["detail"][0]["msg"] == "Value error, The phone 619 asd 721 is not correct"


@pytest.mark.asyncio
async def test_read_student(mongo_mock: Any) -> None:
    response = client.get("/student/6329cd902186c0e6c5fa5eef")
    assert response.status_code == 200
    readed_student = response.json()
    assert readed_student["name"] == "Myke"
    assert readed_student["surname"] == "Fernandez"
    assert readed_student["age"] == 38
    assert readed_student["phone"] == "678 340 253"


@pytest.mark.asyncio
async def test_read_student_not_found(mongo_mock: Any) -> None:
    response = client.get("/student/632c2636db39c267a803f1ed")
    assert response.status_code == 404
    error = response.json()
    assert error["detail"][0] == "Student with id 632c2636db39c267a803f1ed not found"


@pytest.mark.asyncio
async def test_update_student(mongo_mock: Any) -> None:
    updated_student_data = {
        "name": "Myke",
        "surname": "Fernandez",
        "age": 20,
        "phone": "678 340 253"
    }
    response = client.put("/student/6329cd902186c0e6c5fa5eef", content=dumps(updated_student_data))
    assert response.status_code == 200
    json_response = response.json()
    assert (
        json_response["message"] == "Student with id 6329cd902186c0e6c5fa5eef updated successfully"
    )


@pytest.mark.asyncio
async def test_update_student_not_found(mongo_mock: Any) -> None:
    updated_student_data = {
        "name": "Myke",
        "surname": "Fernandez",
        "age": 20,
        "phone": "678 340 253"
    }
    response = client.put("/student/632c2636db39c267a803f1ed", content=dumps(updated_student_data))
    assert response.status_code == 404
    error = response.json()
    assert error["detail"][0] == "Student with id 632c2636db39c267a803f1ed not found"


@pytest.mark.asyncio
async def test_delete_employee(mongo_mock: Any) -> None:
    response = client.delete("/student/6329cd902186c0e6c5fa5eef")
    assert response.status_code == 200
    json_response = response.json()
    assert (
        json_response["message"] == "Student with id 6329cd902186c0e6c5fa5eef deleted successfully"
    )


@pytest.mark.asyncio
async def test_delete_employee_not_found(mongo_mock: Any) -> None:
    response = client.delete("/student/632c2636db39c267a803f1ed")
    assert response.status_code == 404
    error = response.json()
    assert error["detail"][0] == "Student with id 632c2636db39c267a803f1ed not found"
