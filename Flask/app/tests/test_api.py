import requests

from tests.config import API_URL


def test_root():
    response = requests.get(API_URL)
    assert response.status_code == 200
    assert response.json() == dict(status='REST ADS', )


def test_get_user(create_user):
    new_user = create_user
    response = requests.get(API_URL + '/users/' + str(new_user["id"]))
    assert response.status_code == 200
    assert response.json() == {
        "id": new_user["id"],
        "email": new_user["email"],
        "registration_time": new_user["registration_time"].isoformat(),
        }


def test_get_notexisting_user():
    response = requests.get(API_URL + '/users/9999999')

    assert response.status_code == 404
    assert response.json() == {"status": "error", "description": "user not found"}

# Дальше писать тесты не было времени модуль тестов примерно понятен))))

