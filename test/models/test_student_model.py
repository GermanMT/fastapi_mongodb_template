import mongomock


def test_insert_user():
    student = {
        'name': 'John',
        'surname': 'Doe',
        'age': 24,
        'phone': '678340253'
    }

    client = mongomock.MongoClient()
    db = client.get_database('TestStudentDB')
    collection = db.get_collection('Students')

    result = collection.insert_one(student)

    new_student = collection.find_one({'_id': result.inserted_id})

    assert new_student['_id']
    assert new_student['name'] == student['name']
    assert new_student['surname'] == student['surname']
    assert new_student['age'] == student['age']
    assert new_student['phone'] == student['phone']