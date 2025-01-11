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
# driver.save_screenshot(f"./users/poladko.dv/изображения/{name_screenshot}")
driver.save_screenshot('users/poladko.dv/изображения/' + name_screenshot)  # не работает указаение папки для сохранения
print("сделан скрин")
# driver.save_screenshot('2024_05_21.png')  # делает скриншот