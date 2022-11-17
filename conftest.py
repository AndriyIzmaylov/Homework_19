import pytest
import json
import os
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
        admin_name = login_variables["admin_login"]
        admin_password = login_variables["admin_password"]
        return admin_name, admin_password

@pytest.fixture(scope="session", autouse=True)
def sesion_class():
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



# @pytest.fixture(scope="function", autouse=True)
# def login_logout_func(request):
#     # Login as admin
#     username = pytest.driver.find_element(By.XPATH, LoginPage.username_id)
#     password = pytest.driver.find_element(By.XPATH, LoginPage.pswd_id)
#     btn = pytest.driver.find_element(By.XPATH, LoginPage.submit_btn)
#
#     username.send_keys(pytest.secret_variables["adm_name"])
#     password.send_keys(pytest.secret_variables["adm_password"])
#     btn.click()
#
#     # variable needed for determine only failed tests
#     failed_before = request.session.testsfailed
#
#     yield
#     # if test failed add screenshot to allure report
#     if request.session.testsfailed != failed_before:
#         allure.attach(pytest.driver.get_screenshot_as_png(), name="Screen_for_failed",
#                       attachment_type=AttachmentType.PNG)
#         time.sleep(3)
#
#     # logout
#     logout = pytest.driver.find_element(By.XPATH, AdminPage.logout_id)
#     logout.click()
#     time.sleep(2)
#     log_again = pytest.driver.find_element(By.XPATH, AdminPage.log_again_id)
#     log_again.click()

# @pytest.fixture(scope="function", autouse=True)
# def login_into_the_system():
#     pytest.driver.get("https://www.aqa.science/api-auth/login/?next=/")
#     login_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_username"]')
#     password_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_password"]')
#     login_button = pytest.driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]')
#     login_field.send_keys(pytest.creds.admin_login)
#     password_field.send_keys(pytest.creds.admin_password)
#     login_button.click()


