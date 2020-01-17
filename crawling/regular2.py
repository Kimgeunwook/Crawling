from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from bs4 import BeautifulSoup
import re
import os
import json
from pprint import pprint
import os.path
def task(input_url,input_num,Pid,input_category,input_string):#한페이지에서 하는일 써주는 함수
    h=input_url.split('.')
    h=h[0][1:]
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\TripAdvisor2\\'+str(input_string)+'\\' + h + '.csv'):
        print('이미있는상품')
        ############################
        f = open('C:\\Users\\Mandy\\Desktop\\TripAdvisor2\\'+str(input_string)+'\\' + h + '.csv', 'r',encoding='utf-8' ,newline='')
        rdr=csv.reader(f)
        lines=[]
        for line in rdr:
            lines.append(line)
        for line in lines:
            line.append(input_category)

        f.close()  
        os.remove('C:\\Users\\Mandy\\Desktop\\TripAdvisor2\\' +str(input_string)+'\\'+ h + '.csv')
        f2 = open('C:\\Users\\Mandy\\Desktop\\TripAdvisor2\\' +str(input_string)+'\\'+ h + '.csv', 'a',encoding='utf-8' ,newline='')
        wr = csv.writer(f2)
        for a in lines:
            wr.writerow(a)    
        f2.close()
        ############################
        return
#     print(str(input_num+1)+'은'+str(input_url)+'또'+str(Pid))    
    while True:
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
        if matched_company is None:
            company='업체 없음'
        else:
            company_array = matched_company.group()
            company = company_array.split('"')[2]
        ############################################
        ############################################비고 찾는 부분
        
        ############################################
        #################################################가능날짜찾는부분
        url_date ='https://www.tripadvisor.co.uk/AttractionBookingApi/product/'+str(Pid)+'/dates'
        req_date = requests.get(url_date)
        html_date = req_date.content
        soup_date = BeautifulSoup(html_date, 'lxml')
        date_all=json.loads(soup_date.text)
        date_list=list(date_all["data"].keys())
        dates=str(date_list[0]+'-'+date_all["data"][date_list[0]][0])
        
        #################################################가능날짜찾는부분
        #####################################################loactionid찾는거 (url은 함수에서 인풋받는거로 체인지)
        matched_loactionid = re.search(r'/AttractionProductReview-g(.+?)-', input_url, re.S)
        loactionid_array = matched_loactionid.group()
        location_id=loactionid_array.split('-')[1][1:]
        
        #####################################################loactionid찾는거 (url은 함수에서 인풋받는거로 체인지)
        ####################################age밴드 세는거 url 상세페이지 url로 고치기+변수이름도
        agebandid_count=soup_detail.text.count('ageBandId')/2
        s_ageband=''
        for c in range(1,int(agebandid_count)+1):
           s_ageband=str(str(s_ageband)+str(c)+':'+str(1)+',')
        s_ageband=s_ageband[:-1]
        ####################################age밴드 세는거 url 상세페이지 url로 고치기
        #####################################옵션 찾기 url은 빡시게 고치기
        url_option=('https://www.tripadvisor.co.uk/AttractionBookingApi/product/'+str(Pid)+
        '/tour_grades?tourDate='+str(dates)+'&attrdate='+str(dates)+'&ageBands='+str(s_ageband)+
        '&locationId='+str(location_id))
        req_option = requests.get(url_option)
        html_option = req_option.content
        options=json.loads(html_option)
        error_count=str(html_option)
        #####################################예외사항 고치는곳
        if error_count.count('this activity does not allow any')==1:
            url_option=('https://www.tripadvisor.co.uk/AttractionBookingApi/product/'+str(Pid)+
            '/tour_grades?tourDate='+str(dates)+'&attrdate='+str(dates)+'&ageBands=1:1&locationId='+str(location_id))
        elif error_count.count('sorry, this activity requires between 2')==1:
            url_option=('https://www.tripadvisor.co.uk/AttractionBookingApi/product/'+str(Pid)+
            '/tour_grades?tourDate='+str(dates)+'&attrdate='+str(dates)+'&ageBands=1:2&locationId='+str(location_id))
        elif error_count.count('sorry, this activity is limited to 2')==1:
            url_option=('https://www.tripadvisor.co.uk/AttractionBookingApi/product/'+str(Pid)+
            '/tour_grades?tourDate='+str(dates)+'&attrdate='+str(dates)+'&ageBands=1:1&locationId='+str(location_id))
        req_option = requests.get(url_option)
        html_option = req_option.content
        options=json.loads(html_option)
        
        #####################################예외사항 고치는곳    
        if str(options["polling_state"])==str('NO_LONGER_AVAILABLE'):
            print(str(input_num)+'은 사용불가')
            break
        if str(options["polling_state"])==str('COMPLETE'):
            for u in options["tour_grades"]:
                for t in u["age_bands"]:
                  #  +str(t["band_summary"]))
                    f = open('C:\\Users\\Mandy\\Desktop\\TripAdvisor2\\' +str(input_string)+'\\'+h + '.csv', 'a',encoding='utf-8' ,newline='')
                    wr = csv.writer(f)
                    #print(str(t["band_summary"].split('')[3][1:]))
                    wr.writerow(['TripAdvisor', input_string, city, company,input_num
                           , title,str(str(u["grade_title"])+'  '+t["band_summary"].split(" ")[0]+t["band_summary"].split(" ")[1]) 
                            , url_detail, 'KRW'
                             , t["band_summary"].split(" ")[3][1:]
                             , review, input_category])
            print(str(input_num+1)+'끝')
            f.close()
            break
        else:
            continue
            
            
            
            

