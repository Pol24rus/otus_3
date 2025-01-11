import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Сhrome(executable_path='C:\\PycharmProjects\\otus_3\\chromedriver.exe')  # это в случае если
# вебдрайвер не в path а в проекте

# driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# но тогда надо
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(3)
driver.close()
