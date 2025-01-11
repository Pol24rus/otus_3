from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
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

header = driver.find_element(By.XPATH, "//span[@class='title']")
print(header.text)