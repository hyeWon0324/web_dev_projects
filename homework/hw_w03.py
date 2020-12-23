import requests
import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

base_url = "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd="

today = datetime.date.today()   #예: 20200713
ymd = today.strftime("%Y%m%d")  # %Y (year full version) %m (month as a number 01-12) %d (day of month)
url = base_url + ymd

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

top200Songs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")


rank = 0
for song in top200Songs:
    #number_tag = song.select_one("td.number").text.strip()
    rank += 1
    td_tag = song.select_one("td.info")
    title = td_tag.select_one("a.title.ellipsis").text.strip()
    artist = td_tag.select_one("a.artist.ellipsis").text.strip()

    print(rank, end=": ")
    print(title, end=" ---- ")
    print(artist)

    #mongoDB 에 저장
    doc = {'rank': rank, 'title': title, 'artist': artist}
    db.musicchart.insert_one(doc)



