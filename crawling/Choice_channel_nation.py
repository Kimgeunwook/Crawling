from concurrent.futures import ThreadPoolExecutor
import csv
import requests
from bs4 import BeautifulSoup
import re
import os
import json
from pprint import pprint
import os.path
import regular2
import Ta_csvtoexcel
import extract_country_in_mrt
import Choice_menu_city
import Mt_csv_to_excel
import get_auto_name
import city_top
import Klook_detail
import Klook_csv_to_excel
import TripDotCom_nation_to_citylist
import Tripdotcom_csv_to_excel
print('1. MRT')
print('2. Trip Advisor')
print('3. Monkey Travel')
print('4. Klook')
print('5. Trip.com')
input_channel=input('채널 입력 :')

if input_channel=='1':
    input_country=input('나라 입력 (한글) :')
    extract_country_in_mrt.extract(input_country)
    print('Desktop\\country\\mrt폴더 확인')
elif input_channel=='2':
    input_country=input('나라(도시) 입력 (영어):')
    (country,code)=get_auto_name.main(input_country)
    print('1. 도시별 인기상품 추출')
    print('2. 나라별 상품 추출')
    input_num=input('번호 입력 :')
    if input_num=='1':
        city_top.main(country,code)
    else:    
        regular2.Ta_main(country,code)    
        Ta_csvtoexcel.csvtoexcel_main(country)
        print('Desktop\\country폴더 확인')
elif input_channel=='3':
    print('1. 베트남')
    print('2. 태국')
    input_country=input('나라 입력 (번호):')
    if input_country=='1':
        Choice_menu_city.main('vn')#베트남 페이지
        Mt_csv_to_excel.main('베트남')
    elif input_country=='2':
        Choice_menu_city.main('thai')#베트남 페이지
        Mt_csv_to_excel.main('태국')
elif input_channel=='4':
    Klook_detail.main()
    Klook_csv_to_excel.main()

elif input_channel=='5': 
    TripDotCom_nation_to_citylist.main()
    Tripdotcom_csv_to_excel.main()