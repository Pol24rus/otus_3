"""Тест кейс 9 - Опрос"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime
from a_user import *

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()  # чтобы браузер не закрывался
    driver = webdriver.Chrome(options=options, service=g)
    wait = WebDriverWait(driver, 10, poll_frequency=1)  # ожидание 10 сек с частотой проверки 1 сек)
    driver.get(link)
    input_txt = datetime.now().replace(microsecond=0)  # текст в поле, будет каждый раз разный


    class Auth():
        def __init__(self, login, password):
            self.login = login
            self.password = password
            print(self.login)
            print(self.password)

        def autorisation_1(self):  # авторизация
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
            user_profile = driver.find_element(By.ID,
                                               "user-block")  # можно и сюда нажать, профиль откроется если кнопка перекрыта
            user_profile.click()
            exit_btn = driver.find_element(By.XPATH, "//a[@class='system-auth-form__item-link-all']")
            exit_btn.click()


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


        def adding_user(self):  # НАжимаю Добавить работников
            add_user = driver.find_element(By.XPATH,
                                           "//*[@id='entity-selector-oPostFormLHE_blogPostForm']/div/div/div[1]/span/span")
            add_user.click()
            time.sleep(1)
            # добавляю получателей
            element_input = driver.find_element(By.XPATH, "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
            element_input.send_keys(user_2)  # Кобякова вместо меня из-за авторизации
            time.sleep(1)
            element_input.send_keys(Keys.ENTER)
            time.sleep(1)
            element_input.send_keys(user_3)
            time.sleep(1)
            element_input.send_keys(Keys.ENTER)
            time.sleep(1)
            element_input.send_keys(user_4)  # добавить Соболева?
            time.sleep(1)
            element_input.send_keys(Keys.ENTER)
            element_input.send_keys(Keys.ESCAPE)  # убираю выпадающий список сотрудников


        # adding_user()
        def question_form(self):  # нахожу Вопрос
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

        """поменять местами 123 и 127
        не голосует у Кобяковой"""
        def vote_users(self):  # Голосование у выбранных сотрудников
            print("self.login - ", self.login)
            if self.login == login_3: # or login_3:
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

    auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
    auth_1.autorisation_1()
    vote_1 = Vote(login_2)
    vote_1.opros()
    vote_1.opros2()
    vote_1.adding_user()
    vote_1.question_form()
    vote_1.vote_users()
    auth_1.profile_exit()

    auth_2 = Auth(login_3, pass_3)
    auth_2.autorisation_1()
    vote_2 = Vote(login_3)
    # vote_2.opros()
    vote_2.vote_users()
    auth_2.profile_exit()

    auth_3 = Auth(login_4, pass_4)
    auth_3.autorisation_1()
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
    # find_user_1 = driver.find_element(By.XPATH, "//div[@class='popup-window --open']/div/span/span/a/span[@class='bx-ilike-popup-name-new']")
    # ТО же, только короче
    find_user_1 = driver.find_element(By.XPATH,
                                      "//div[@class='popup-window --open']//span[@class='bx-ilike-popup-name-new']")
    find_user_1_txt = find_user_1.text  # находит ФИО 'Соболев Иван'
    print("find_user_1.text - ", find_user_1.text)
    # print("find_user_1 - ", find_user_1_txt)  # результат одинаковый
    vote_res_1.send_keys(Keys.ESCAPE)

    # нахожу вторую кнопку
    vote_res_2 = driver.find_element(By.XPATH,
                                     "//div[@class='bx-vote-container bx-vote-container-web']/form//tr[2]/td[2]/span/a")
    vote_res_2.click()
    time.sleep(1)
    find_user_2 = driver.find_element(By.XPATH,
                                      "//div[@class='popup-window --open']/div/span/span/a[1]/*[@class='bx-ilike-popup-name-new']")
    find_user_2_txt = find_user_2.text  # находит ФИО 'Кобякова Елена'
    print("find_user_2.text - ", find_user_2_txt)
    # time.sleep(2)
    find_user_3 = driver.find_element(By.XPATH,
                                      "//div[@class='popup-window --open']/div/span/span/a[2]/*[@class='bx-ilike-popup-name-new']")
    find_user_3_txt = find_user_3.text  # находит ФИО 'ОТдел кадров'
    print("find_user_3.text - ", find_user_3_txt)
    # time.sleep(2)
    driver.refresh()
    needed_user_1 = 'Соболев Иван'
    needed_user_2 = 'Кобякова Елена'
    needed_user_3 = 'Отдел Кадров'
    assert find_user_1_txt == needed_user_1
    assert find_user_2_txt == needed_user_2
    assert find_user_3_txt == needed_user_3

    # self.assertEqual(needed_text, actual_text, "Не тот текст")
    # print("ТК_9 опрос")

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла
