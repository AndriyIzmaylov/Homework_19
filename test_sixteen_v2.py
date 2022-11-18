import pytest
from selenium.webdriver.common.by import By


def test_create(login_logout_system, check_create_user, cred_file):
    assert check_create_user == "HTTP 201 Created"
    user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    pytest.driver.get(user_id_after_create)
    user_name_after_creating = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
    assert user_name_after_creating == f'"{cred_file["new_user_name"]}"'


def test_read(login_logout_system, check_create_user, cred_file):
    user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    pytest.driver.get(user_id_after_create)
    user_status_for_read = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
    assert user_status_for_read == "HTTP 200 OK"



def test_update (login_logout_system, check_create_user, cred_file):
    user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    pytest.driver.get(user_id_after_create)
    new_user_name_for_update = pytest.driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[1]/div/input')
    new_user_name_for_update.clear()
    new_user_name_for_update.send_keys(cred_file["updated_name"])
    put_button = pytest.driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
    put_button.click()
    pytest.driver.get(user_id_after_create)
    user_upd = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
    assert user_upd == f'"{cred_file["updated_name"]}"'


def test_delete(login_logout_system, check_create_user, cred_file):
    user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    pytest.driver.get(user_id_after_create)
    status_by_xpath_after_delete = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span/b[1]').text
    assert status_by_xpath_after_delete == 'HTTP 200 OK'

