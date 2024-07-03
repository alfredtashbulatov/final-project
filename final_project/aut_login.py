from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from time import sleep
import allure



class Aut_and_reg:
    
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.kinopoisk.ru/s/")
    
    @allure.step("Регистрация")
    def registration_by_phone(self):

        with allure.step("Клик по кнопке 'Войти'"):
            self.browser.find_element(By.CSS_SELECTOR, 'button[class="ZbVGA14bTNo86weQTABU"]').click()
            sleep(2)

        with allure.step("Клик по кнопке 'Создать ID'"):
            self.browser.find_element(By.CSS_SELECTOR, 'a[id="passp:exp-register"]').click()
            sleep(2)

        with allure.step("Клик по кнопке 'Для себя'"):
            self.browser.find_element(By.XPATH, "//button[text()='Для себя']").click()
            sleep(2)

    
        with allure.step("Ввод данных в поле номер телефона"):
            self.browser.find_element(By.CSS_SELECTOR, '#passp-field-phone').send_keys("9999948859")
            sleep(2)
    
        with allure.step("Клик по кнопке 'Далее'"):
            self.browser.find_element(By.CSS_SELECTOR, "button[id='passp:phone:controls:next']").click()
            sleep(6)


    @allure.step("Авторизация")
    def auth_by_mail(self, mail, password):
        with allure.step("Клик по кнопке 'Войти'"):
            self.browser.find_element(By.CSS_SELECTOR, 'button[class="ZbVGA14bTNo86weQTABU"]').click()
            sleep(2)

        with allure.step("Ввести в поле 'mail' почтовый адресс"):    
            self.browser.find_element(By.CSS_SELECTOR, 'input[id="passp-field-login"]').send_keys(mail)
            sleep(1)


        with allure.step("Кликнуть по кнопке 'Войти'"): 
            self.browser.find_element(By.CSS_SELECTOR, 'button[id="passp:sign-in"]').click()
            sleep(1)


        with allure.step("Выбрать способ входа. (По паролю)"): 
            self.browser.find_element(By.CSS_SELECTOR,'button[data-t="button:pseudo"]').click()
            sleep(2)


        with allure.step("Ввести в поле 'password' пароль "): 
            self.browser.find_element(By.CSS_SELECTOR, 'input[id="passp-field-passwd"]').send_keys(password)
            sleep(2) 


        with allure.step("Кликнуть по кнопке 'продолжить'"): 
            self.browser.find_element(By.CSS_SELECTOR, 'button[id="passp:sign-in"]').click()
            sleep(5)
