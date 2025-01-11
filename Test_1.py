from selenium import webdriver
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
print("Input login")
pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
pass_word.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Input login button")
"""проверка по наличию на открывшейся странице уникального слова, например Products"""
# check_word = driver.find_element(By.XPATH, "//span[@class='title']")  #находим на открывшейся странице "Products"
# value_check_word = check_word.text  #считали текст в найденном локаторе
# print(value_check_word)  # проверим для себя что мы нашли
# assert value_check_word == "Products"
# print("Good")

"""проверка по открывшемуся УРЛу"""
url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)
assert get_url == url
print("Good url")
