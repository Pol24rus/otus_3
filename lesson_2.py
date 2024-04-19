"""Решение проблемы с закрытием Google Chrome """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()  # создаем экземпляр класса ChromeOptions
options.add_experimental_option("detach", True)  # добавляем опцию "detach", чтобы браузер не закрывался после
# завершения сеанса тестирования.
g = Service()  # создаем экземпляр класса Service, который представляет собой фоновый процесс драйвера Chrome. Этот
# процесс будет работать в фоновом режиме и управлять браузером.
driver = webdriver.Chrome(options=options, service=g)  # создаем экземпляр класса WebDriver, который представляет
# собой драйвер для управления браузером. В параметре options мы передаем опции, которые мы создали в первых двух
#  строках кода, а в параметре service мы передаем экземпляр класса Service
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# user_name = driver.find_element_by_id("user-name")
# user_name = driver.find_element(By.ID,"user-name")  # ID
# user_name = driver.find_element(By.NAME,"user-name")  #NAME
# user_name = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")  #full XPATH
# user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")  # ID XPATH
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")  # * - поиск по всем тэгам
"""кастомный x-path"""
user_name = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']")
user_name = driver.find_element(By.XPATH, "//input[@name='user-name']")
"""поиск по индексу"""
user_name = driver.find_element(By.XPATH, '(//div[@class="form_group"])[1]')
# - локатор для элемента с class="form_group" номер один на странице", если их два или больше

user_name.send_keys("test")
