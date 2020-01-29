#!/usr/bin/env python
# coding: utf-8

# In[28]:


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
import os.path
import choice_page
import chardet
def main(input_country,input_nation,input_city,input_url):
    print('choice_category 진입')
    dir_path='C:\\Users\\Mandy\\Desktop\\MonkeyTravel'
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\MonkeyTravel\\'+str(input_nation)):
        print('')
    else:    
        os.mkdir(dir_path+'/'+input_nation+'/')
    url=input_url
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    category_list=soup.find('ul',attrs={'class':'tab_tour tabtour_inb'})
    category_list=category_list.find_all('li')
    category_l=list()
    for i in category_list:  #비고 list쭉 만들기
        category_l.append((i.text.split('(')[0],i.a['href']))

    for i in range (1,len(category_l)): #각 비고 리스트들 마다 상세페이지로 이동하는곳
        category=category_l[i][0]
        url_detail='https://'+input_country+'.monkeytravel.com/user/product/'+category_l[i][1]
        choice_page.main(input_nation,input_city,category,url_detail)
        
        


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




