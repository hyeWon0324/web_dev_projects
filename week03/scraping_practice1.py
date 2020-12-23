import requests
import datetime
from bs4 import BeautifulSoup

base_url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date="

today = datetime.date.today()   #예: 20200713
ymd = today.strftime("%Y%m%d")  # %Y (year full version) %m (month as a number 01-12) %d (day of month)
url = base_url + ymd

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    title_tag = movie.select_one('td.title > div > a')
    if title_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = title_tag.text
        print(rank, title)