def detail_main(input_url,input_category,input_string):
    countt=0
    for i in range(1,1000): #페이지 몇개있을줄 모르니까 넉넉하게 1000개잡고
        countt=(i-1)*30
        print(str(i)+'진입'+str(countt))
        ################################################1페이지인지 2페이지이상인지에 따라url_page설정
        if i==1:
            url_page='https://www.tripadvisor.co.uk'+input_url
        else:
            url_split=input_url
            url_split=url_split.split('-') #['/Attraction_Products', 'g293921', 'zfg12024', 'Vietnam.html']
            #'https://www.tripadvisor.co.uk/Attraction_Products-g293921-oa60-a_sort.-zfg11865-Vietnam.html#ATTRACTION_LIST
            #url_page='https://www.tripadvisor.co.uk/Attraction_Products-g189512-oa'+str(30*(i-1))+'-a_sort.-Denmark.html#ATTRACTION_LIST'
            url_page='https://www.tripadvisor.co.uk'+url_split[0]+'-'+url_split[1]+'-oa'+str(30*(i-1))+'-a_sort.-'+url_split[2]+'-'+url_split[3]+'#ATTRACTION_LIST'
        req = requests.get(url_page)
        html = req.content
        soup = BeautifulSoup(html, 'lxml')
        #페이지에 상품 있는지 없는지 체크
        product_exist=soup.find('div',attrs={'id':'ATTRACTION_PRODUCTS_LIST'})
        if product_exist is None:
            print(str(i)+'페이지부터 상품 없음')
            break
        #페이지에 상품 있는지 없는지 체크
        ################################################1페이지인지 2페이지이상인지에 따라url_page설정
        #############################################url30개 얻어오기 (product_list)
        product_url_list=list()
        for i in soup.find_all('div',attrs={'class':'attraction_clarity_cell'}):
            tag_a=i.find('a')
            product_url_list.append(tag_a.attrs['href'])
        #############################################url30개 얻어오기 (product_list)
        ##################################프로덕트 아이디 찾는부분
        product_id=soup.find_all('div',attrs={'class':'listing_title'})
        ##################################프로덕트 아이디 찾는부분
        for j in range(0,len(product_id)): #한페이지에 상품 개수만큼
            matched_code = re.search(r'trackCancelLabel(.+?),',str(product_id[j]), re.S)
            code_array = matched_code.group()
            productid=code_array.split('\'')[1]            
            executor.submit(task, product_url_list[j],countt+j,productid,input_category,input_string) #스레드에 product_list0~29번 차레대로 넣어주기

executor = ThreadPoolExecutor(60)              
def Ta_main(input_string):
    print('ta-main 호출')
    ######################################
    #######################################
    url_country='https://www.tripadvisor.co.uk/TypeAheadJson?action=API&types=geo&name_depth=1&details=true&legacy_format=true&rescue=true&max=8&uiOrigin=Home_geopicker&source=Home_geopicker&searchSessionId=F006E6198C9CA5D9A05BD88C0457795D1578988735242ssid&scope=1&beforeGeoId=1&afterGeoId=1&startTime=1578988963492'
    data={'query':input_string}

    req_country = requests.get(url_country,params=data)
    html_country = req_country.content
    soup_country = BeautifulSoup(html_country, 'lxml')
    json_country=json.loads(soup_country.text)
    for i in range(0,len(json_country)-1):
        print(str(i+1)+'. '+json_country[i]["details"]["name"])
    choice=input('몇번 나라인가요? :')
    choice_country=json_country[int(choice)-1]["url"].split('-')[1]
    dir_path='C:\\Users\\Mandy\\Desktop\\TripAdvisor2'
    os.mkdir(dir_path+'/'+choice_country+'/')
    #######################################
    main_url='https://www.tripadvisor.co.uk/Attraction_Products-'+choice_country
    main_req = requests.get(main_url)
    main_html = main_req.content
    main_soup = BeautifulSoup(main_html, 'lxml')

    category_group=main_soup.find('div',attrs={'class':'filter_list_0'})
    category_group=category_group.find_all('a')
    
    for category_url in category_group:
        string_category_group=category_url.text.split(' ')
        string_category=''
        for iii in range(0,len(string_category_group)-1):
            string_category=string_category+' '+string_category_group[iii]
        detail_main(category_url.attrs['href'],string_category,input_string)
    executor.shutdown(wait=True)    
    print('finish')
