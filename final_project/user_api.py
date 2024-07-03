import requests


class Api:
    def __init__(self, url) -> None:
        self.url = url

    def get_token(self):
        token = str("Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D")
        return token

    def search_films_by_genres(self, name):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url+"/v1.4/movie?year=2023&genres"+ str(name), headers=token)
        return res.json()
    

    def search_films_by_name(self, name):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url + "/v1.4/movie/search?page=1&limit=1&query="+ str(name), headers=token)
        return res.json()

    
    def search_films_by_Rating(self, rating):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&ageRating=" +str(rating), headers=token)
        return res.json()
        

    def search_top_10_films(self, top):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&notNullFields=" +str(top), headers=token)
        return res.json()

    def search_films_by_rated(self, rating_kp):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&selectFields=name&rating.kp=" +str(rating_kp), headers=token)
        return res.json()
        

    def search_films_by_years(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()


# НИГАТИВНЫЕ 

    def search_films_by_big_years_nigativ(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()
    

    def search_films_by_rated_nigative(self, rating_kp):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&rating.kp=" +str(rating_kp), headers=token)
        return res.json()


    def search_films_by_Rating_nigative(self, rating):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&ageRating=" +str(rating), headers=token)
        return res.json()


    def search_films_by_min_years_nigativ(self, year):
        token = {}
        token["X-API-KEY"] ="Z2QZF5T-P1CMYXF-PSA0BPH-9XRJ91D"
        res = requests.get(self.url +"/v1.4/movie?page=1&limit=10&year=" +str(year), headers=token)
        return res.json()


        