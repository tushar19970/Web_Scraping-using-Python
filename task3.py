from task2 import*
import json 
from pprint import pprint

def group_by_decade(movies):
    movies_decade = {}
    list1 = []
    for i in movies:
        mode = i % 10
        decade = i - mode 
        if decade not in list1 :
            list1.append(decade)
    print(sorted(list1))
    for i in list1:
        movies_decade[i] = []
    for k in list1:
        dec = k + 9
        for l in movies:
            if l <= dec and l >= k:
                for m in movies[l]:
                    movies_decade[k].append(m)
                b = open("task3_data.json", "w")
                json.dump(movies_decade, b, indent = 4)
                b.close()
    return movies_decade
task3 = group_by_decade(task2)
# pprint(task3)
