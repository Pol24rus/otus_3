from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import unittest
from a_user import *

input_txt = datetime.now().replace(microsecond=0)  #переменная, вставляю в текст, чтобы текст был разный
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()  # чтобы браузер не закрывался
driver = webdriver.Chrome(options=options, service=g)
driver.get(link)
driver.maximize_window()


# определение самого длинного логина. потом передавать в поле user_login для удаления предыдущего логина
# user_log = [login_2, login_3, login_4]
# print(user_log)
# print(type(user_log))
# max_lenght = len(max(user_log, key=len))
# print(max_lenght)


class Auth():

    def __init__(self, login, password):
        self.login = login
        self.password = password
        # print(self.login)
        # print(self.password)

    def autorisation_1(self):  # авторизация, использую класс Auth, импортировал из b-classes
        max_lenght = len(max(user_login,
                             key=len))  # определяю, сколько символов максимального логина затереть в строке ввода логина
        # login_lenght = len(self.login)
        # print(login_lenght)
        login_field = driver.find_element(By.ID, "USER_LOGIN")
        login_field.send_keys(
            Keys.BACKSPACE * max_lenght)  # после выхода из УЗ остается в строке логин, поэтому сначала стираю его
        login_field.send_keys(self.login)
        password_field = driver.find_element(By.ID, "USER_PASSWORD")
        password_field.send_keys(self.password)
        button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
        button1.click()
        time.sleep(1)

    def profile_exit(self):  # выход из УЗ
        # можно и сюда нажать, профиль откроется если кнопка перекрыта
        user_profile = driver.find_element(By.ID, "user-block")
        user_profile.click()
        exit_btn = driver.find_element(By.XPATH, "//a[@class='system-auth-form__item-link-all']")
        exit_btn.click()


class Users_add():  # ввод пользователей в поля выбора польз.

    def __init__(self, sotrudnik_1, sotrudnik_2, value_1, value_2): #, sotrudnik, value):
        # не указываю в классе, тк сотрудников может быть от 1 до 3
        # пользователи те, кого я ввожу в соотв кейсе, а не те что в файле a_user
        self.sotrudnik_1 = None
        self.sotrudnik_2 = None
        self.sotrudnik_3 = None
        self.value_1 = None  # значение локатора
        self.value_2 = None  # возможно присвоение значения сразу, а не в ТК
        # self.element = None
        # self.element = driver.find_element(By.XPATH, self.value)  # это будет element

    def adding_user_1(self, sotrudnik_1, value_1, value_2):  # Добавление 1 работника
        self.sotrudnik_1 = sotrudnik_1
        self.value_1 = value_1  # локатор на Добавить работников
        self.value_2 = value_2  # локатор на поле ввода работников
        # нахожу Кому (добавить работников)
        # value_1
        # add_user = driver.find_element(By.XPATH, "//*[@id='entity-selector-oPostFormLHE_blogPostForm']/div/div/div[1]/span/span")
        add_user = driver.find_element(By.XPATH, self.value_1)
        add_user.click()
        time.sleep(1)
        # value_2
        # element_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")))
        element_input = driver.find_element(By.XPATH, self.value_2)
        element_input.send_keys(self.sotrudnik_1)  # Кобякова вместо меня из-за авторизации
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys(Keys.ESCAPE)  # убираю выпадающий список сотрудников

    def adding_user_2(self, sotrudnik_1, sotrudnik_2, value_1, value_2):  # добавление 2-х сотрудников
        self.sotrudnik_1 = sotrudnik_1
        self.sotrudnik_2 = sotrudnik_2
        self.value_1 = value_1  # локатор на Добавить работников
        self.value_2 = value_2  # локатор на поле ввода работников

        add_user = driver.find_element(By.XPATH, self.value_1)
        add_user.click()
        time.sleep(1)
        element_input = driver.find_element(By.XPATH, self.value_2)
        element_input.send_keys(self.sotrudnik_1)  # Кобякова вместо меня из-за авторизации
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys(self.sotrudnik_2)
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        element_input.send_keys(Keys.ESCAPE)  # убираю выпадающий список сотрудников

    def adding_user_3(self, sotrudnik_1, sotrudnik_2, sotrudnik_3, value_1, value_2):
        # Добавление 3-х сотрудников
        self.sotrudnik_1 = sotrudnik_1
        self.sotrudnik_2 = sotrudnik_2
        self.sotrudnik_3 = sotrudnik_3
        self.value_1 = value_1  # локатор на Добавить работников
        self.value_2 = value_2  # локатор на поле ввода работников

        add_user = driver.find_element(By.XPATH, self.value_1)
        add_user.click()
        time.sleep(1)
        element_input = driver.find_element(By.XPATH, self.value_2)
        element_input.send_keys(self.sotrudnik_1)  # Кобякова вместо меня из-за авторизации
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys(self.sotrudnik_2)
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys(self.sotrudnik_3)  # добавить Соболева?
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        element_input.send_keys(Keys.ESCAPE)  # убираю выпадающий список сотрудников


