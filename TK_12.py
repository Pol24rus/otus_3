"""Фильтр в Ленте. Проверить отсутствие Важных сообщений, Благодарностей и Опросов"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime
from a_user import *
# input_txt = datetime.now() # текст в поле, будет каждый раз разный

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys(login_2)
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys(pass_2)
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    #time.sleep(1)


    
    #нахожу "Фильтр и поиск"
    driver.find_element(By.XPATH, "//input[@placeholder='Фильтр + поиск']").click()
    time.sleep(2)
    # нахожу "Тип"
    type_field = driver.find_element(By.XPATH, "//div[@data-name='EVENT_ID']")  # возможно сделать с "...)[1]"
    # type_field = driver.find_element(By.XPATH, "//div[@class='main-ui-control main-ui-multi-select']")
    type_field.click()
    """Выбрать из выпадушки Благодарность и проверить отсутствие Опросов и важных. 
    Для сброса достаточно обновить страницу. Вопрос: прокручивать ли и как страницу до конца? 
    Как в одном кейсе проверить три типа сообщений, или заводить новые функции в итоговом файле?"""
    # # текст сообщения
    # iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    # driver.switch_to.frame(iframe1)
    # input2 = driver.find_element(By.TAG_NAME, "body")
    # input2.send_keys("Тест на объявление благодарности от ", str(input_txt))
    # driver.switch_to.default_content()
    #
    # #Ищу и нажимаю Добавить ещё
    # driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption").click()
    # # ищу и ввожу Поладько и Отдел кадров
    # element_input = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
    #     )
    # time.sleep(1)
    # element_input.send_keys("Поладько")
    # time.sleep(1)
    # element_input.send_keys(Keys.ENTER)
    # time.sleep(1)
    # element_input.send_keys("Отдел")
    # time.sleep(1)
    # element_input.send_keys(Keys.ENTER)
    # # убираю Всем работникам
    # driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click()
    #
    # #Найти "Кто награждается" и ввести ФИО
    # driver.find_element(By.CSS_SELECTOR, "#entity-selector-dest-selector-blog-post-form-grat > div > div > div.ui-tag-selector-items > span > span").click()
    # element_input2 = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#entity-selector-dest-selector-blog-post-form-grat > div > div > div.ui-tag-selector-items > input"))
    #     )
    # time.sleep(1)
    # element_input2.send_keys("Поладько")
    # time.sleep(1)
    # element_input2.send_keys(Keys.ENTER)
    #
    # button = driver.find_element(By.ID, "blog-submit-button-save")
    # button.click()
    # time.sleep(2)
    #
    # """найти картинку Палец вверх и ФИО. Или Дату? или это два разных условия"""
    # gratitude_text = driver.find_element(By.XPATH, "//div[@class='feed-post-text'][contains(text(), 'Тест на объявление благодарности от ')]").text
    # # [contains(text(), '"Тест на объявление благодарности от ", str(input_txt)')]
    # print("текст благодарности - ", gratitude_text)
    # needed_text = ("Тест на объявление благодарности от " + str(input_txt))
    # print("требуемый текст - ", needed_text)
    # assert gratitude_text == needed_text
    # gratitude_simbol = driver.find_element(By.XPATH, "//div[@class='feed-grat-img']")  # значок палец вверх
    # Проверка по наличию иконки Благодарность.
    # icons = driver.find_element(By.XPATH, "//div[@class='feed-grat-img']")  # нахожу иконку Благодарность
    # использовать assertIn для проверки нахождения иконки на stream upd: не работает, нужен список а не webelement
    # self.assert_(icons, "нет иконки Благодарность")  # проверка наличия элемента на странице.
    # self.assertTrue(driver.find_element(By.XPATH, "//div[@class='feed-grat-img']"), "нет иконки Благодарность")

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла