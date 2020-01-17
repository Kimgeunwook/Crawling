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
print('1. MRT')
print('2. Trip Advisor')
print('3. Monkey Travel')
input_channel=input('채널 입력 :')

if input_channel=='1':
    input_country=input('나라 입력 (한글) :')
    extract_country_in_mrt.extract(input_country)
    print('Desktop\\country\\mrt폴더 확인')
elif input_channel=='2':
    input_country=input('나라 입력 (영어):')
    regular2.Ta_main(input_country)
    Ta_csvtoexcel.csvtoexcel_main(input_country)
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