"""Тест включает ТКейсы №№ 1 (невозможно отправить сообщение не админу) 2 (сообщ. 2-м),3 (важное),
4 (Сообщение всем откл в связи с большим кол-вом писем на почту),
5 (редактировать сообщ), 6(сообщ одному), 7 (создать задачу), 8 (Событие календаря); 9 (Опрос);
10(Благодарность), 14 (добавить пользователя в коммент), 15 (добавить ссылку в коммент)"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from datetime import datetime
import unittest
from a_user import *

input_txt = datetime.now().replace(microsecond=0)  #переменная, вставляю в текст, чтобы текст был разный
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()  # чтобы браузер не закрывался
driver = webdriver.Chrome(options=options, service=g)
driver.get(link)
driver.maximize_window()
# options.add_argument('--headless=new')  # скрываю браузер


# авторизация
class Auth():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def autorisation_1(self):  # авторизация, использую класс Auth
        # определяю, сколько символов максимального логина затереть в строке ввода логина
        max_lenght = len(max(user_login, key=len))
        # login_lenght = len(self.login)
        login_field = driver.find_element(By.ID, "USER_LOGIN")
        # после выхода из УЗ остается в строке логин, поэтому сначала стираю его
        login_field.send_keys(Keys.BACKSPACE * max_lenght)
        login_field.send_keys(self.login)
        password_field = driver.find_element(By.ID, "USER_PASSWORD")
        password_field.send_keys(self.password)
        button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
        button1.click()
        time.sleep(1)

    def profile_exit(self):  # выход из УЗ
        user_profile = driver.find_element(By.ID, "user-block")
        user_profile.click()
        exit_btn = driver.find_element(By.XPATH, "//a[@class='system-auth-form__item-link-all']")
        exit_btn.click()


class UsersAdd():  # ввод пользователей в поля выбора польз.
    def __init__(self, sotrudnik_1, sotrudnik_2, value_1, value_2):  # , sotrudnik, value):
        # не указываю в классе, тк сотрудников может быть от 1 до 3. Указываю в конкретной функции
        # пользователи те, кого я ввожу в соотв кейсе, а не те что в файле a_user
        self.sotrudnik_1 = None
        self.sotrudnik_2 = None
        self.sotrudnik_3 = None
        self.value_1 = None  # значение локатора
        self.value_2 = None  # возможно присвоение значения сразу, а не в ТК. Если значение одинаково для всех проверяемых
        # self.element = None
        # self.element = driver.find_element(By.XPATH, self.value)  # это будет element

    def adding_user_1(self, sotrudnik_1, value_1, value_2):  # Добавление 1 работника
        self.sotrudnik_1 = sotrudnik_1
        self.value_1 = value_1  # локатор на Добавить работников
        self.value_2 = value_2  # локатор на поле ввода работников
        # нахожу Кому (добавить работников)
        add_user = driver.find_element(By.XPATH, self.value_1)
        add_user.click()
        time.sleep(2)
        # value_2
        # element_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")))
        element_input = driver.find_element(By.XPATH, self.value_2)
        element_input.send_keys(self.sotrudnik_1)  #
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(2)
        element_input.send_keys(Keys.ESCAPE)  # убираю выпадающий список сотрудников

    def adding_user_2(self, sotrudnik_1, sotrudnik_2, value_1, value_2):  # добавление 2-х сотрудников
        self.sotrudnik_1 = sotrudnik_1
        self.sotrudnik_2 = sotrudnik_2
        self.value_1 = value_1  # локатор на Добавить работников
        self.value_2 = value_2  # локатор на поле ввода работников
        # ищу Кому +Добавить работников
        add_user = driver.find_element(By.XPATH, self.value_1)
        add_user.click()
        time.sleep(2)
        # в открывшемся окне ищу само поле ввода
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
        time.sleep(2)
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


class Vote():  # Для ТК_9 опрос
    def __init__(self, login, input_text, frame_locator):
        self.login = login
        self.input_text = input_text  # текст автоматизированный опрос или др.
        self.frame_locator = frame_locator  # селектор поиска во фрейме

    def opros(self):  # нахожу "Опрос"
        driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-vote']").click()
        time.sleep(2)

    def opros2(self):
        # открываю фрейм, пишу текст
        iframe: WebElement = driver.find_element(By.CSS_SELECTOR, self.frame_locator)
        # "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm > iframe") # локатор
        driver.switch_to.frame(iframe)
        task_txt = driver.find_element(By.TAG_NAME, "body")
        # task_txt.send_keys("Автоматизированный опрос от ", str(input_txt)) # оригинальн. текст
        task_txt.send_keys(self.input_text, str(input_txt))
        driver.switch_to.default_content()
        time.sleep(2)

    def question_form(self):  # нахожу Вопрос в форме опроса
        question_field = driver.find_element(By.XPATH, "//input[@placeholder='Вопрос ']")
        question_field.click()
        question_field.send_keys("Test " + str(input_txt))
        # нахожу Ответ
        answer_field_1 = driver.find_element(By.XPATH, "//input[@placeholder='Ответ  1']")
        answer_field_1.click()
        answer_field_1.send_keys("Ответ 1 - Да (Соболев)")
        answer_field_2 = driver.find_element(By.XPATH, "//input[@placeholder='Ответ  2']")
        answer_field_2.click()
        answer_field_2.send_keys("Ответ 2 - Нет (ОК, Кобякова)")
        # Нахожу Отправить
        send_keys = driver.find_element(By.ID, "blog-submit-button-save")
        send_keys.click()
        time.sleep(3)

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

    # try:


class TestAbs(unittest.TestCase):
    # Авторизация. беру из класса Auth
    auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
    auth_1.autorisation_1()

    def test_abs02(self):
        # ТК_2 Сообщение двум (3 проверки)
        input1_3 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")  # клик в поле
        input1_3.click()
        # текст сообщения. Открываю фрейм с помощью класса
        input2 = Vote(None, "Тест сообщение двум, от ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input2.opros2()
        # Ищу и нажимаю Добавить ещё. Далее ищу и ввожу Поладько и Отдел кадров
        add_user = UsersAdd(None, None, None, None)
        add_user.adding_user_2(user_1, user_2, "(//span[@class='ui-tag-selector-add-button-caption'])[1]",
                               "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        # клик в Отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        time.sleep(1)
        # Проверка, находим элемент, содержащий текст
        actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text"])[1]').text
        needed_text = ("Тест сообщение двум, от " + str(input_txt))
        # Проверка по статусу Кому отправлено
        actual_recipient2 = driver.find_element(By.XPATH, "(//a[@data-bx-entity-id='26538'])[1]").text
        actual_recipient3 = driver.find_element(By.XPATH, "(//a[@data-bx-entity-id='26547'])[1]").text
        self.assertEqual(needed_text, actual_text, "Не тот текст")
        self.assertEqual(user_1, actual_recipient2, "Не тот Пол")
        self.assertEqual(user_2, actual_recipient3, "Не тот Отдел кадров")
        print("ТК_2 сообщение двум ")
        time.sleep(3)

    def test_abs03(self):
        # TK_3 (important message, важное сообщение)
        driver.find_element(By.ID, "feed-add-post-form-link-text").click()  # сообщ - ещё
        driver.find_element(By.XPATH, '(//span[@class="menu-popup-item-text"])[3]').click()  # Важное сообщ в выпадушке
        # текст сообщения, открываю фрейм с помощью класса
        input3 = Vote(None, "Тест на Важное сообщение от ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input3.opros2()
        #Ищу и нажимаю Кому, использую класс User_add и ф-цию для добавления 2-х сотрудников
        add_user = UsersAdd(None, None, None, None)
        # в классе не прописываю значения пользователей и локаторов, тк в разных ф-циях класса они мб разные
        add_user.adding_user_2(user_1, user_2, "(//span[@class='ui-tag-selector-add-button-caption'])[1]",
                               "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        # нажимаю кнопку Отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        time.sleep(1)
        # Проверка по зеленая иконка "i" что важное, проверяю наличие её размера
        green_btn = driver.find_element(By.XPATH, '//div[@class ="feed-important-icon"]').size
        needed_btn = {'height': 56, 'width': 56}
        # проверка по части текста
        actual_text2 = driver.find_element(By.XPATH, "//span[contains(text(), 'С сообщением ознакомлен')]").text
        needed_text = "С сообщением ознакомлен"
        # Проверка по статусу Кому отправлено
        actual_recipient2 = driver.find_element(By.XPATH, "(//a[@data-bx-entity-id='26538'])[1]").text
        actual_recipient3 = driver.find_element(By.XPATH, "(//a[@data-bx-entity-id='26547'])[1]").text
        self.assertEqual(needed_text, actual_text2, "Не тот текст")
        self.assertEqual(needed_btn, green_btn, "Не та кнопка, Урри!")
        self.assertEqual(user_1, actual_recipient2, "Не тот Пол")
        self.assertEqual(user_2, actual_recipient3, "Не тот Отдел кадров")
        print("TK_3 важное сообщение ")
        time.sleep(3)

    def test_abs04(self):
        # TK_4 (message to all)
        input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")  # клик в поле
        input1.click()
        # текст сообщения, открываю фрейм с помощью класса
        input4 = Vote(None, "Отправка сообщения всем работникам \nТест от ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input4.opros2()
        # Ищу и нажимаю Добавить работников, группы или отделы
        ok = driver.find_element(By.XPATH, '(//span[@class="ui-tag-selector-add-button-caption"])[1]')
        ok.click()
        # Ищу в выпадающем списке, поиск по части текста по X-path
        element_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   "//div[text()='Всем работникам']")))
        element_input.click()
        # убираю выпадушку
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        ).click()  # просто клик в поле Кому
        # или такой вариант, он лучше/ Почему перестал работать?!
        # element_input.send_keys(Keys.ESCAPE)
        # ищу и нажимаю Отправить. с ожиданием
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "blog-submit-button-save"))
        )
        button.click()
        # проверка # нахожу в списке Кому с ожиданием
        driver.implicitly_wait(5)
        actual_text4 = driver.find_element(By.XPATH,
                                           '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td['
                                           '2]/table/tbody/tr/td/div/div[2]/div/div[4]/div[3]/div[1]/div/div[1]/div['
                                           '3]/span/span[2]').text
        # проверка по статусу Кому отправлено
        needed_text_4 = "Всем работникам"
        # assert actual_text4 == needed_text_4
        self.assertEqual(needed_text_4, actual_text4, "Не тот текст")
        print("TK_4 Сообщение всем")

    def test_abs05(self):
        # TK_6 (message to one)
        input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")
        input1.click()
        # текст сообщения, открываю фрейм с помощью ф-ции opros2 класса Vote
        input5 = Vote(None, "Тест сообщения одному, от ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input5.opros2()
        # Ищу и нажимаю Добавить ещё. Использую класс UsersAdd и ф-цию в нём
        add_user = UsersAdd(None, None, None, None)
        add_user.adding_user_1(user_1, "(//span[@class='ui-tag-selector-add-button-caption'])[1]",
                               "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        # кнопка отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        time.sleep(1)
        # проверка/ По тексту и получателю
        actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text-block"]/div/div/div)[1]')
        needed_text = ("Тест сообщения одному, от " + str(input_txt))  # текст должен совпадать c Vote(input_text)
        actual_recipient5 = driver.find_element(By.XPATH, "(//a[@data-bx-entity-id='26538'])[1]").text
        self.assertEqual(user_1, actual_recipient5, "Не тот Пол")
        self.assertEqual(needed_text, actual_text.text, "Не тот текст")
        print("TK_6 Сообщение одному")
        time.sleep(1)

    def test_abs06(self):
        # редактирование предыдущего сообщения, TK_5 (edit message to one)
        # нахожу поле, где сообщение, использую три точки
        original_text = driver.find_element(By.XPATH, '(//div[@class="feed-post-right-top-corner"]/div)[1]')
        original_text.click()
        time.sleep(1)
        # нахожу Редактировать. Перебор стрелками не работает
        edit_field = driver.find_element(By.LINK_TEXT, "Редактировать")
        # time.sleep(1)
        edit_field.click()
        # открываю фрейм с помощью ф-ции opros2 класса Vote
        input5 = Vote(None, "=Edited= ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input5.opros2()
        # нахожу и кликаю Отправить
        driver.find_element(By.XPATH, "//span[@id='blog-submit-button-save']").click()
        time.sleep(1)
        # проверка. Нахожу сообщ содержащее слово "Edited", проверяю находится ли слово в тексте
        actual_text = driver.find_element(By.XPATH, "//div[contains(text(), 'Edited')]").text
        self.assertIn("Edited", actual_text, "Текст не отредактирован (не содержит Edited)")
        # проверка что значение истинно, те длина сообщ со словом Edited больше 7
        # self.assertTrue(len(actual_text) >= 7, "Текст не отредактирован (не содержит Edited)")
        # проверяет что длина найденного сообщ содержащего Edited больше нуля, те что оно есть
        # self.assertNotEqual(len(actual_text), 0, "Текст не отредактирован (не содержит Edited)")
        # проверка когда фрейм открывался в данной ф-ции и сравнив-сь вставляемое слово, в данн случае Edited
        # self.assertEqual(input5_1, actual_text, "Не отредактирован текст")
        print("TK_5 редактирование сообщения ")

    def test_abs07(self):
        # TK_7 (Task Задача)
        # нахожу "Задача"
        task_btn = (driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-tasks']"))
        task_btn.click()
        time.sleep(7)
        # открываю фрейм с помощью ф-ции opros2 класса Vote
        iframe_7 = Vote(None, "Текст в теле задачи от ", "#bx-html-editor-iframe-cnt-livefeed_task_form > iframe")
        iframe_7.opros2()
        # нахожу поле для Название задачи
        task_title = driver.find_element(By.XPATH,
                                         "//*[@id='bx-component-scope-livefeed_task_form']/div/div[1]/div[1]/div[2]/input")
        # time.sleep(2)
        task_title.click()
        task_title.send_keys("Задача из Ленты от ", str(input_txt))
        # кнопка Отправить
        driver.find_element(By.XPATH, "//div[@id='feed-add-buttons-blockblogPostForm']/span[1]").click()
        time.sleep(2)
        # переключаюсь на Задачи и проекты
        driver.get(link_7)
        actual_text_7 = driver.find_element(By.XPATH,
                                            "//a[@class='task-title task-status-text-color-in-progress'][contains(text(), 'Задача из Ленты от ')]").text
        needed_text_7 = ("Задача из Ленты от " + str(input_txt))
        self.assertEqual(needed_text_7, actual_text_7, "Не та задача или задача не найдена")
        print("ТК_7 Создать задачу в Ленте")
        # Удалить созданную задачу
        task_burger = driver.find_element(By.XPATH,
                                          "//tbody//td[2]/span[@class='main-grid-cell-content']/a")
        task_burger.click()
        time.sleep(1)
        del_task = (driver.find_element(By.XPATH, "//span[text()='Удалить']"))
        del_task.click()

        driver.get(link)
        time.sleep(2)

    def test_abs08(self):
        # ТК_8 событие в календаре из ленты
        # нахожу "Событие"
        driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-calendar']").click()
        time.sleep(5)
        # поле Название события.
        even_name_field = ("xpath", "//div[@class='calendar-info pinned']/div/div[2]/input")
        driver.find_element(*even_name_field).send_keys("Событие календаря от ", str(input_txt))
        time.sleep(2)
        # ищу кнопку Сохранить
        driver.find_element(*even_name_field).send_keys(Keys.CONTROL + Keys.ENTER)
        time.sleep(3)

        # открытие алерта для проверки
        alert_btn = driver.find_element(By.XPATH,
                                        "//div[@class='ui-notification-balloon ui-notification-balloon-animate']/div/div/span[@class='ui-notification-balloon-action']")
        alert_btn.click()
        time.sleep(2)
        # Проверка
        actual_text_8 = driver.find_element(By.XPATH,
                                            "//span[@class='calendar-head-area-title-name'][contains(text(), 'Событие календаря от ')]").text
        needed_text_8 = ("Событие календаря от " + str(input_txt))
        self.assertEqual(needed_text_8, actual_text_8, "Не то событие в Календаре")
        print("TK_8 Событие календаря")

        # наверное надо закрыть слайдер События. А ещё лучше - удалю
        del_btn = driver.find_element(By.XPATH,
                                      "//button[@class='ui-btn ui-btn-light-border'][contains(text(), 'Удалить')]")
        del_btn.click()
        driver.get(link)
        time.sleep(2)

    def test_abs09(self):  # опрос
        auth_1 = Auth(login_2, pass_2)  # вариант если каждый логин длиннее предыдущего
        # auth_1.autorisation_1()
        vote_1 = Vote(login_2, "Автоматизированный опрос от ",
                      "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm > iframe")
        vote_1.opros()  # нахожу опрос
        time.sleep(2)
        vote_1.opros2()  # фрейм
        time.sleep(2)
        # вынес сюда определение поля, куда вводятся сотрудники, тк в класс нельзя, в каждом кейсе поле своё
        # добавляю пользователей и локатор в класс
        add_user = UsersAdd(None, None, None, None)  # определяю сотрудника и локатор
        # в ф-цию adding_user_1 определяю 1-го сотрудника ОК, и 2 локатора
        add_user.adding_user_3(user_2, user_3, user_4,
                               "//*[@id='entity-selector-oPostFormLHE_blogPostForm']/div/div/div[1]/span/span",
                               "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        time.sleep(2)
        vote_1.question_form()
        time.sleep(2)
        vote_1.vote_users()
        time.sleep(2)
        auth_1.profile_exit()

        auth_2 = Auth(login_3, pass_3)  # Соболев авторизуется
        auth_2.autorisation_1()
        vote_2 = Vote(login_3, None, None)
        # vote_2.opros()
        vote_2.vote_users()
        auth_2.profile_exit()

        auth_3 = Auth(login_4, pass_4)
        auth_3.autorisation_1()
        # Вставил ТК_1. Можно отдельной ф-цией, но тогда нужна отдельная авторизация
        input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner").size
        vote_3 = Vote(login_4, None, None)
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
        self.assertDictEqual(input1, needed_input,
                             "Отсутствие возможности отправить сообщение простым пользователем - не пройдено")
        print("ТК_9 Создать опрос пройден")
        print("ТК_1 Невозможность отправки сообщения в ленте Кобяковой - пройден")

    def test_abs10(self):
        # TK_10 (gratitude message Благодарность)
        # нахожу "Еще"
        driver.find_element(By.ID, "feed-add-post-form-link-text").click()
        # нахожу "Благодарность"
        # driver.find_element(By.CSS_SELECTOR, "span.menu-popup-item.menu-popup-no-icon.feed-add-post-form-grat.feed-add-post-form-grat-more > span.menu-popup-item-text").click()
        driver.find_element(By.XPATH, "//span[text()='Благодарность']").click()
        # текст сообщения
        input10 = Vote(None, "Тест на объявление благодарности от ",
                       "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        input10.opros2()

        # Ищу и нажимаю "Добавить ещё". Использую класс
        add_user = UsersAdd(None, None, None, None)
        add_user.adding_user_2(user_1, user_2, "(//span[@class='ui-tag-selector-add-button-caption'])[1]",
                               "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")

        # для нахожден поля Кто награждается использую класс UsersAdd. Работает несмотря на Ecs
        add_user2 = UsersAdd(None, None, None, None)
        add_user2.adding_user_1(user_2, "//span[text()='Добавить работников']",
                                "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")
        # сразу кнопку Отправить, выпадушку закрыть не надо искать селектор
        button_send = driver.find_element(By.ID, "blog-submit-button-save")
        button_send.click()
        time.sleep(2)

        # Проверка. Найти текст и Дату
        gratitude_text = driver.find_element(By.XPATH,
                                             "//div[@class='feed-post-text'][contains(text(), 'Тест на объявление благодарности от ')]").text
        needed_text = ("Тест на объявление благодарности от " + str(input_txt))
        # Проверка по наличию иконки Благодарность. Не очень корректно, поэтому проверю размер именно этой иконки
        icons = driver.find_element(By.XPATH,
                                    "//div[@class='feed-grat-img']").size  # нахожу размер иконку Благодарность
        self.assertTrue(icons != 0, "Иконка Благодарность отсутствует на странице")
        self.assertEqual(needed_text, gratitude_text, "Не тот текст Благодарности")
        print("TK_10 благодарность ")

    def test_abs14(self):
        # TK_14 (add user in comment)
        # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
        comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
        comment_field.click()
        time.sleep(2)
        # нажимаю кнопку Отметить человека
        # Заменить на adding_user() не получилось, мешает нажатие Esc в конце
        input14 = driver.find_element(By.XPATH, "(//div[@data-id='mention'])[2]")
        input14.click()
        time.sleep(1)
        # ввожу ФИО в открывшееся поле
        input14_name = driver.find_element(By.XPATH,
                                           "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")  # работает, но нужны паузы

        input14_name.send_keys(user_1)
        time.sleep(1)
        input14_name.send_keys(Keys.ENTER)
        time.sleep(1)
        # использовать adding_user_1 не получилось из-за отсутствия клика после нахождения поля Отметить человека
        # Нажимаю Отправить
        input14_sendkey = driver.find_element(By.XPATH,
                                              "(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
        input14_sendkey.click()
        # time.sleep(1)
        # Проверка по ФИО. Это будет actual_text. Локатор только этот!
        actual_text = driver.find_element(By.XPATH, "//a[@class='blog-p-user-name'][contains(text(), 'Поладько')]").text
        self.assertEqual(user_1, actual_text, "Не тот сотрудник (текст) в комментарии")
        print("TK_14 (упоминание сотрудника в комментарии) ")

    def test_abs15(self):
        # ТК_15 Вставить ссылку в комментарии.
        # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
        comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
        comment_field.click()
        time.sleep(1)

        # Ищу кнопку Ссылка"""
        button_link = driver.find_element(By.XPATH, "//span[@title='Ссылка']")
        button_link.click()
        time.sleep(1)
        # Ищу адресную строку. Ввожу ссылку. И текстовую строку"""
        text_link = driver.find_element(By.XPATH, "(//td[@class='bxhtmled-right-c']/input)[1]")
        text_link.send_keys('Официальный сайт РЛИ ')
        adress_link = driver.find_element(By.XPATH, "(//td[@class='bxhtmled-right-c']/input)[2]")
        adress_link.send_keys("https://roslesinforg.ru/")
        adress_link.send_keys(Keys.ENTER)
        time.sleep(1)
        #Нажимаю Отправить"""
        input15_sendkey = driver.find_element(By.XPATH,
                                              "(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
        input15_sendkey.click()
        time.sleep(1)

        # проверка по урл"""
        actual_url = driver.find_element(By.XPATH, "//a[contains(text(), 'Официальный сайт РЛИ')]").get_dom_attribute(
            name='href')
        # needed_url = link_15
        self.assertEqual(link_15, actual_url, "Не та ссылка в комментарии")
        print("ТК_15 (вставка ссылки в комментарий) ")


if __name__ == "__main__":
    unittest.main()
    # print("All tests passed!")

# finally:
# driver.quit()
# не забываем оставить пустую строку в конце файла
