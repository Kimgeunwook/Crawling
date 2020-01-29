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
from . import monkey
import chardet

def main(input_nation,input_city,input_category,input_url):
    
    category=input_category
    for i in range(1,100):
        url=input_url+'&page='+str(i)
        req = requests.get(url)
        html = req.content
        soup = BeautifulSoup(html, 'lxml')
        item_list=soup.find_all('a',attrs={'class':'gaec_product'})
        for item in item_list: #상세페이지로 넘어가기
            title=item.find('em').text
            if input_nation=='베트남':
                link='https://vn.monkeytravel.com/'+item['href']
            elif input_nation=='태국':
                link='https://thai.monkeytravel.com/'+item['href']
            monkey.main(input_nation,input_city,category,link,title)
        if len(item_list)==0:
            break
   
