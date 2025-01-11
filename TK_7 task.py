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

link = "https://intranet-test.roslesinforg.ru/stream/"
link_7 = "https://intranet-test.roslesinforg.ru/company/personal/user/26547/tasks/"
user_1 = "Поладько Дмитрий"
user_2 = "Отдел Кадров"


try:
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()  # чтобы браузер не закрывался
    driver = webdriver.Chrome(options=options, service=g)
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    # time.sleep(1)

    input_txt = datetime.now()  # текст в поле, будет каждый раз разный

    # нахожу "Задача"
    # task_field = (driver.find_element(By.ID, "feed-add-post-form-tab-tasks"))
    # task_field.click()  # поиск по ID CSS
    driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-tasks']").click()  # поиск по xpath
    time.sleep(5)

    """сначала открыть фрейм, потом открывать поле для имени задачи"""
    # текст сообщения
    iframe7: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-livefeed_task_form > iframe")
    # iframe7: WebElement = driver.find_element(By.XPATH, "//*[@id='bx-html-editor-iframe-cnt-livefeed_task_form'] > iframe")
    driver.switch_to.frame(iframe7)
    task_txt = driver.find_element(By.TAG_NAME, "body")
    task_txt.send_keys("Текст в теле задачи от ", str(input_txt))
    driver.switch_to.default_content()
    time.sleep(2)
    # нахожу поле для Название задачи
    task_title = driver.find_element(By.XPATH, "//*[@id='bx-component-scope-livefeed_task_form']/div/div[1]/div[1]/div[2]/input")
    # time.sleep(2)
    task_title.click()
    # time.sleep(2)
    task_title.send_keys("Тестовая задача от ", str(input_txt))
    # кнопка Отправить
    driver.find_element(By.XPATH, "//div[@id='feed-add-buttons-blockblogPostForm']/span[1]").click()
    time.sleep(2)

    # переключаюсь на Задачи и проекты
    driver.get(link_7)
    # actual_text = driver.find_element(By.XPATH, "//table[@class='main-grid-table']/tbody/tr[2]/td[3]/div/span[1]/a/text()").text
    actual_text_7 = driver.find_element(By.XPATH,
                                      "//a[@class='task-title task-status-text-color-in-progress'][contains(text(), 'Тестовая задача от ')]").text
    # or class="main-grid-row main-grid-row-body" & contains(text())
    print("actual_text - ", actual_text_7)
    needed_text_7 = ("Тестовая задача от " + str(input_txt))
    print("needed_text_7 - ", needed_text_7)
    assert actual_text_7 == needed_text_7


finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла