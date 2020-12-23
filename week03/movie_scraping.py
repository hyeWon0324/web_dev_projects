import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
movies = soup.select("#old_content > table > tbody > tr") #리스트 형태로 반환
# 순위 , 영화명, 평점, 변동폭

#rank = 0
# for i in range(0, len(movies)):
#     a_tag = movies[i].select_one('td.title > div > a')       #한 요소만 가져옴
#     if a_tag is not None:
#         rank += 1
#         print(rank, end=": ")
#         print(a_tag.text)
#     else:
#         #rank를 올리지 않는다
#         pass

for movie in movies:
    a_tag = movie.select_one('td.title > div > a')       #한 요소만 가져옴
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        point = movie.select_one('td.point').text
        print(rank, end=": ")
        print(title, end=" ----- ")
        print(point)



#############################