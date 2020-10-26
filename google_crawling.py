from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)
# 한글은 인터넷에서 바로 사용하는 방식이 아니라, quote_plus가 변환해줌
# URL에 막 %CE%GD%EC 이런 거 만들어주는 친구

driver = webdriver.Chrome(executable_path= r'/Users/kimjoohee/Desktop/python_trial/chromedriver')
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

v = soup.select('.yuRUbf')
# print(type(v)) 강의에서는 list가 나오는데, 나는 bs4.element.ResultSet 나옴..

for i in v:
    print(i.select_one('.LC20lb.DKV0Md').text)
    print(i.select_one('.iUh30.gBIQub.qLRx3b.tjvcx').text)
    print(i.a.attrs['href'])
    print()

driver.close()