class Vote():
    def __init__(self, login):
        self.login = login

    def opros(self):  # нахожу "Опрос"
        driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-vote']").click()
        time.sleep(2)

    def opros2(self):
        # открываю фрейм, пишу текст
        iframe9: WebElement = driver.find_element(By.CSS_SELECTOR,
                                                  "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm > iframe")
        driver.switch_to.frame(iframe9)
        task_txt = driver.find_element(By.TAG_NAME, "body")
        task_txt.send_keys("Автоматизированный опрос от ", str(input_txt))
        driver.switch_to.default_content()
        time.sleep(2)

    # opros()

    def question_form(self):  # нахожу Вопрос в форме опроса
        question_field = driver.find_element(By.XPATH, "//input[@placeholder='Вопрос ']")
        # //input[@placeholder='Вопрос ']
        # question_field = driver.find_element(By.XPATH, "//div[@class='feed-add-vote-wrap']/div/ol/li/div/input[@type='text']")
        question_field.click()
        question_field.send_keys("Test " + str(input_txt))
        # нахожу Ответ
        answer_field_1 = driver.find_element(By.XPATH, "//input[@placeholder='Ответ  1']")
        answer_field_1.click()
        answer_field_1.send_keys("Ответ 1 - Да")
        answer_field_2 = driver.find_element(By.XPATH, "//input[@placeholder='Ответ  2']")
        answer_field_2.click()
        answer_field_2.send_keys("Ответ 2 - Нет")
        # Нахожу Отправить
        send_keys = driver.find_element(By.ID, "blog-submit-button-save")
        send_keys.click()
        time.sleep(3)

    # question_form()

    def vote_users(self):  # Голосование у выбранных сотрудников
        # print("self.login - ", self.login)
        if self.login == login_3:  # or login_3:
            answer_1 = driver.find_element(By.XPATH,
                                           "//table[@class='bx-vote-answer-list']/tbody/tr//span[@class='bx-vote-block-inp-substitute']")
            answer_1.click()
        else:
            answer_2 = driver.find_element(By.XPATH,
                                           "//table[@class='bx-vote-answer-list']/tbody/tr[2]//span[@class='bx-vote-block-inp-substitute']")
            answer_2.click()
        vote_btn = driver.find_element(By.XPATH,
                                       "//button[@data-bx-vote-button='actVoting']")  # //button[@class='ui-btn ui-btn-lg ui-btn-primary']
        vote_btn.click()


