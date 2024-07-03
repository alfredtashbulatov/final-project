from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from time import sleep
import allure

class Search_films_and_TV_series:

    def __init__(self, browser):
        self.browser = browser
        # self.browser.get("https://www.kinopoisk.ru/")

    
    @allure.step("Поиск фильмов и сериалов")
    def search_content(self, films):
        
        with allure.step("Ввести в поле поиска название фильма"):
            self.browser.find_element(By.CSS_SELECTOR, 'input[role="combobox"]').send_keys(films)
            sleep(2)
    
        with allure.step("Нажать кнопку 'Поиск'"):
            self.browser.find_element(By.CSS_SELECTOR, 'button[data-tid="f49ca51f"]').send_keys(keys.Keys.ENTER)
            sleep(2)

        with allure.step("Кликнуть по нужному фильму"):
            self.browser.find_element(By.CSS_SELECTOR, 'a[href="/film/5388902/sr/1/"]').click()
            sleep(2)

        with allure.step("Нажать кнопку 'Смотреть'"):
            self.browser.find_element(By.CSS_SELECTOR, 'a[data-test-id="Watch"]').click()
            sleep(20)
               
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




















