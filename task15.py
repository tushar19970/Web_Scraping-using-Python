import json 
from pprint import pprint

json_files = open("task13_data.json", "r")
files = json.load(json_files)
json_files.close()

def analyse_actors(movies):
    dic1 = {}
    dic2 = {}
    for id in movies:
        cast = (id["Cast"])
        for i in cast:
            imdb = (i["Imdb_id"])
            if imdb in dic1:
                dic1[imdb]+=1
            else:
                dic1[imdb]=1
    for i in dic1:
        for id in movies:
            cast = (id["Cast"])
            for j in cast:
                if i == (j["Imdb_id"]) and i not in dic2:
                    dic2[i]={"Name":j["Name"],"num_movies":dic1[i]}
    
    json_files = open("task15_data.json", "w")
    json.dump(dic2, json_files, indent = 4)
    json_files.close()
    return dic2
        
task15 = analyse_actors(files)
# pprint(task15)