class TestAbs(unittest.TestCase):
    # Авторизация. беру из класса Auth
    # auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
    # auth_1.autorisation_1()

    # try:
    def test_abs09(self):  # опрос
        auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
        auth_1.autorisation_1()

        vote_1 = Vote(login_2)
        vote_1.opros()  # нахожу опрос
        time.sleep(2)
        vote_1.opros2()  # фрейм
        time.sleep(2)

        # add_user = driver.find_element(By.XPATH,
        #                                "//*[@id='entity-selector-oPostFormLHE_blogPostForm']/div/div/div[1]/span/span")
        # add_user.click()
        time.sleep(1)
        # вынес сюда определение поля, куда вводятся сотрудники, тк в класс нельзя, в каждом кейсе поле своё

        # добавляю пользователей и локатор в класс
        add_user = Users_add(None, None, None, None)  # определяю сотрудника и локатор
        # в ф-цию adding_user_1 определяю 1-го сотрудника ОК, и 2 локатора
        add_user.adding_user_3(user_2, user_3, user_4, "//*[@id='entity-selector-oPostFormLHE_blogPostForm']/div/div/div[1]/span/span", "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        time.sleep(2)
        vote_1.question_form()
        time.sleep(2)
        vote_1.vote_users()
        time.sleep(2)
        auth_1.profile_exit()

        auth_2 = Auth(login_3, pass_3)  # Соболев
        auth_2.autorisation_1()
        vote_2 = Vote(login_3)
        # vote_2.opros()
        vote_2.vote_users()
        auth_2.profile_exit()

        auth_3 = Auth(login_4, pass_4)  # Кобякова
        auth_3.autorisation_1()
        # Вставить ТК_1. Можно отдельной ф-цией, но тогда нужна отдельная авторизация
        input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner").size
        vote_3 = Vote(login_4)
        # vote_3.opros()
        vote_3.vote_users()
        auth_3.profile_exit()

        # Проверка
        auth_1 = Auth(login_2, pass_2)  # авторизуюсь под кадрами
        auth_1.autorisation_1()

        # надо найти сначала кнопку, то есть цифру в ответах, потом искать Соболева
        vote_res_1 = driver.find_element(By.XPATH,
                                         "//div[@class='bx-vote-container bx-vote-container-web']/form//tr/td[2]/span/a")
        vote_res_1.click()
        time.sleep(1)
        # нахожу Соболева в 1-м ответе
        find_user_1 = driver.find_element(By.XPATH,
                                          "//div[@class='popup-window --open']//span[@class='bx-ilike-popup-name-new']")
        find_user_1_2 = find_user_1.text  # находит ФИО 'Соболев Иван'
        # print("find_user_1.text - ", find_user_1.text)
        # print("find_user_1 - ", find_user_1_txt)  # результат одинаковый
        vote_res_1.send_keys(Keys.ESCAPE)

        # нахожу вторую кнопку
        vote_res_2 = driver.find_element(By.XPATH,
                                         "//div[@class='bx-vote-container bx-vote-container-web']/form//tr[2]/td[2]/span/a")
        vote_res_2.click()
        time.sleep(1)
        find_user_2 = driver.find_element(By.XPATH,
                                          "//div[@class='popup-window --open']/div/span/span/a[1]/*[@class='bx-ilike-popup-name-new']")
        find_user_2_2 = find_user_2.text  # находит ФИО 'Кобякова Елена'
        # time.sleep(2)
        find_user_3 = driver.find_element(By.XPATH,
                                          "//div[@class='popup-window --open']/div/span/span/a[2]/*[@class='bx-ilike-popup-name-new']")
        find_user_3_2 = find_user_3.text  # находит ФИО 'ОТдел кадров'
        # time.sleep(2)
        driver.refresh()
        needed_user_1 = user_3  # Соболев Иван
        needed_user_2 = user_4  # 'Кобякова Елена'
        needed_user_3 = user_2  # 'Отдел Кадров'
        needed_input = {'height': 0, 'width': 0}  # проверка к ТК_1
        self.assertEqual(find_user_1_2, needed_user_1, "Не соответствует Соболев")
        self.assertEqual(find_user_2_2, needed_user_2, "Не соответствует Кобякова")
        self.assertEqual(find_user_3_2, needed_user_3, "Не соответствует ОК")
        self.assertDictEqual(input1, needed_input, "Нет отсутствия возможности отправить сообщение простым пользователем")
        print("ТК_9 Создать опрос пройден")
        print("ТК_1 Невозможность отправки сообщения в ленте Кобяковой - пройден")

        # finally:
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        driver.quit()
        # не забываем оставить пустую строку в конце файла
