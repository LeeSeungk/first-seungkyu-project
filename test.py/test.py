import csv
import requests 
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
f=open("시가총액top200.csv","w",encoding='utf-8',newline="")
writer = csv.writer(f)

title  = 'N 종목명 현재가 전일미 등락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER ROE 토론실'.split(' ')
writer.writerow(title)

data = []
for page in range(1,5) :
    response =requests.get(url+str(page)) #url 요청해서 해당 html을 return받기 
    soup = BeautifulSoup(response.content,"html.parser") #response를 soup객체로 파싱

    rows=soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    for row in rows :
        columns = row.find_all("td")
        if len(columns) <= 1 :
            continue #빈 columns를 skip
        for column in columns :
            data.append(column.get_text().strip()) #tab 지우기
            #csv 추가
        writer.writerow(data) #writerow(list) 추가
        print(data)
        data.clear()
f.close