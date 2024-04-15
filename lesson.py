import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.chrome(executable_path='C:\\PycharmProjects\\otus_3\\chromedriver.exe')  # это в случае если
# вебдрайвер не в path а в проекте
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys("secret_sauce")
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()

time.sleep(5)
driver.close()


