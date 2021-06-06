from pprint import pprint
import json 

task5 = open("task5_data.json", "r")
task = json.load(task5)

task12 = open("task12_data.json", "r")
sec_task = json.load(task12)

def scrape_movie_details():
    dict1 = {}
    list1 = []
    for i, j in zip(task, sec_task):
        dict1["Movie_Name"] = i 
        dict1["Cast"] = j
        list1.append(dict1.copy())

    json_files = open("task13_data.json", "w")
    json.dump(list1, json_files, indent = 4)
    json_files.close()
    return list1

task13 = scrape_movie_details()
# pprint(task13) 