"""Тест кейс 9 - Опрос"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime
from a_user import *


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()  # чтобы браузер не закрывался
driver = webdriver.Chrome(options=options, service=g)
wait = WebDriverWait(driver, 10, poll_frequency=1)  # ожидание 10 сек с частотой проверки 1 сек)
driver.get(link)
input_txt = datetime.now().replace(microsecond=0)  # текст в поле, будет каждый раз разный
# driver.maximize_window()  # раскрываю окно браузера
# options.add_argument('--headless=new')  # скрываю браузер

# user_log = [login_2, login_3, login_4]  # необх чтобы определять длину логина
# user_pass = [pass_2, pass_3, pass_4]

try:

    class Auth():
        def __init__(self, login, password):
            self.login = login
            self.password = password
            print(self.login)
            print(self.password)


        def autorisation_1(self):  # авторизация
            max_lenght = len(max(user_login, key=len))  # определяю, сколько символов максимального логина затереть в строке ввода логина
                # login_lenght = len(self.login)
                # print(login_lenght)
            login_field = driver.find_element(By.ID, "USER_LOGIN")
            login_field.send_keys(Keys.BACKSPACE * max_lenght)  # после выхода из УЗ остается в строке логин, поэтому сначала стираю его
            login_field.send_keys(self.login)
            password_field = driver.find_element(By.ID, "USER_PASSWORD")
            password_field.send_keys(self.password)
            button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
            button1.click()
            time.sleep(1)


        def profile_exit(self):
            user_profile = driver.find_element(By.ID,
                                                   "user-block")  # можно и сюда нажать, профиль откроется если кнопка перекрыта
            user_profile.click()
            exit_btn = driver.find_element(By.XPATH, "//a[@class='system-auth-form__item-link-all']")
            exit_btn.click()


    # profile_exit()
    auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
    auth_1.autorisation_1()
    auth_1.profile_exit()

    # auth_1 = Auth(user_log[0], pass_2)  # вариант определения длины предыдущего логина
    # auth_1.autorisation_1()
    # auth_1.profile_exit()

    auth_2 = Auth(login_3, pass_3)
    auth_2.autorisation_1()
    auth_2.profile_exit()
    # auth_2 = Auth(user_log[1], pass_3)
    # auth_2.autorisation_1()
    # auth_2.profile_exit()

    auth_3 = Auth(login_4, pass_4)
    auth_3.autorisation_1()
    auth_3.profile_exit()
    # auth_3 = Auth(user_log[2], pass_4)
    # auth_3.autorisation_1()
    # auth_3.profile_exit()

    auth_4 = Auth(login_2, pass_2)
    auth_4.autorisation_1()
    auth_4.profile_exit()
    # auth_4 = Auth(user_log[0], pass_2)
    # auth_4.autorisation_1()
    # auth_4.profile_exit()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # driver.quit()
    # не забываем оставить пустую строку в конце файла
