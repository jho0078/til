import requests
from bs4 import BeautifulSoup
url = 'http://www.op.gg/summoner/userName='
username = 'hide on bush'
response = requests.get(url+username).text
soup = BeautifulSoup(response, 'html.parser')
wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
# 태그를 제외한 값만 뽑아오기 위해서 .text 사용
print(wins.text)
print(loses.text)