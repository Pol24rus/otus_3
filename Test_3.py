"""тест на неправильный логин и пароль, неправильными делаем их удаляя последние символы"""
import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()

driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
time.sleep(3)
user_name.send_keys(Keys.BACKSPACE)  # удаляю символ из логина
print("Input wrong login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_all)
# print("Input Password")
pass_word.send_keys(Keys.RETURN)  # клик Enter, можно Enter но лучше RETURN
# print("Press ENTER")
time.sleep(1)
"""Проверка на негативный логин"""
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("Good negative test by login")

driver.refresh()  # обновим страницу

"""Тест на негативный пароль"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
# print("Input login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_all)
pass_word.send_keys(Keys.BACKSPACE)
print("Input wrong Password")
time.sleep(1)
pass_word.send_keys(Keys.RETURN)

"""Проверка на негативный пароль"""
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test = warring_text.text
assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
print("Good negative test by pass_word")

driver.refresh()

"""Позитивный сценарий"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
# print("Input login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_all)
# print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
# print("Input login button")

"""в фильтре меняю строку выпадающего меню"""
filter_button = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
filter_button.send_keys(Keys.RETURN)
filter_button.send_keys(Keys.DOWN)
time.sleep(1)
filter_button.send_keys(Keys.RETURN)
print("Изменен фильтр")

"""Ввод даты"""
now_date = (datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S"))
print(now_date)
name_screenshot = 'screenshot' + now_date + '.png'
print(name_screenshot)
# driver.save_screenshot(f"./users/poladko.dv/изображения/)
driver.save_screenshot('name_screenshot')
print("сделан скрин")
# driver.save_screenshot('2024_05_21.png')  # делает скриншот