from bs4 import BeautifulSoup
import urllib.request
html = urllib.request.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# print(html)
soup = BeautifulSoup(html, "lxml")
table = soup.find("table", class_="list_ranking")
table_body = table.find('tbody')
rows = table_body.find_all('tr')

rank_list = soup.find_all("div","tit3")
# count = 1
# for i in rank_list:
#     title = i.find('a').contents[0]
#     print("{0:2d}위: {1}".format(count,title))
#     count = count + 1
    
# # print(rows)
# movies = []
# for row in rows:
#     try:
#         print(row.find('a')['title'])
#         movies.append(row.find('a')['title'])
#     except:
#         print("none")
# print(movies)


for idx, rank in enumerate(rank_list,1):
    title = rank.find('a').string
    print("{0:2d}위: {1}".format(idx,title))