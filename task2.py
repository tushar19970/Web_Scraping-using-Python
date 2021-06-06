import json
from pprint import pprint
from task1 import*

def group_by_year(movies):
    release_years = []
    for i in movies :
        year1 = i["years"]
        if year1 not in release_years:
            release_years.append(year1)
            release_years.sort()
    movies_dict={i:[]for i in release_years}
    for j in movies:
        year1 = j["years"] 
        for k in movies_dict:
            if str(k) ==  str(year1):
                movies_dict[k].append(j)   
        b = open("task2_data.json", "w")
        json.dump(movies_dict, b, indent = 4)
        b.close()
    return movies_dict
task2 = (group_by_year(task1))
# pprint(task2)