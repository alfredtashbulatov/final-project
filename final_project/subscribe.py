from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from time import sleep
import allure


class Buy_subscribe:

    def __init__(self, browser):
        self.browser = browser


    @allure.step("оформление подписки")    
    def add_card(self, card_number, data, cvc):
        with allure.step("Ввод данный в пооле 'Номер карты'"):
            self.browser.find_element(By.CSS_SELECTOR, 'input[id="regular-card-number-input"]').send_keys(card_number)
            sleep(1)
# ввод cvc cod
        with allure.step("Ввод данны для поля 'cvc'"):
            self.browser.find_element(By.CSS_SELECTOR, 'div[class="card-form__shutter shutter_cvv"]' ).send_keys(cvc)
            sleep(2)
# ввод дат
        with allure.step("Ввод данных для поля 'Срок карты'"):
            self.browser.find_element(By.CSS_SELECTOR, 'div[class="column column_date-filler"]' ).send_keys(data)
            sleep(2)