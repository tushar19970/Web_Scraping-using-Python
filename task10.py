import json
from pprint import pprint

files_json = open ("task5_data.json", "r")
files = json.load(files_json)
files_json.close()

def annlays_director_and_language():
    director_dic = {}
    for movie in files:
        for director in movie["director"]:
            director_dic[director] = {}
            
    for i in range (len(files)):
        for director in director_dic:
            if director in files [i]["director"]:
                for language in files[i]["Movie_Language"]:
                    director_dic[director][language] = 0

    for i in range (len(files)):
        for director in director_dic:
            if director in files [i]["director"]:
                for language in files[i]["Movie_Language"]:
                    director_dic[director][language] += 1

    json_files = open("task10_data.json", "w")
    json.dump(director_dic, json_files, indent = 4)
    json_files.close()

    return director_dic

director_by_language = annlays_director_and_language() 
# pprint(director_by_language)





