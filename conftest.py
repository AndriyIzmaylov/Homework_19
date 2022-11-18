import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

project_pass = Path.cwd()
file_pass = project_pass.joinpath("creds.json")

@pytest.fixture()
def cred_file():
    # take admin credentials
    with open(file_pass, "r") as f:
        login_variables = json.load(f)
        return login_variables


@pytest.fixture(scope="session", autouse=True)
def session_class():
    # Open file with data
    with open(file_pass, "r") as f:
        login_variables = json.load(f)


    port = 4488

    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Run Chrome with options
    pytest.driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}/wd/hub',
        options=options
    )

    # open url
    pytest.driver.get(login_variables["endpoint"])
    yield
    # Post-conditions
    time.sleep(3)
    pytest.driver.close()

@pytest.fixture()
def login_into_the_system(cred_file):
    pytest.driver.get("https://www.aqa.science/api-auth/login/?next=/")
    login_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_username"]')
    password_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_password"]')
    login_button = pytest.driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]')
    login_field.send_keys(cred_file["admin_login"])
    password_field.send_keys(cred_file["admin_password"])
    login_button.click()
    yield
    pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/button').click()
    pytest.driver.find_element(By.XPATH, '//*[@id="deleteModal"]/div/div/div[2]/form/button').submit()
    pytest.driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")

