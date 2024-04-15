import time
from selenium import webdriver


# driver = webdriver.chrome(executable_path='C:\\PycharmProjects\\otus_3\\chromedriver.exe')  # это в случае если
# вебдрайвер не в path а в проекте
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(5)
driver.close()


