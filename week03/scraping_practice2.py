import requests
import datetime
from bs4 import BeautifulSoup

base_url = "https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo"


# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(base_url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

teams = soup.select("#regularTeamRecordList_table > tr")

for team in teams:
    win_rate = team.select_one('td:nth-child(7) > strong').text
    if float(win_rate) >= 0.5:
        rank = team.select_one('th > strong').text
        team_name = team.select_one('td.tm > div > span').text
        print(rank, team_name, win_rate)

#  th > strong

# td.tm > div.team_NC