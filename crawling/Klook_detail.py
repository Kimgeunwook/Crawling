#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import os.path
import urllib
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
def work(input_num):
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\Klook\\'+str(input_num)+'.csv'):
        print(str(input_num)+'은 이미 있는 상품')
        return
    num=input_num
    url='https://www.klook.com/ko/activity/'+str(num)
    cookie='klk_lang=ko; abtest_revamp=1579252233275; _pxvid=3794364d-3909-11ea-b154-0242ac120002; device_id_new=ryEGX8eZpJ00300000000000005L7iGrdXwD00502715765WpYWiKzBGCfRUhXyDN25S16Goh5Mk0045zgp4q8JSa00000qZkTE00000675NPgb7KNrq55xFbQfG:40::4a9c40ec717aafca; tag_fok=1579252233000; _ga=GA1.2.1554928380.1579252235; _gcl_aw=GCL.1579252235.EAIaIQobChMI4fbQgaWK5wIV1amWCh242AlnEAAYASAAEgIDQPD_BwE; _gcl_dc=GCL.1579252235.EAIaIQobChMI4fbQgaWK5wIV1amWCh242AlnEAAYASAAEgIDQPD_BwE; _gcl_au=1.1.1616812397.1579252235; __utmz=other; _gac_UA-86696233-1=1.1579252287.EAIaIQobChMI4fbQgaWK5wIV1amWCh242AlnEAAYASAAEgIDQPD_BwE; __pxvid=57fbed7b-3909-11ea-a0b6-0242ac110003; G_ENABLED_IDPS=google; CSRF-Token=MTU3OTQ4Mjc2NHxGY0V5WTNTV0JickNQcXA2TDNna19ZdTNrT25NRS0ySny0DslTQc9Z5hvsYhwWjkoDUoCFVYZJs2ISEqU_hBrT3g==; CSRF-Token-Valid=valid; _gid=GA1.2.662095178.1579482761; webp_support=1; retina_support=0; klk_currency=HKD; JSESSIONID=DFC4C31CAA9D8A3346EC1AEF5525BF7B; _gat_UA-86696233-1=1; mp_c2ca8b423fd75a10792debf44cd6b51a_mixpanel=%7B%22distinct_id%22%3A%20%2216fc08246f3b98-02a60c61864f9e-c383f64-1fa400-16fc08246f4924%22%2C%22%24device_id%22%3A%20%2216fc08246f3b98-02a60c61864f9e-c383f64-1fa400-16fc08246f4924%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22Language%22%3A%20%22ko%22%2C%22Platform%22%3A%20%22Web%22%2C%22Backend%20User%20Country%22%3A%20%22KR%22%2C%22Domain%22%3A%20%22www.klook.com%22%2C%22Login%20Status%22%3A%20false%2C%22Test-Pre-Activity-Phase2%22%3A%20%22variant1%22%2C%22__timers%22%3A%20%7B%7D%7D; _dc_gtm_UA-86696233-1=1; wcs_bt=s_2cb388a4aa34:1579502647; _pxff_ne=1; _px3=c869358ddfd625f43865b2b76f59d72af9921f2ef12efe6d7181a4ca7203f479:xC7tHq8lE4MlNAcjLL71rhXUoXlIWjI/vjm4hOKe6LyC8r8lST3m6FmZKRTwrYhgr+VbTwWoJde4rH74P5lghA==:1000:r/5DKEXhu4fl4Vjx2hUXIHj8MHM/5faTjfU+GA2ie2Ij0TsdluDZrWKNtQiou1oACqIVfFqr0nswnoolGTfbmhmSakbuwLy+KpKIPR7Nhds4MCFg7TZt0qXQ83Mp+sLco3onsfOHDGTKEjMPr2JP4uixphhUAXNdosYIavXPiNM='
    #user-agent,referer,accept-language,set-fetch-site,same-origin,cookie
    req = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                                    'referer':'https://www.daum.net','Accept-Language':'ko',
                                   'sec-fetch-site':'same-origin','cookie':cookie})
    
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    if req.status_code/400 > 1:
        print(str(input_num)+'은 '+str(req.status_code)+'에러')
        return
   
    
    title=soup.find('h1',attrs={'class':'act_title'}).text.strip()
    location_category=soup.find_all('a',attrs={'class':'f_h_main'})
    nation=''
    city=''
    if len(location_category)>42:
        nation=location_category[42].text
    if len(location_category)>43:    
        city=location_category[43].text
    category1=''
    category2=''
    if len(location_category)>44:
        category1=location_category[44].text
    if len(location_category)>45:
        category2=location_category[45].text
    review=''
    if soup.find('a',attrs={'class':'wifi_sim_act__span--star_num'}) is not None:
        review=soup.find('a',attrs={'class':'wifi_sim_act__span--star_num'}).text[6:-2].strip()
    if soup.find('button',attrs={'class':'g_row1 t16 m_btn_gray j_goto_pkg select_option_btn'})is not None:
        f = open('C:\\Users\\Mandy\\Desktop\\Klook\\'+str(input_num)+'.csv', 'a',encoding='utf-8' ,newline='')
        wr = csv.writer(f)
        wr.writerow(['Klook', nation, city,input_num
                           , title,''
                            , url, 'HKD'
                             , '', review,'현재 예약 불가',''])
        print(str(input_num)+'끝')
        f.close()
        return
    matched_product_id=re.findall(r'package_id":(.+?),',req.text,re.S) #product_id 가져오는것
    for p_id in matched_product_id:# pid하나하나 돌면서
        ########################################pid에 매칭되는 옵션얻기
        p_id_name_url='https://www.klook.com/xos_api/v1/usrcsrv/packages/'+str(p_id)+'/base/published'
        p_id_name_req = requests.get(p_id_name_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                                    'referer':'https://www.naver.com','Accept-Language':'ko'})
        p_id_name_json=json.loads(p_id_name_req.text)
        option=p_id_name_json['result'][0]['package_name'] 
        ########################################pid에 매칭되는 옵션얻기
        p_id_price_url='https://www.klook.com/xos_api/v1/usrcsrv/packages/'+str(p_id)+'/schedules_and_units'
        p_id_price_req = requests.get(p_id_price_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                                    'referer':'https://www.naver.com','Accept-Language':'ko'})
        p_id_price_json=json.loads(p_id_price_req.text)
        for item in p_id_price_json['result']['unit_info']['units']:
            price=item['selling_price']
            age_band=item['price_name']
            f = open('C:\\Users\\Mandy\\Desktop\\Klook\\'+str(input_num)+'.csv', 'a',encoding='utf-8' ,newline='')
            wr = csv.writer(f)
            wr.writerow(['Klook', nation, city,input_num
                           , title,str(option)+' '+str(age_band) 
                            , url, 'HKD'
                             , price, review,category1,category2])
    print(str(input_num)+'끝')
    f.close()   
def main():
    executor = ThreadPoolExecutor(50)      
    for i in range(1,35000):
        executor.submit(work, i) 
    executor.shutdown(wait=True)      
    print('finish')










