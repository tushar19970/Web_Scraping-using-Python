import requests,json
from pprint import pprint
from bs4 import BeautifulSoup

json_files = open("task1_data.json","r")
files = json.load(json_files)

def scrape_movie_details(movie):
    d = []
    for i in movie:
        for j in i:
            if j=="url":
                d.append(i[j])
    list1=[]
    c=1
    dict1={}
    for j in d:
        url=requests.get(j)
        soup=BeautifulSoup(url.text,"html.parser")
        ul=soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        tit=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")#, role="presentation")
        title=soup.find("h1",class_="TitleHeader__TitleText-sc-1wu6n3d-0")
        a=tit.find_all("li",class_="ipc-inline-list__item")
        s=0
        for i in a:
            if s==2:
                dict1["runtime"]=i.text

            s+=1
        a=tit.find("li",class_="ipc-inline-list__item")
        for j in ul:
            gg=[]
            if "Language" in j.text:
                li = j.find_all("li")
                for i in li:
                    if "Language" in i.text:
                        div = i.find("div")
                        a= div.find_all("a")
                        for lan in a:
                            gg.append(lan.get_text())
                        dict1["language"]=gg
                    if "Country" in i.text:
                        a=i.find("a")
                        dict1["Country"]=a.get_text()
                    if "Release" in i.text:
                        a=i.find("li")
                        dict1["year"]=a.text
        dict1["movie_name"]=soup.find('h1').text
        dict1["genre"]=soup.find("span",class_="ipc-chip__text").text
        dict1["director"]=soup.find("div",class_="ipc-metadata-list-item__content-container").text
        dict1["img_url"]='https://www.imdb.com/'+(soup.find("a",class_="ipc-lockup-overlay ipc-focusable")["href"][:-14])
        dict1["bio_title"]=soup.find("div",class_="GenresAndPlot__TextContainerBreakpointM-cum89p-2 iJnWgZ").text
        list1.append(dict1.copy())

        if c==1:
            break
        c+=1

    file=open("task4_data.json","w")
    json.dump(list1,file,indent=4)
    file.close()
    return dict1

task4 = scrape_movie_details(files)
# pprint(task4)







