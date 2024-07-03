import requests

from user_api import Api

api = Api("https://api.kinopoisk.dev")

# def test():

#     token = {}
#     token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
#     res = requests.get("https://api.kinopoisk.dev/v1.4/movie?year=2023&genres.name=криминал", headers=token)
#     return res.json()
#     assert len(res) >0


def test_api_search_by_genres():
    name = "криминал"
    body = api.search_films_by_genres(name)
    assert len(body) > 0

def test_api_search_by_name():
    name = "холоп"
    body = api.search_films_by_name(name)
    assert len(body) > 0
 

def test_search_films_by_Rating():
    rating = "0"
    body = api.search_films_by_Rating(rating) 
    assert len(body) > 0


def test_search_top_10_films():
    top = "top10"
    body = api.search_top_10_films(top)
    assert len(body) > 0


def test_search_films_by_rated():
    rating_kp = "7.2-10"
    body = api.search_films_by_rated(rating_kp)
    assert len(body) > 0

def test_search_films_by_years():
    year = "2000"
    body = api.search_films_by_years(year)
    assert len(body) > 0