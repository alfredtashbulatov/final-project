import requests

from user_api import Api

api = Api("https://api.kinopoisk.dev")



def test_search_films_by_big_years_nigative():
    year = "2100"
    body = api.search_films_by_big_years_nigativ(year)
    assert len(body) > 0

def test_search_films_by_rated_nigative():
    rating_kp = "-7"
    body = api.search_films_by_rated_nigative(rating_kp)
    assert len(body) > 0

def test_search_films_by_Rating_nigative():
    rating = "55"
    body = api.search_films_by_Rating_nigative(rating) 
    assert len(body) > 0

def test_search_films_by_min_years_nigative():
    year = "1870"
    body = api.search_films_by_min_years_nigativ(year)
    assert len(body) > 0