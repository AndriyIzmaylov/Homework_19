import pytest
from selenium.webdriver.common.by import By


new_user_name = "rando"
new_user_email = "aa@aa.com"
updated_name = "ololo"

# def click_delete_on_user_page():
#     pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/button').click()
#     pytest.driver.find_element(By.XPATH, '//*[@id="deleteModal"]/div/div/div[2]/form/button').submit()

def login_into_the_system(cred_file):
    pytest.driver.get("https://www.aqa.science/api-auth/login/?next=/")
    login_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_username"]')
    password_field = pytest.driver.find_element(By.XPATH, '//*[@id="id_password"]')
    login_button = pytest.driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]')
    login_field.send_keys(cred_file[0])
    password_field.send_keys(cred_file[1])
    login_button.click()




def test_create(cred_file):
    login_into_the_system(cred_file)
    pytest.driver.get("https://www.aqa.science/users")
    userName_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
    userEmail_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
    createUserButton = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
    userName_field.send_keys(new_user_name)
    userEmail_field.send_keys(new_user_email)
    createUserButton.click()
    status_by_xpath_from_response = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
    assert status_by_xpath_from_response == "HTTP 201 Created"
    user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    pytest.driver.get(user_id_after_create)
    user_name_after_creating = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
    assert user_name_after_creating == f'"{new_user_name}"'
    # click_delete_on_user_page()
    pytest.driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")


# def test_read():
#     pytest.driver.get("https://www.aqa.science/users")
#     userName_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
#     userEmail_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
#     createUserButton = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
#     userName_field.send_keys(new_user_name)
#     userEmail_field.send_keys(new_user_email)
#     createUserButton.click()
#     user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
#     pytest.driver.get(user_id_after_create)
#     user_status_for_read = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
#     assert user_status_for_read == "HTTP 200 OK"
#     click_delete_on_user_page()
#     pytest.driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")
#
#
# def test_update ():
#     pytest.driver.get("https://www.aqa.science/users")
#     userName_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
#     userEmail_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
#     createUserButton = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
#     userName_field.send_keys(new_user_name)
#     userEmail_field.send_keys(new_user_email)
#     createUserButton.click()
#     user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
#     pytest.driver.get(user_id_after_create)
#     new_user_name_for_update = pytest.driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[1]/div/input')
#     new_user_name_for_update.clear()
#     new_user_name_for_update.send_keys(updated_name)
#     put_button = pytest.driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
#     put_button.click()
#     pytest.driver.get(user_id_after_create)
#     user_upd = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
#     assert user_upd == f'"{updated_name}"'
#     click_delete_on_user_page()
#     pytest.driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")
#
# def test_delete():
#     pytest.driver.get("https://www.aqa.science/users")
#     userName_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
#     userEmail_field = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
#     createUserButton = pytest.driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
#     userName_field.send_keys(new_user_name)
#     userEmail_field.send_keys(new_user_email)
#     createUserButton.click()
#     user_id_after_create = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
#     pytest.driver.get(user_id_after_create)
#     click_delete_on_user_page()
#     status_by_xpath_after_delete = pytest.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span/b[1]').text
#     assert status_by_xpath_after_delete == 'HTTP 200 OK'
#     pytest.driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")
#
#
# def test_close():
#     pytest.driver.close()

