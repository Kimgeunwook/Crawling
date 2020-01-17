from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from bs4 import BeautifulSoup
import re
import json
from pprint import pprint
import os.path

def task(input_url,input_num):#한페이지에서 하는일 써주는 함수
    #나중에 함수로 url밭으면 url=_url해주기
    url_detail ='https://www.tripadvisor.co.uk/'+input_url
    req_detail = requests.get(url_detail)
    html_detail = req_detail.content
    soup_detail = BeautifulSoup(html_detail, 'lxml')

    data=soup_detail.find('script',text=re.compile('window.__WEB_CONTEXT__')).text.replace('window.__WEB_CONTEXT__=','').replace('{pageManifest:', '{"pageManifest":')[:-2]
    ############################################리뷰수 정규식으로 찾는부분
    matched_review = re.search(r'reviewCount":(.+?),"reviewRating"', data, re.S) 
    review_array = matched_review.group()
    review = review_array.split('"')[1][1:][:-1]
    ############################################

    ############################################상품명 정규식으로 찾는부분
    matched_title = re.search(r'productTitle":"(.+?)","productTitleMobile', data, re.S)
    title_array = matched_title.group()
    title = title_array.split('"')[2]
    ############################################

    ############################################도시명 정규식으로 찾는부분
    matched_city = re.search(r'location_string":"(.+?)","awards"', data, re.S)
    city_array = matched_city.group()
    city = city_array.split('"')[2].split(',')[-1].strip()
    ############################################

    ############################################업체명 정규식으로 찾는부분
    matched_company = re.search(r'supplierName":"(.+?)","supplierUrl', data, re.S)
    company_array = matched_company.group()
    company = company_array.split('"')[2]
    ############################################

    ############################################비고 찾는 부분
    category=soup.find('ul',attrs={'class':'breadcrumbs'}).text.split('\xa0')[-1]
    ############################################
    print(str(input_num)+company)
    f = open('C:\\Users\\Mandy\\Desktop\\TripAdvisor\\info' + str(input_num) + '.csv', 'w',encoding='utf-8' ,newline='')
    wr = csv.writer(f)
    wr.writerow(['TripAdvisor', '베트남', city, company,''  # all에추가
                                            , title, ''
                                            , url_detail, 'KRW'
                                            , ''
                                            , review, category])
    f.close()
    
    
    
executor = ThreadPoolExecutor(30) #한 페이지에 상품 30개 멀쓰 돌릴거니까 30
countt=0
for i in range(1, 5): #페이지 몇개있을줄 모르니까 넉넉하게 1000개잡고
    countt=(i-1)*30
    print(str(i)+'진입'+str(countt))
    ################################################1페이지인지 2페이지이상인지에 따라url_page설정
    if i==1:
        url_page='https://www.tripadvisor.co.uk/Attraction_Products-g293921-a_sort.-Vietnam.html#ATTRACTION_LIST'
    else:
        url_page='https://www.tripadvisor.co.uk/Attraction_Products-g293921-oa'+str(30*(i-1))+'-a_sort.-Vietnam.html#ATTRACTION_LIST'
   
    req = requests.get(url_page) 
    html = req.content
    soup = BeautifulSoup(html, 'lxml') 
    
    #페이지에 상품 있는지 없는지 체크
    product_exist=soup.find('div',attrs={'id':'ATTRACTION_PRODUCTS_LIST'}) 
    if product_exist is None:
        print(str(i)+'페이지부터 상품 없음')
        break
    ################################################
    
    #############################################url30개 얻어오기 (product_list)
    req = requests.get(url_page)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')  
    product_url_list=list()
    for i in soup.find_all('div',attrs={'class':'attraction_clarity_cell'}):
        tag_a=i.find('a')
        product_url_list.append(tag_a.attrs['href'])
    #############################################
   
    for j in range(0,30): #한페이지에 상품 개수만큼
        executor.submit(task, product_url_list[j],countt+j) #스레드에 product_list0~29번 차레대로 넣어주기
           
executor.shutdown(wait=True)    
print('finish')