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
        print(text)       
        

        for key, value in all_dictionary["movieInfoResult"]["movieInfo"].items(): 
            dic = {}
        
            dic["movieCd"] = movieCds
            dic["movieNm"] = all_dictionary["movieInfoResult"]["movieInfo"]["movieNm"]
            dic["movieNmEn"] = all_dictionary["movieInfoResult"]["movieInfo"]["movieNmEn"]
            dic["movieNmOg"] = all_dictionary["movieInfoResult"]["movieInfo"]["movieNmOg"]
            dic["openDt"] = all_dictionary["movieInfoResult"]["movieInfo"]["openDt"]
            dic["showTm"] = all_dictionary["movieInfoResult"]["movieInfo"]["showTm"]

            dic["genres"] = all_dictionary["movieInfoResult"]["movieInfo"]["genres"][0]["genreNm"]
            dic["directors"] = all_dictionary["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]
            dic["audits"] = all_dictionary["movieInfoResult"]["movieInfo"]["audits"][1]["watchGradeNm"]

            if not all_dictionary["movieInfoResult"]["movieInfo"]["actors"]:
                for i in range(1, 4):
                    dic[f"actors{i}"] = " "
            if len(all_dictionary["movieInfoResult"]["movieInfo"]["actors"]) == 1:
                dic['actors1'] = all_dictionary["movieInfoResult"]["movieInfo"]["actors"][0]["peopleNm"]
                for i in range(2, 4):
                    dic[f"actors{i}"] = " "
            if len(all_dictionary["movieInfoResult"]["movieInfo"]["actors"]) == 2:
                for i in range(1, 3):
                    dic[f"actors{i}"] = all_dictionary["movieInfoResult"]["movieInfo"]["actors"][i-1]["peopleNm"]
                    dic[f"actors{3}"] = " "                    
            
            all_list.append(dic) 

with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'openDt', 'showTm', 'genres', 'directors', 'audits', 'actors1', 'actors2', 'actors3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in all_list:        
        writer.writerow({'movieCd': i["movieCd"], 'movieNm': i["movieNm"], 'movieNmOg': i["movieNmOg"], 'openDt': i["openDt"], 'showTm': i["showTm"],
                        'genres': i["genres"], 'directors': i["directors"], 'audits': i["audits"], 'actors1': i["actors1"], 'actors2': i["actors2"], 'actors3': i["actors3"],   })
       
with open('movie.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movieCd'], row['movieNm'], row['movieNmOg'], row['openDt'], row['showTm'], row['genres'], row['directors'], row['audits'], 
              row['actors1'], row['actors2'], row['actors3'] ) 



            
           






     