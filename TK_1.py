from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import unittest
from a_user import *
import time

link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys(login_4)  # Кобякова
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys(pass_4)
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    #time.sleep(1)

    # size = ()

    input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner").size
    # нахожу размер, должен быть как needed_input, то есть ноль. а правильный как valid_input
    print(input1)
    valid_input = {'height': 24, 'width': 496}  # в этом случае assert input1 != valid_input
    needed_input = {'height': 0, 'width': 0}
    # assert input1 != valid_input
    assert input1 == needed_input
    print("ТК_1 (невозможность отправки сообщения в ленту) пройден")


    """ assertNotIn(элемент, список). Проверяет, что элемент не входит в список.
    То есть проверить, можно ли найти input1 на link """

finally:
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    driver.quit()
