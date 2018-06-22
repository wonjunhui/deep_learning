from bs4 import BeautifulSoup
import urllib.request
html = urllib.request.urlopen("http://nlotto.co.kr/gameResult.do?method=byWin")
# print(html)
soup = BeautifulSoup(html, "lxml")
# print(soup)
hoi = soup.find("h3", class_="result_title")
# print(hoi)
print(hoi.strong.string,"회")

numbers = []
p = soup.find("p", class_="number")
imgs = p.find_all('img')
# print(imgs)
for i in imgs :
    # print(i['alt'])
    numbers.append(i['alt'])

# print("당첨번호:",numbers)
bonus = numbers.pop(6)
print(" ".join(numbers))
print("보너스:",bonus)
# print(p