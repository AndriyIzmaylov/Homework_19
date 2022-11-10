from selenium import webdriver
from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
new_user_name = "rando"
new_user_email = "aa@aa.com"
updated_name = "ololo"

login = "admin"
password = "admin123"


def click_delete_on_user_page():
    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="deleteModal"]/div/div/div[2]/form/button').submit()


def login_into_the_system():
    driver.get("https://www.aqa.science/api-auth/login/?next=/")
    login_field = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]')
    login_field.send_keys(login)
    password_field.send_keys(password)
    login_button.click()


def test_create():
    login_into_the_system()
    driver.get("https://www.aqa.science/users")
    userName_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
    userEmail_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
    createUserButton = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
    userName_field.send_keys(new_user_name)
    userEmail_field.send_keys(new_user_email)
    createUserButton.click()
    status_by_xpath_from_response = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
    assert status_by_xpath_from_response == "HTTP 201 Created"
    user_id_after_create = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    driver.get(user_id_after_create)
    user_name_after_creating = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
    assert user_name_after_creating == f'"{new_user_name}"'
    click_delete_on_user_page()
    driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")


def test_read():
    login_into_the_system()
    driver.get("https://www.aqa.science/users")
    userName_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
    userEmail_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
    createUserButton = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
    userName_field.send_keys(new_user_name)
    userEmail_field.send_keys(new_user_email)
    createUserButton.click()
    user_id_after_create = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    driver.get(user_id_after_create)
    user_status_for_read = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/b[1]').text
    assert user_status_for_read == "HTTP 200 OK"
    click_delete_on_user_page()
    driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")


def test_update ():
    login_into_the_system()
    driver.get("https://www.aqa.science/users")
    userName_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
    userEmail_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
    createUserButton = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
    userName_field.send_keys(new_user_name)
    userEmail_field.send_keys(new_user_email)
    createUserButton.click()
    user_id_after_create = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    driver.get(user_id_after_create)
    new_user_name_for_update = driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[1]/div/input')
    new_user_name_for_update.clear()
    new_user_name_for_update.send_keys(updated_name)
    put_button = driver.find_element(By.XPATH, '//*[@id="put-object-form"]/form/fieldset/div[4]/button')
    put_button.click()
    driver.get(user_id_after_create)
    user_upd = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[14]').text
    assert user_upd == f'"{updated_name}"'
    click_delete_on_user_page()
    driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")

def test_delete():
    login_into_the_system()
    driver.get("https://www.aqa.science/users")
    userName_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[1]/div/input')
    userEmail_field = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[2]/div/input')
    createUserButton = driver.find_element(By.XPATH, '//*[@id="post-object-form"]/form/fieldset/div[4]/button')
    userName_field.send_keys(new_user_name)
    userEmail_field.send_keys(new_user_email)
    createUserButton.click()
    user_id_after_create = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span[1]/span[3]/a').text
    driver.get(user_id_after_create)
    click_delete_on_user_page()
    status_by_xpath_after_delete = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[4]/pre/span/b[1]').text
    assert status_by_xpath_after_delete == 'HTTP 200 OK'
    driver.get("https://www.aqa.science/api-auth/logout/?next=/users/")


def test_close():
    driver.close()

