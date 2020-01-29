#!/usr/bin/env python
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import csv
import json
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from . import TripDotCom_citylist_to_detail
def main():
    urll='https://www.trip.com/restapi/soa2/14857/destinationCountryCities'
    data={"head":{"vid":"1579567387348.2kjdro","union":{"sid":"1621818","aid":"14887","ouid":"ctag.hash.c482de2c5d2d"},"url":"https://kr.trip.com/things-to-do/","referrer":"https://kr.trip.com/things-to-do/list?searchtype=1&cityid=4896","language":"ko-KR","currency":"CNY","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36","cookie":"_tp_search_latest_channel_name=hotels; _gid=GA1.2.732865174.1579567388; _ga=GA1.2.2085391719.1579567388; _gcl_au=1.1.878208001.1579567389; _RF1=58.151.93.98; _RSG=.7ardRBy.JFCIvp4JmcPbA; _RDG=289bbe456313132bdb39257bb3dd285aab; _RGUID=f4fef0b6-e7d6-41fe-a959-9b04c4cf948c; __utmz=1.1579567427.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gac_UA-109672825-1=1.1579567388.EAIaIQobChMIrLzKiLuT5wIVSKqWCh2itASKEAAYASAAEgLXX_D_BwE; ibu_h5_site=KR; ibu_h5_group=trip; ibu_h5_local=ko-kr; ibu_h5_lang=kr; ibu_h5_curr=KRW; download-banner-hide=download-banner-hide; _gcl_aw=GCL.1579573145.EAIaIQobChMI772KwtCT5wIVDXZgCh32mgj9EAAYASAAEgJfoPD_BwE; _gcl_dc=GCL.1579573145.EAIaIQobChMI772KwtCT5wIVDXZgCh32mgj9EAAYASAAEgJfoPD_BwE; _gac_UA-109672825-3=1.1579573145.EAIaIQobChMI772KwtCT5wIVDXZgCh32mgj9EAAYASAAEgJfoPD_BwE; Union=AllianceID=14887&SID=1621818&OUID=ctag.hash.c482de2c5d2d&SourceID=&AppID=&OpenID=&Expires=1582165149276&createtime=1579573149; _gac_UA-109672825-1=1.1579567388.EAIaIQobChMIrLzKiLuT5wIVSKqWCh2itASKEAAYASAAEgLXX_D_BwE; GUID=09031144311852167072; ibu_online_home_language_match={\"isFromTWNotZh\":false,\"isFromIPRedirect\":false,\"isFromLastVisited\":false,\"isRedirect\":true,\"isShowSuggestion\":false,\"lastVisited\":\"http://uk.trip.com?locale=en-gb\"}; ibulocale=ko_kr; cookiePricesDisplayed=CNY; __utmc=1; __utma=1.2085391719.1579567388.1579591716.1579653622.4; __utmt=1; _gat=1; _gat_UA-109672825-3=1; _bfs=1.130; _bfa=1.1579567387348.2kjdro.1.1579591715041.1579653619298.4.418; __utmb=1.119.10.1579653622; _bfi=p1%3D10650014881%26p2%3D10650012671%26v1%3D418%26v2%3D417; ibulanguage=KR","width":1920,"height":1080,"innerHeight":969,"offset":{"height":2897,"width":967},"platform":"Online","enviroment":"PROD","channel":"trip","log_version":"2019-12-11 18:49:57","syscode":"09","pageId":"10650014881","netState":"4G","randomId":5},"clientInfo":{"platformId":26,"version":"608.000","currency":"CNY","locale":"ko-KR"}}
    req = requests.post(urll,data=json.dumps(data))
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    nation_list=json.loads(soup.text)['destinationCountries']
    
    for i in nation_list:
        if not i['country']['countryName']=='인기 여행지':
            for j in i['cities']:
                TripDotCom_citylist_to_detail.main(i['country']['countryName'],j['cityName'],j['cityId'])
            


# In[ ]: