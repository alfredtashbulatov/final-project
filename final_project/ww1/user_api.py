import requests
import allure

class Api:
    def __init__(self, url) -> None:
        self.url = url

    @allure.step("Api. Получить токен авторизации")
    def get_token(self):
        token = str("Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D")
        return token

    @allure.step("Api. Поиск фильмов, сериалов по жанру {genre}")
    def search_films_by_genres(self, genre):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url+"/v1.4/movie?year=2023&genres"+ str(genre), headers=token)
        return res.json()
    
    @allure.step("Api. Поиск фильмов, сериалов по названию {name}")
    def search_films_by_name(self, name):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url + "/v1.4/movie/search?page=1&limit=1&query="+ str(name), headers=token)
        return res.json()

    @allure.step("Api. Поиск фильмов, сериалов по возростному ограничению {ageRating}")
    def search_films_by_ageRating(self, ageRating):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&ageRating=" +str(ageRating), headers=token)
        return res.json()
        
    @allure.step("Api. Поиск топ 10 фильмов и сериалов зв месяц {top}")
    def search_top_10_films(self, top):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&notNullFields=" +str(top), headers=token)
        return res.json()

    @allure.step("Api. Поиск фильмов и сериалов по рейтингу {rating_kp}")
    def search_films_by_rated(self, rating_kp):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&selectFields=name&rating.kp=" +str(rating_kp), headers=token)
        return res.json()
        
    @allure.step("Api. Поиск фильамов и сенриалов по годам {year}")
    def search_films_by_years(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()


# НИГАТИВНЫЕ 
    @allure.step("Api. Поиск фильамов и сенриалов по годам большим допустимого значения {year}")
    def search_films_by_big_years_nigativ(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()
    
    @allure.step("Api. Поиск фильмов и сериалов по отрицательному рейтингу {rating_kp}")
    def search_films_by_rated_nigative(self, rating_kp):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&rating.kp=" +str(rating_kp), headers=token)
        return res.json()

    @allure.step("Api. Поиск фильмов, сериалов по неккоректному возростному ограничению {ageRating}")
    def search_films_by_ageRating_nigative(self, ageRating):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&ageRating=" +str(ageRating), headers=token)
        return res.json()

    @allure.step("Api. Поиск фильамов и сенриалов по годам меньшим допустимого значения {year}")
    def search_films_by_min_years_nigativ(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()


        