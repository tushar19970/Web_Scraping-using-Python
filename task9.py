import json
import os
import time 

files = open("task1_data.json", "r")
json_files = json.load(files)
files.close()

def scrape_movie_details_again(json_files):
    aa = int (input("Which position of movie data do you want to check ? "))
    for i in json_files[:aa]:
        link = (i['url'])
        movie_id = ''
        for _id in link[27:]:
            if '/' not in _id :
                movie_id += _id
            else:
                break
        file_name = movie_id + ".json"
        if not os.path.exists(file_name):
            print("No Catch Data")
            second = 3 
            for i in range (second):
                print(str(second - i))
                time.sleep(1)
            file1 = open(file_name, "w")
            temp = json.dumps(i, indent = 4)
            file1.write(temp)
            file1.close()
        else:
            print("File Already exixts ")
            second = 3 
            for i in range (second):
                print(str(second - i))
                time.sleep(1)
task9 = scrape_movie_details_again(json_files)
# pprint(task9)

