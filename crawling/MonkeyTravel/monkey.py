import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import openpyxl
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import chardet
def main(input_nation,input_city,input_category,link,input_title):
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\MonkeyTravel\\'+str(input_nation)+'\\'+str(input_title).replace('/','')+'.csv'):
        print(str(input_nation)+(input_title)+' 이미 있는 상품')
        return
    f = open('C:\\Users\\Mandy\\Desktop\\MonkeyTravel\\'+str(input_nation)+'\\'+str(input_title).replace('/','')+'.csv', 'a',encoding='utf-8' ,newline='')
    wr = csv.writer(f)
    url=link
    print(url)
    print(input_title+'진입')
    category=input_category
    nation=input_nation
    city=input_city
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    #############################업체명
    company=soup.find('div',attrs={'class':'business_info'})
    if company is None:
        company=''
    else:
        company=company.find('span').text
    #############################업체명    

    ##############################타이틀
    title=input_title
    ##############################타이틀

    ########################################리뷰
    review=soup.find('strong',attrs={'itemprop':'reviewCount'})
    review=review.text
    ########################################리뷰
    print(nation+' '+city+' '+category+' '+company+' '+url+' '+title+' '+review)
    tog=soup.find('div',attrs={'class':'pri_tog'}) #옵션 첫 한단락
    if tog is None:
        option='없음'
    else:
        tog=tog.find_all('tr',attrs={'class':'t_parent'})# 옵션 한 목록 ex_하룽크루즈 요일 성인 아동 유아
        for i in tog: #각각의 목록 돌면서 
            price_all=i.find_all('td',attrs={'class':'price_all ltsno ac'})
            wr.writerow(['Monkey Travel', nation, city, company
                           , title,url ,i.find('td').text,i.find('li').text,
                         price_all[0].text.strip(),price_all[1].text.strip(),price_all[2].text.strip()
                        ,  review ,category  ])
    f.close()        