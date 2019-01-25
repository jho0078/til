import requests
import json
import csv
import os

token = os.getenv("token")
all_list = []
with open('boxoﬃce.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movieCds = row['movieCd']               
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={movieCds}'
        res = requests.get(url)
        text = res.text 
        all_dictionary = json.loads(text)               
        
        movieinfo_dic = all_dictionary["movieInfoResult"]["movieInfo"]        
        dic = {}
        
        dic["movieCd"] = movieCds
        dic["movieNm"] = movieinfo_dic["movieNm"]
        dic["movieNmEn"] = movieinfo_dic["movieNmEn"]
        dic["movieNmOg"] = movieinfo_dic["movieNmOg"]
        dic["openDt"] = movieinfo_dic["openDt"]
        dic["showTm"] = movieinfo_dic["showTm"]
        dic["genres"] = movieinfo_dic["genres"][0]["genreNm"]
        dic["directors"] = movieinfo_dic["directors"][0]["peopleNm"]
        dic["audits"] = movieinfo_dic["audits"][0]["watchGradeNm"]       

        actor_list = movieinfo_dic["actors"]
        a = len(actor_list)  
        
        for i in range(1, a+1):
            dic[f"actors{i}"] = movieinfo_dic["actors"][i-1]["peopleNm"]
        for j in range(a+1, 4):
            dic[f"actors{j}"] = ""        
          
        all_list.append(dic) 

with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'openDt', 'showTm', 'genres', 'directors', 'audits', 'actors1', 'actors2', 'actors3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in all_list:        
        writer.writerow({'movieCd': i["movieCd"], 'movieNm': i["movieNm"], 'movieNmEn': i["movieNmEn"], 'movieNmOg': i["movieNmOg"], 
                         'openDt': i["openDt"], 'showTm': i["showTm"], 'genres': i["genres"], 'directors': i["directors"], 
                         'audits': i["audits"], 'actors1': i["actors1"], 'actors2': i["actors2"], 'actors3': i["actors3"],})
       
with open('movie.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movieCd'], row['movieNm'], row["movieNmEn"], row['movieNmOg'], row['openDt'], row['showTm'], row['genres'], 
              row['directors'], row['audits'], row['actors1'], row['actors2'], row['actors3']) 



            
           






     