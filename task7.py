import json
# from task5 import *
from pprint import pprint

files = open("task5_data.json", "r")
load_of_json = json.load(files)
files.close()

def analyse_movies_directors(movies):
    list1 = []
    for i in movies:
        for j in i["director"]:
            list1.append(j)
            temp = set(list1)
            director_dict = {}
            for k in temp:
                director_dict[k] = list1.count(k)
    json_files = open("task7_data.json", "w")
    json.dump(director_dict, json_files, indent = 4)
    json_files.close()
    return director_dict
task7 = analyse_movies_directors(load_of_json)
# pprint(task7)