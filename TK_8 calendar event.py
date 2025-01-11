"""Тест кейс 8 - Событие в календаре"""
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
link_8 = "https://intranet-test.roslesinforg.ru/company/personal/user/26547/calendar/"
user_1 = "Поладько Дмитрий"
user_2 = "Отдел Кадров"


try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()  # чтобы браузер не закрывался
    driver = webdriver.Chrome(options=options, service=g)
    wait = WebDriverWait(driver, 10, poll_frequency=1)  # ожидание 10 сек с частотой проверки 1 сек)
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    # time.sleep(1)

    input_txt = datetime.now().replace(microsecond=0)  # текст в поле, будет каждый раз разный
    print("date = ", input_txt)

    # нахожу "Событие"
    driver.find_element(By.XPATH, "//span[@id='feed-add-post-form-tab-calendar']").click()
    time.sleep(5)

    """В связи с тем что в поле не ввести (локатор хоть и правильный, но не срабатывает) и в 7м кейсе сначала"""
    """вводился текст в поле с фреймом и только потом название задачи в поле, то буду пытаться активировать поле с названием разными способами"""



    # поле Название события. ===оказывается работает и без ожидания. Вместо клика сразу вводить текст
    even_name_field = ("xpath", "//div[@class='calendar-info pinned']/div/div[2]/input")
    # wait.until(EC.element_to_be_clickable(even_name_field)) # ожидание что поле будет кликабельно. выдает ошибку на моменте send_keys мол кортеж не имеет аттрибут
    # wait.until(EC.presence_of_element_located(even_name_field))  # Ожидает, что элемент будет присутствовать в DOM - работает
    # time.sleep(2)
    driver.find_element(*even_name_field).send_keys("Событие календаря от ", str(input_txt))

    """следующий блок не идет, не распечатывает scheduler_action_2. Возможно надо переделать even_name_field или искать другой способ проверки исходного текста"""

    # scheduler_action = driver.find_element(*even_name_field)
    # scheduler_action.send_keys("Событие календаря от ", str(input_txt))
    # print("scheduler_action - ", scheduler_action)
    # time.sleep(3)
    # scheduler_action_2 = scheduler_action.text
    # print("scheduler_action_2 - ", scheduler_action_2)

    # (By.XPATH, "//div[@class='calendar-info pinned']/div/div[2]/input")
    # even_name_field.click()
    # even_name_field.send_keys("Testing ")
    time.sleep(2)
    # ищу кнопку Сохранить
    # save_btn = driver.find_element(By.XPATH, "//div[@class='calendar-form-footer-container']/button[1]")
    # save_btn.click()
    # или сразу нажать ctrl+Enter
    driver.find_element(*even_name_field).send_keys(Keys.CONTROL + Keys.ENTER)
    time.sleep(3)

    # переключаюсь на календарь
    # driver.get(link_8)

    # локатор на текст
    # //div[@class ="calendar-grid-month calendar-grid-month-current"]/span[@class='calendar-event-line-text'][contains(text(), 'Событие календаря ')]
    # //*[@class='calendar-main-container calendar-main-container--scope']/div[2]/div[3]/div[2]/div/div/div[4]/div[8]/div[1]/div/div/span[2]/span основной поиск локатора
    # //*[@class='calendar-main-container calendar-main-container--scope'][contains(text(), 'Событие календаря ')]
#     //*[@id="EC1480541055-main-container"]/div[2]/div[3]/div[2]/div/div/div[4]/div[8]/div[1]/div/div/span[2]/span
#     even_field = driver.find_element(By.LINK_TEXT, "Событие календаря от ")  #
#     even_field = driver.find_element(By.XPATH, "//div[@class='calendar-month-view']/div[2]/div/div/div[2]/div/div/span")
    # //div[@class='calendar-month-view']/[contains(text(), 'Событие календаря от ')]
    # even_field.click()

    # """попытаюсь открыть на главной странице, в Ближайшие события"""
    # actual_text_8 = driver.find_element(By.XPATH, "//div[@class='sidebar-widget sidebar-widget-calendar']/div[2]/a/span/span[contains(text(), 'Событие календаря от ']").text
    # """если несколько событий, > 1 или 2, то не ищет корректно"""
    # print("actual_text_8 - ", actual_text_8)
    # needed_text_8 = ("Событие календаря от " + str(input_txt))
    # print("needed_text_8 - ", needed_text_8)

    """Или открывать событие календаря по алерту? тк искать в самом календаре можно и ошибиться. настроить локатор, но дата сменится и будет искать в другом месте"""
# открытие алерта
#     alert_btn = driver.switch_to.alert
#     alert_txt = alert_btn.text
#     print("alert_txt - ", alert_txt)
# //div[@class='ui-notification-balloon-message']   /div/span

    # оказывается это не алерт, ищется стандартно, только успеть надо
    alert_btn = driver.find_element(By.XPATH, "//div[@class='ui-notification-balloon ui-notification-balloon-animate']/div/div/span[@class='ui-notification-balloon-action']")
    alert_btn.click()
    time.sleep(2)

    actual_text_8 = driver.find_element(By.XPATH,
                                      "//span[@class='calendar-head-area-title-name'][contains(text(), 'Событие календаря от ')]").text

    # or class="main-grid-row main-grid-row-body" & contains(text())
    print("actual_text - ", actual_text_8)
    needed_text_8 = ("Событие календаря от " + str(input_txt))
    print("needed_text_8 - ", needed_text_8)
    assert actual_text_8 == needed_text_8

    # наверное надо закрыть слайдер События. А ещё лучше - удалю
    del_btn = driver.find_element(By.XPATH, "//button[@class='ui-btn ui-btn-light-border'][contains(text(), 'Удалить')]")
    del_btn.click()

finally:
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    driver.quit()
    # не забываем оставить пустую строку в конце файла