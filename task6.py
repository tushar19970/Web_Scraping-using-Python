from pprint import pprint
import json 
# from  task5 import *

files = open("task5_data.json", "r")
load_of_json = json.load(files)

def analyse_movies_language(movies):
    list1 = []
    for i in movies:
        for j in i["Movie_Language"]:
            list1.append(j)
            temp = set(list1)
            language_dict = {}
            for i in temp:
                language_dict[i]=list1.count(i)

    json_file = open("task6_data.json", "w")
    json.dump(language_dict, json_file, indent = 4)
    json_file.close()
    return language_dict
    
task6 = analyse_movies_language(load_of_json)
# pprint(task6)