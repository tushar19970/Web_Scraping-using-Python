import json,pprint
file=open("/home/navgurukul/Desktop/IMDB_Task/task12_data.json",'r')
movie_list = json.load(file)

def analyse_co_actors():
    movies_cast = []
    for cast in movie_list:
        cast_dict = {}
        for i in range(len(cast)-1):
            actors_list=[]
            actors_dict={}
            actors_dict['Imdb_id'] = cast[i+1]["Imdb_id"]
            actors_dict["Name"] = cast[i+1]['Name']
            Count = 0
            for Movies in movie_list :
                if cast[i] in Movies and cast[i+1] in Movies:
                    Count+=1
            actors_dict['count_movies'] = Count
            actors_list.append(actors_dict)
            cast_dict[cast[i]['Imdb_id']]={"Name":cast[i]['Name'],'frequent_co_actors':actors_dict}
        movies_cast.append(cast_dict)
        
    f=open('task14_data.json','w')
    json.dump(movies_cast,f,indent=4)
    f.close()
    return movies_cast

task_14=analyse_co_actors()
# pprint.pprint(task_14)
