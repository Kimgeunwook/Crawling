#!/usr/bin/env python
# coding: utf-8

# In[102]:


import requests
from bs4 import BeautifulSoup
import re
import csv
import xlsxwriter 
import openpyxl
import json
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
def main(input_country,input_code):
    
    total_item=list()
    city=input_country
    citycode=input_code#페이지수도 고치기
    dir_path='C:\\Users\\Mandy\\Desktop\\country\\TopRank\\'
    os.mkdir(dir_path+'/'+str(city)+'/')
    workbook = xlsxwriter.Workbook('C:\\Users\\Mandy\\Desktop\\country\\TopRank\\'+str(city)+'\\'+str(city)+'.xlsx') 
    worksheet = workbook.add_worksheet() 
    workbook.close() 
    write_wb=openpyxl.load_workbook('C:\\Users\\Mandy\\Desktop\\country\\TopRank\\'+str(city)+'\\'+str(city)+'.xlsx')#엑셀 파일 열기
    write_ws=write_wb.active
    url='https://www.tripadvisor.co.uk/Attractions-g'+str(citycode)+'-Activities-'+str(city)+'.html#FILTERED_LIST'
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    data = BeautifulSoup(req.content).find('script', text = re.compile('window.__WEB_CONTEXT__')).text
    data=data.replace('window.__WEB_CONTEXT__=','').replace('{pageManifest:', '{"pageManifest":')[:-175]
    pageManifest = json.loads(data)
    item_list=pageManifest['pageManifest']['redux']['api']['responses']['/data/1.0/attraction_overview/'+str(citycode)[1:]]['data']['topPOIs']['pois']
    last_page=pageManifest['pageManifest']['redux']['api']['responses']['/data/1.0/attraction_overview/'+str(citycode)[1:]]['data']['topPOIs']['paginationModel']['lastLink']['page']
    for i in item_list: #첫 페이지 특이 케이스
        if 'fromTicketPrice' in i.keys():
            price=i['fromTicketPrice'] # 가격
        else :
            price=''
        url='https://www.tripadvisor.co.uk/'+i['detailUrl'] #url
        total_item.append([str(city),i['categoryName'],i['name'],price,
                         str(i['numReviews']),url,i['productCount']])
    
    for j in range(1,last_page):
        print(j)
        url2='https://www.tripadvisor.co.uk/Attractions-g'+str(citycode)+'-Activities-oa'+str(30*j)
        req2 = requests.get(url2)
        html2 = req2.content
        soup2 = BeautifulSoup(html2,'lxml')
        item_list=soup2.find_all('div',attrs={'class':'attraction_element_tall'})
        for i in item_list:#카테고리 타이틀 price review
            category_list=i.find_all('span',attrs={'class':'matchedTag noTagImg'})
            category=''
            for k in category_list:
                category=str(category)+' '+str(k.text)
                
            title=i.find('div',attrs={'class':'tracking_attraction_title listing_title'}).text
            
            if i.find('span',attrs={'class':'price_from'}) is not None:
                price=i.find('span',attrs={'class':'price_from'}).text
            else:
                price=''
            
            if i.find('span',attrs={'class':'more'}) is not None:
                review=i.find('span',attrs={'class':'more'}).text   
            else:
                review=''
            
            if i.find('div',attrs={'class':'tracking_attraction_cta display_text ui_button primary fullwidth'}) is not None:
                see_string=i.find('div',attrs={'class':'tracking_attraction_cta display_text ui_button primary fullwidth'}).text.replace('\n','').split(' ')[1]
            else:
                see_string=''
                
            url='https://www.tripadvisor.co.uk/'+a_list[1]['href']#url
           
           
            total_item.append([str(city),category,title,
                              price,review.split(" ")[0],url,see_string])
    for item in total_item:
        write_ws.append(item)
    write_wb.save('C:\\Users\\Mandy\\Desktop\\country\\TopRank\\'+str(city)+'\\'+str(city)+'.xlsx')
    print('finish')    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




