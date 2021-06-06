import  requests
import json 
from pprint import pprint 
from bs4 import BeautifulSoup
from requests.api import request

def scrape_top_list():
    page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
    a = BeautifulSoup(page.text,'html.parser') 
    b = a.find("div",class_= "lister")
    c = b.find("tbody", class_= "lister-list")
    d = c.find_all("tr")

    movies_name, years, position, rating, url = [],[],[],[],[]

    for movie in d :
        movies_name.append(movie.find("td",class_="titleColumn").find("a").get_text())
        rate = (movie.find("td",class_="ratingColumn imdbRating").text)
        rating.append(float(rate.strip()))
        years.append(int(movie.find("span",class_="secondaryInfo").text[1:5]))
        position.append(int(movie.text.strip().split('.')[0]))
        url.append('https://www.imdb.com'+movie.find('a').get('href'))
    return page_information(movies_name, rating, years, position, url)

def  page_information(movies_name, rating, years, position, url):
    dic = {}
    Top_250_movies = []
    for j, k, l, m, n, in zip(movies_name, rating, years, position, url):
        dic["movies_name"] = j
        dic["rating"] = k
        dic["years"] = l
        dic["position"] = m
        dic["url"] = n
        Top_250_movies.append(dic.copy())
    js = open("task1_data.json", "w")
    json.dump(Top_250_movies, js, indent = 4)
    js.close()
    return Top_250_movies
task1 = scrape_top_list()
# pprint(task1)