#!/usr/bin/env python
# coding: utf-8

# In[15]:


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
import chardet
import choice_category

def main(input_country):
    if input_country=='vn':#베트남일때
        print('Choice_menu_city 진입')
        link_list=[('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=242&mfcode=MTU3fDY0MA==','다낭'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=243&mfcode=MTU3fDkxNw==','호이안'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=241&mfcode=MTU3fDY0Mw==','호치민'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=240&mfcode=MTU3fDY0NA==','하노이'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=245&mfcode=MTU3fDY0NQ==','하롱베이'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=255&mfcode=MTU3fDY0Ng==','나짱(나트랑)'),
                  ('https://vn.monkeytravel.com/user/product/product_list.php?part=tour&city_id=256&mfcode=MTU3fDY0Nw==','푸꾸옥(푸꿕)' )]
        for i in link_list:
            choice_category.main(input_country,'베트남',i[1],i[0])
            
    elif input_country=='thai':
        print('Choice_menu_city 진입')            
        link_list=[('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=1&mfcode=NXw2Mw==','방콕'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=5&mfcode=NXwxOA==','파타야'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=6&mfcode=NXwyOTg=','푸켓'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=21&mfcode=NXwxMTM=','치앙마이'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=113&mfcode=NXwyMjc=','끄라비'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=114&mfcode=NXw1NzU=','카오락'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=22&mfcode=NXwyMA==','후아힌'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=tour&city_id=261&mfcode=NXw4OTk=','1박2일투어'),
                   
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=1&mfcode=Nnw2NQ==','방콕'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=5&mfcode=Nnw2NA==','파타야'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=6&mfcode=NnwxMTQ=','푸켓'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=21&mfcode=NnwyNA==','치앙마이'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=20&mfcode=Nnw1OTU=','사무이'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=113&mfcode=Nnw1OTY=','끄라비'),
                   ('https://thai.monkeytravel.com/user/product/product_list.php?part=show&city_id=22&mfcode=NnwyNQ==','후아힌')]
        for i in link_list:
            choice_category.main(input_country,'태국',i[1],i[0])
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




