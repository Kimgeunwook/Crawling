import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
from . import TripDotCom_detail
def main(input_nation,input_city,input_citycode):
    executor = ThreadPoolExecutor(60)
    category=''
    category_dict={"jiaotongjiebo":"교통수단","cpktp":"교통수단","qcbsp":"교통수단",'jtkq':'교통수단',
                   "yiriyou":"데이 투어","riyou_new":"데이 투어","djzy_new":"데이 투어",
                   "wifi_new":"WiFi & 유심",
                   "jdmp":"명소 & 공연","ycp":"명소 & 공연",'zhanl':'명소 & 공연'
                   ,"tyss_new":"이색 체험","spasl":"스파"}
    url='https://kr.trip.com/restapi/soa2/14857/productSearch'
    for i in range(1,21):
        data={"head":{"syscode":"","lang":"","auth":"","cid":"","ctok":"","cver":"","sid":"","extension":[],"pauth":"","sauth":"","appid":"100016584"},"clientInfo":{"platformId":24,"version":"611.000","location":{"lat":"0.0","lon":"0.0","cityId":input_citycode,"locatedCityId":0},"extension":[{"name":"srhtraceid","value":"d1726d2a-8913-18c9-de01-157292093018"}],"locale":"ko-KR","currency":"CNY"},"productid":"0","searchParameter":{"searchType":1,"sortType":0,"searchKey":"-1","promotionIdList":[],"pageSetting":{"pageIndex":i,"pageSize":20},"categoryCode":"-1"}}
        req = requests.post(url,data=json.dumps(data))
        html = req.content
        soup = BeautifulSoup(html, 'lxml')
        citylist=json.loads(soup.text)['products']
        for i in citylist:
            category=''
            if i['currentCategoryCode'] in category_dict.keys():
                category=category_dict[i['currentCategoryCode']]
            else:
                category='기타'
            executor.submit(TripDotCom_detail.main,input_nation,input_city,i['productId'],category,i['commentCount'])
            #TripDotCom_detail.main(input_nation,input_city,i['productId'],category,i['commentCount'])#나라 도시 상품코드 카테고리 리뷰수
    executor.shutdown(wait=True)          