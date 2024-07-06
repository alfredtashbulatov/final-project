from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import allure
import pytest
from subscribe import Buy_subscribe
from aut_login import Aut_and_reg
from search_films import Search_films_and_TV_series
import allure



@allure.title("Регистрация, покупка подписки, просмотр фильмов исериалов")
@allure.description("Тест проходит полный путь до  просмотра фильма.\
                    Регистрация, авторизация, покупка подписки, поиск фильма(сериала), просмотр")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SMOKE")
def test_smoke():
    with allure.step("Инициализировать браузер"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса Aut_and_reg"):
        auth = Aut_and_reg(browser)

    with allure.step("Вызвать метод для авторизации"):    
        auth.auth_by_mail(mail="malalfred", password="jvp+XTdf3Esmjtz")

    with allure.step("Передать браузер в конструктор класса Search_films_and_TV_series"):
        search = Search_films_and_TV_series(browser)

    with allure.step("Вызвать метод для поиска"): 
        search.search_content(films="на автомате")
    

@allure.title("Тест оформления подписки")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SMOKE")
def test_buy():
    with allure.step("Инициализировать браузер"):
         browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса Aut_and_reg"):
        auth = Aut_and_reg(browser)

    with allure.step("Вызвать метод для авторизации"):    
        auth.auth_by_mail(mail="Your mail", password="your password")

    with allure.step("Передать браузер в конструктор класса Buy_subscrib"):
        buy = Buy_subscribe(browser)

    with allure.step("Вызвать метод для добавления карты"):
        buy.add_card(card_number="0000 0000 0000 0000", data="ММ/гг", cvc="000")


@allure.title("Авторизация пользователя")
@allure.description("Тест выполняет авторизацию пользователя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("SMOKE")
def test_user_authorization():
    with allure.step("Инициализировать браузер"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса Aut_and_reg"):
        auth = Aut_and_reg(browser)

    with allure.step("Вызвать метод для авторизации"):    
        auth.auth_by_mail(mail="malalfred", password="jvp+XTdf3Esmjtz")








# # '#passp:exp-register'
# browser = webdriver.Chrome()
# browser.get("https://www.kinopoisk.ru/s/")
# sleep(2)


# # поиск фильмов 
# # ввод названия 
# browser.find_element(By.CSS_SELECTOR, 'input[role="combobox"]').send_keys("холоп 2")
# sleep(2)
# # клик по кнопке поиск 
# browser.find_element(By.CSS_SELECTOR, 'button[data-tid="f49ca51f"]').send_keys(keys.Keys.ENTER)
# sleep(2)
# browser.find_element(By.CSS_SELECTOR, 'a[href="/film/5047468/sr/1/"]').click()
# sleep(4)
# #клик по кнопке смотреть 
# browser.find_element(By.CSS_SELECTOR, 'button[id="button-film"]').click()
# sleep(2)















# оформлениеи подписки 
# Добавление карты
# ввод номера карты 
# browser.find_element(By.CSS_SELECTOR, 'input[id="regular-card-number-input"]').send_keys("5469 0600 2526 4331")
# sleep(1)

# # ввод cvc cod
# browser.find_element(By.CSS_SELECTOR, 'div[class="card-form__shutter shutter_cvv"]' ).send_keys("947")
# sleep(2)
# # ввод даты
# browser.find_element(By.CSS_SELECTOR, 'div[class="column column_date-filler"]' ).send_keys("10 25")
# sleep(2)