import requests
import allure
from user_api import Api

api = Api("https://api.kinopoisk.dev")


@allure.title("Поиск фильмов и сериалов по жанру")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по жанру с параметрами genre = криминал")
@allure.feature("SEARCH BY GENRES")
@allure.severity(allure.severity_level.BLOCKER)
def test_api_search_by_genres():
    with allure.step("Задать значение параметру 'genre'"):
        genre = "криминал"
    with allure.step("Вызвать Api метод для поиска по жанрам"):
        body = api.search_films_by_genres(genre)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и серилов по названию")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по названию с параметрами name = холоп")
@allure.feature("SEARCH BY NAME")
@allure.severity(allure.severity_level.BLOCKER)
def test_api_search_by_name():
    with allure.step("Задать значение параметру 'name'"):
        name = "холоп"

    with allure.step("Вызвать Api метод для поиска по названию"):
        body = api.search_films_by_name(name)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0
        
 

@allure.title("Поиск фильмов и сериалов по возростному ограничению")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по возростному ограничению с параметром ageRating = 0")
@allure.feature("SEARCH BY AGE-RATING")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_films_by_ageRating():
    with allure.step("Задать значение параметру 'ageRating'"):
        ageRating = "0"
    with allure.step("Вызвать Api метод для поиска по возростному ограничению"):
        body = api.search_films_by_ageRating(ageRating) 

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск топ 10 фильмов и сериалов")
@allure.description("Тест вызывает Api метод для поиска ТОП-10 фильмов и сериалов с параметром top = top10")
@allure.feature("SEARCH BY TOP-10")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_top_10_films():
    with allure.step("Задать значение параметру 'top'"):
        top = "top10"

    with allure.step("Вызвать Api метод для поиска ТОП-10 фильмов и сериалов"):
        body = api.search_top_10_films(top)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по рейтингу")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по ")
@allure.feature("SEARCH BY RATED")
@allure.severity(allure.severity_level.BLOCKER)
def test_search_films_by_rated():
    with allure.step("Задать значение параметру 'rating_kp'"):
        rating_kp = "7.2-10"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по рейтингу"):
        body = api.search_films_by_rated(rating_kp)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0


@allure.title("Поиск фильмов и сериалов по году")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по годам \
                    с параметрами 'year=2000'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_films_by_years():
    with allure.step("Задать значение параметру 'rating_kp'"):
        year = "2000"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по годам"):   
        body = api.search_films_by_years(year)

    with allure.step("Выполнить проверки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0