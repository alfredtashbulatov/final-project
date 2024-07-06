import requests
import allure

from user_api import Api

api = Api("https://api.kinopoisk.dev")


@allure.title("Поиск фильмов и сериалов по году большим допустимого значения")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по годам \
                    большим допустимого значения с параметрами 'year=2100'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_big_years_nigative():
    with allure.step("Задать значение парметру 'year'"):
        year = "2100"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по годам \
                     большим допустимого значения"):
        body = api.search_films_by_big_years_nigativ(year)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message' из списка 'body' равна\
                         'Значение поля year должно быть в диапазоне от 1874 до 2050!'"):
            assert body['message'] == ['Значение поля year должно быть в диапазоне от 1874 до 2050!']


@allure.title("Поиск фильмов и сериалов по году большим допустимого значения")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по годам \
                    меньшим допустимого значения с параметрами 'year=1870'")
@allure.feature("SEARCH BY YEAR")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_min_years_nigative():
    with allure.step("Задать значение парметру 'year'"):
        year = "1870"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по годам \
                     большим допустимого значения"):
        body = api.search_films_by_min_years_nigativ(year)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):   
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message' из списка 'body' равна\
                         'Значение поля year должно быть в диапазоне от 1874 до 2050!'"):
            assert body['message'] == ['Значение поля year должно быть в диапазоне от 1874 до 2050!']


@allure.title("Поиск фильмов и сериалов по отрицательному рейтингу")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов по отрицательному рейтингу\
                    с параметром rating_kp= -7")
@allure.feature("SEARCH BY RATED")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_rated_nigative():
    with allure.step("Задать значение парметру 'rating_kp'"):
        rating_kp = "-7"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по отрицательному рейтингу"):    
        body = api.search_films_by_rated_nigative(rating_kp)

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):       
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message' из списка 'body' равна\
                         ''Поле rating.kp должно быть числом или массивом чисел!',\
                               'Значение поля rating.kp должно быть в диапазоне от 0 до 10!'"):    
            assert body['message'] == ['Поле rating.kp должно быть числом или массивом чисел!', 'Значение поля rating.kp должно быть в диапазоне от 0 до 10!']
    

@allure.title("Поиск фильмов и сериалов по неккоректному возростному ограничению")
@allure.description("Тест вызывает Api метод для поиска фильмов и сериалов\
                    по неккоректному возростному ограничению с параметрами ageRating=55")
@allure.feature("SEARCH BY AGE-RATING")
@allure.severity(allure.severity_level.NORMAL)
def test_search_films_by_ageRating_nigative():
    with allure.step("Задать значение парметру 'ageRating'"):
        ageRating = "55"

    with allure.step("Вызвать Api метод для поиска фильмов и сериалов по неккоректному возростному ограничению"): 
        body = api.search_films_by_ageRating_nigative(ageRating) 

    with allure.step("Выполнить прповерки"):
        with allure.step("Проверить, что длина списка в 'body' больше чем '0'"):      
            assert len(body) > 0

        with allure.step("Проверить, что значение ключа 'message' из списка 'body' равна\
                         'Значение поля ageRating должно быть в диапазоне от 0 до 18!'"):
            assert body['message'] == ['Значение поля ageRating должно быть в диапазоне от 0 до 18!']

