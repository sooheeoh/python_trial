import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


search = input('검색어를 입력하세요. :')
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC={quote_plus(search)}'
# quote_plus 통해 입력하면 웹에서 지원하는 방식으로 변환되게 함

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
total = soup.select('.api_txt_lines.total_tit')

'''
for i in total:
    print(i.text)
    print(i.attrs['href']) # 아니 구글에서는 링크 가져오는 게 i.a.attrs 였잖아. 왜..? ㅠㅠ
    print()
목적은 이게 아니었다고 함
'''
searchList = []

for i in total:
    temp = []
    temp.append(i.text) # 제목 추가
    temp.append(i.attrs['href']) # 링크 추가
    searchList.append(temp) # !!!!

f = open(f'{search}.csv', 'w', encoding='CP949', newline='') # 검색어가 제목이 되는 마법, 뉴라인은 한줄추가 문제 해결됨
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()

print('완료!')
