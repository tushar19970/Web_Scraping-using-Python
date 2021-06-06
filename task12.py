import json
from typing import Text
import requests 
from pprint import pprint
from bs4 import BeautifulSoup

json_files = open("task1_data.json", "r")
movie_caste_url = json.load(json_files)
json_files.close()

def scrape_movie_cast(movie_caste_url):
    list = []
    for i in movie_caste_url:
        for j in i:
            if j == "url":
                list.append(i[j])
    for k in list:
        url = requests.get(k)
        soup = BeautifulSoup(url.text, "html.parser")
        name = soup.find_all("a",class_="ipc-lockup-overlay ipc-focusable")
        list2 = []
        for l in name:
            dict1 = {}
            ddd = l["href"][6:16]
            aaa = ddd.replace("?","")
            if "nm" in ddd:
                dict1["Imdb_id"],dict1["Name"]= aaa, l["aria-label"][:15]
                list2.append(dict1)

    json_files = open("task12_data.json", "w")
    json.dump(list2, json_files, indent = 4)
    json_files.close()
    return list2

task12 = scrape_movie_cast(movie_caste_url[:25])
# pprint(task12)