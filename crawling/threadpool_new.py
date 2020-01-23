#!/usr/bin/env python
# coding: utf-8

# In[3]:


from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from bs4 import BeautifulSoup
import re
import json
from pprint import pprint
import os.path
def task(num):
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\threadpool5\\info' + str(num) + '.csv'):
        print(str(num)+'은 이미 존재')
    else:
        url = 'https://www.myrealtrip.com/offers/' + str(num)
        req = requests.get(url)
        html = req.content
        soup = BeautifulSoup(html, 'lxml')
        page_source = req.text  # 정규식 쓰기위한 텍스트 가져오기
        matched = re.search(r'"name"(.+?),"description"', page_source, re.S)  # 정규식으로 업체명 부분 짤라오려고 이렇게
        f = open('C:\\Users\\Mandy\\Desktop\\threadpool5\\available' + str(num) + '.csv', 'w',encoding='utf-8' ,newline='')
        wr = csv.writer(f)
        f2 = open('C:\\Users\\Mandy\\Desktop\\threadpool5\\info' + str(num) + '.csv', 'w',encoding='utf-8', newline='')
        wr2 = csv.writer(f2)
        if matched is None:  # 없는페이지 패스
            wr.writerow([num, "NO"])
            print(str(num)+'은 없는페이지')
        else:  # 페이지가 있으면
            print(str(num)+'은 있는페이지')
            title = soup.find('b')  # 타이틀 찾기
            price = soup.find('meta', attrs={'itemprop': 'price'})  # 가격 찾기
            review = soup.find('meta', attrs={'itemprop': 'ratingCount'})  # 후기수
            location = soup.find('meta', attrs={'itemprop': 'category'})  # 지역
            location = location.get('content').split()  # 지역을 나라+도시로 바꾸기 위해
            nation = location[0]  # 나라
            city = location[2]  # 도시
            # 비고 찾기
            mark = soup.find_all('script', attrs={'js-react-on-rails-component'})  # 비고 전체 찾기
            mark_text = json.loads(mark[1].text)
            mark_2 = '없음'  # 비고 2,3의 디폴트는 없음
            mark_3 = '없음'
            mark_list = list()
            for i in mark_text["offerInfo"]["tag_list"]:
                mark_list.append(i)
            if len(mark_list) == 1:
                mark_2 = mark_list[0]
            elif len(mark_list) == 2:
                mark_2 = mark_list[0]
                mark_3 = mark_list[1]
            # 비고 찾기
            # 업체명 가져오는 부분
            company = matched.group()
            company = company.split('"')
            # 업체명 가져오는 부분
            ######################날짜 가져오기
            url_date = ('https://www.myrealtrip.com/offers/'+str(num)+'/occupied_dates?start_date=2020-01-01&end_date=2021-01-01')  # str(v["key"])가 키값 가져오는거
            page_date = requests.get(url_date)
            d_date=json.loads(page_date.text)
            breaker=False
            for days in range(1,30):
                if breaker==True:
                    break
                for months in range(1,13):
                    if months==1 and days<9:
                        continue
                    if '2020-'+("{:02d}".format(months))+'-'+("{:02d}".format(days))+'' not in d_date["dates"]:
                        month=months
                        day=days
                        print(month)
                        print(day)
                        breaker=True
                        break
#             ######################날짜 가져오기
            url_getkey = 'https://www.myrealtrip.com/offers/' + str(num) + '/options?begin_at=2020-'+("{:02d}".format(month))+'-'+("{:02d}".format(day))+''  # 키 가져올때 참고할url
            #url_getkey = 'https://www.myrealtrip.com/offers/' + str(num) + '/options?begin_at=2020-04-08'  # 키 가져올때 참고할url
            page_source = requests.get(url_getkey).text
            d = json.loads(page_source)
            ###################################################
            if 'option_set' not in d:  # 옵션 안나오는거
                print(str(num)+'옵션 안나옴')
                if review is None:  # 후기 이벤트경우
                    wr.writerow([num, "YES",'후기 이벤트','옵션 없음'])
                    wr2.writerow(['마이리얼트립', nation, city, company[3], str(num)  # all에추가
                                        , title.text, '없음'
                                        , url, 'KRW'
                                        , price.get('content')
                                        , '후기 이벤트(나오지 않음)', mark_text["offerInfo"]["category"], mark_2, mark_3])
                else:  # 후기수 있는경우
                    wr.writerow([num, "YES", '후기수 있음', '옵션 없음'])
                    wr2.writerow(['마이리얼트립', nation, city, company[3], str(num)  # all에추가
                                        , title.text, '없음'
                                        , url, 'KRW'
                                        , price.get('content')
                                        , review.get('content'), mark_text["offerInfo"]["category"], mark_2, mark_3])
            ####################################################
            else:  # 옵션 나오는거
                print(str(num)+'옵션 나옴')
                for v in d["option_set"]["options"]:
                    url_getoptionprice = ('https://www.myrealtrip.com/offers/' + str(num) + '/check_option?choice_'
                                          + 'set[begin_at]=2020-'+("{:02d}".format(month))+'-'+("{:02d}".format(day))+'&choice_set[choices][][key]='  #
                                          + str(v["key"]) + '&choice_set[choices][][travelers]=1')
                    page_source2 = requests.get(url_getoptionprice).text
                    d2 = json.loads(page_source2)
                    ############################
                    if 'choice_set' not in d2:  # 옵션 선택했을때 이상하게 뜨는애들 ex)8179
                        wr.writerow([num, "YES", '후기수 있음', '옵션 없음'])
                        break
                    ############################
                    if review is None:  # 후기 이벤트경우
                        wr.writerow([num, "YES", '후기 이벤트', '옵션 있음'])
                        print(str(num)+'wr2쓰기전')
                        wr2.writerow(['마이리얼트립', nation, city, company[3], str(num)  # all에추가
                                            , title.text, str(d2["choice_set"]["choices"][0]["option"]["title"])
                                            , url, str(d2["choice_set"]["choices"][0]["price"]["currency_code"])
                                            , str(d2["choice_set"]["choices"][0]["price"]["amount"])
                                            , '후기 이벤트(나오지 않음)', mark_text["offerInfo"]["category"], mark_2, mark_3])
                        print(str(num)+'wr2쓰기후')
                    else:  # 후기수 있는경우
                        wr.writerow([num, "YES", '후기수 있음', '옵션 있음'])
                        wr2.writerow(['마이리얼트립', nation, city, company[3], str(num)  # all에추가
                                            , title.text, str(d2["choice_set"]["choices"][0]["option"]["title"])
                                            , url, str(d2["choice_set"]["choices"][0]["price"]["currency_code"])
                                            , str(d2["choice_set"]["choices"][0]["price"]["amount"])
                                            , review.get('content'), mark_text["offerInfo"]["category"], mark_2, mark_3])
        print(str(num)+'클로즈')
        f.close()
        f2.close()
                              
executor = ThreadPoolExecutor(100)
for i in range(0, 14000):
    future = executor.submit(task, i)
executor.shutdown(wait=True)    
print('finish')


# In[ ]:





# In[ ]:





# In[ ]:




