import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""тест тройной, проверка неверных логина и пароля, отсутствие перехода на нужную страницу. В закрытом режиме"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=g)
# driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

login_negative_user = "standard_use"
password_negative = "secret_sau"

"""Тест на негативный логин"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_negative_user)
# но можно не вводить доп переменную, а стереть символ с помощью селениум, например
# user_name.send_keys(Keys.BACKSPACE)
print("Input wrong login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

"""Проверка на негативный логин"""
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("Good negative test by login")

"""Проверка на url"""
url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print("Current url - ", get_url)
assert get_url != url
print("Good test for negative url")

"""Сброс введенных данных"""
# driver.get(base_url)  # работает, но правильно ниже.
driver.refresh()

"""Тест на негативный пароль"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_negative)
print("Input wrong Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()

"""Проверка на негативный пароль"""
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("Good negative test by pass_word")

"""проверка на кликабельность элемента (крестика) об ошибке. """
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print('Click Error-Button')
print("value_warring_test - ", value_warring_test)
# Проверю тем, что после клика не будет текста на странице. Но элемента уже нет на странице, поэтому его не найти. и
# значит не проверить
# assert value_warring_test != "Epic sadface: Username and password do not match any user in this service"
