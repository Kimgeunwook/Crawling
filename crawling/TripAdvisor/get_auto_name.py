#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from bs4 import BeautifulSoup
import re
import os
import json
from pprint import pprint
import os.path
def main(input_string):
    url_country='https://www.tripadvisor.co.uk/TypeAheadJson?action=API&types=geo&name_depth=1&details=true&legacy_format=true&rescue=true&max=8&uiOrigin=Home_geopicker&source=Home_geopicker&searchSessionId=F006E6198C9CA5D9A05BD88C0457795D1578988735242ssid&scope=1&beforeGeoId=1&afterGeoId=1&startTime=1578988963492'
    data={'query':input_string}
    req_country = requests.get(url_country,params=data)
    html_country = req_country.content
    soup_country = BeautifulSoup(html_country, 'lxml')
    json_country=json.loads(soup_country.text)
    for i in range(0,len(json_country)-1):
        print(str(i+1)+'. '+json_country[i]["details"]["name"])
    choice=input('몇번 나라(도시)인가요? :')
    choice_country=json_country[int(choice)-1]["url"].split('-')[1]
    return (json_country[int(choice)-1]["details"]["name"],choice_country)

