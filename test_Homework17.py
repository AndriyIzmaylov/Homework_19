import requests
import pytest


status_ok = 200
status_created = 201
status_deleted = 204
status_already_exists = 400
var_for_update = "ragnarjok"
url = 'https://www.aqa.science/users/'


@pytest.fixture
def credentials():
   return ('admin', 'admin123')


# добавить в json после чего тут вытаскивать из файла
@pytest.fixture
def getpayload():
    return {
        "username": "igorek",
        "email": "aaaaa@abc.com"
    }


@pytest.fixture
def user_create_helper(getpayload, credentials):
    print("setup")
    response = requests.post(url, auth=credentials, data=getpayload)
    while response.status_code != status_created:
        getpayload["username"] = getpayload["username"] + "1"
        response = requests.post(url, auth=credentials, data=getpayload)
    yield response
    user_id = response.json()["url"]
    requests.delete(user_id, auth=credentials)
    print("teardown")


def test_create(user_create_helper, credentials):
    response = user_create_helper
    assert status_created == response.status_code
    user_id = response.json()["url"]


def test_read(user_create_helper, credentials):
    response = user_create_helper
    user_id = response.json()["url"]
    assert requests.get(user_id, auth=credentials).status_code == status_ok


def test_update(user_create_helper, credentials):
    response = user_create_helper
    user_id = response.json()["url"]
    update_user = requests.put(user_id, auth=credentials, data={
        "username": var_for_update, "email": "aaaaa@abc.com"})
    assert update_user.status_code == status_ok
    assert update_user.json()["username"] == var_for_update


def test_delete(getpayload, credentials):
    response = requests.post(url, auth=credentials, data=getpayload)
    while response.status_code != status_created:
        getpayload["username"] = getpayload["username"] + "1"
        response = requests.post(url, auth=credentials, data=getpayload)
    user_id = response.json()["url"]
    assert requests.delete(user_id, auth=credentials).status_code == status_deleted