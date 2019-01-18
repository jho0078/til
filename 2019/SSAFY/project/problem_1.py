import requests
import json
import csv
import os
import datetime


token = os.getenv("token")
today = datetime.datetime(2019, 1, 13)
movie_list = []
all_list =[]
for i in range(10):
    new_today = today - datetime.timedelta(weeks=i)    
    new_today_string = new_today.strftime('%Y%m%d')

    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={new_today_string}&weekGb=0'
    res = requests.get(url)
    text = res.text
    all_dictionary = json.loads(text)  

          
    for movie_dic in all_dictionary["boxOfficeResult"]["weeklyBoxOfficeList"]: 
        dic = {}
        movie_list.append(movie_dic["movieNm"])
              
        if movie_list.count(movie_dic["movieNm"]) > 1:           
            continue

        dic['movieCd'] = movie_dic["movieCd"]
        dic['movieNm'] = movie_dic["movieNm"]
        dic['audiAcc'] = movie_dic["audiAcc"]
        dic['date'] = new_today_string
        all_list.append(dic)

with open('boxoﬃce.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movieCd', 'movieNm', 'audiAcc', 'date')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in all_list:        
        writer.writerow({'movieCd': i["movieCd"], 'movieNm': i["movieNm"], 'audiAcc': i["audiAcc"], 'date': i["date"]})
       
with open('boxoﬃce.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movieCd'], row['movieNm'], row['audiAcc'], row['date']) 