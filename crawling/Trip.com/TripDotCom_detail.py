#!/usr/bin/env python
# coding: utf-8

# In[40]:


import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
def main(input_nation,input_city,input_detailcode,input_category,input_reviewcount):
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\Tripdotcom\\'+str(input_detailcode)+'.csv'):
        print(str(input_detailcode)+'은 이미 있는 상품')
        return
    url='https://www.trip.com/restapi/soa2/14580/getProductPriceCalendar'
    data={"head":{"syscode":"","lang":"","auth":"","ctok":"","cver":"","sid":"8888","extension":[],"pauth":"","sauth":"","appid":"100017626"},"clientInfo":{"crnVersion":"2019-12-11 18:49:57","platformId":24,"location":{"lat":"0.0","lon":"0.0","cityId":0,"locatedCityId":0},"locale":"ko-KR","currency":"CNY"},"id":input_detailcode,"productIds":[str(input_detailcode)],"sourcePageType":2}
    req = requests.post(url,data=json.dumps(data))
    if req.status_code/400 > 1:
        print(str(input_detailcode)+'은 '+str(req.status_code)+'에러')
        return
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    try:
        json_detail=json.loads(soup.text)
        title=json_detail['data']['basicInfo']['productName']
        for i in json_detail['data']['packageInfos']:
            option=i['packageName'].replace(title,'')
            for j in i['resourceInfos']:
                f = open('C:\\Users\\Mandy\\Desktop\\Tripdotcom\\'+str(input_detailcode)+'.csv', 'a',encoding='utf-8' ,newline='')
                wr = csv.writer(f)
                wr.writerow(['Tripdotcom', input_nation, input_city,input_detailcode
                                   , title,option[1:]+' '+j['resourceName']
                                    ,'https://kr.trip.com/things-to-do/detail/'+str(input_detailcode) , 'CNY'
                                     , j['minPrice'], input_reviewcount,input_category])
                print(str(input_detailcode)+'끝')
        f.close()
    except:
        print(str(input_detailcode)+'은 json불가')
   
            


# In[ ]:


