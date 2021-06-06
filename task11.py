from pprint import pprint
import json 

json_files = open("task5_data.json", "r")
files =  json.load(json_files)
json_files.close()

def analyse_movies_genre():
    list1 = []
    for movie in files:
        for genre in movie["genre"]:
            list1.append(genre)
            temp = set(list1)
            movie_genre = {}
            for genre in list1:
                movie_genre[genre] = list1.count(genre)

    files_11 = open("task11_data.json", "w")
    json.dump(movie_genre,files_11, indent = 4)
    files_11.close()

    return movie_genre
task11 = analyse_movies_genre()
# pprint(task11)