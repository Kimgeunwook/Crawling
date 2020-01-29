#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import openpyxl
import os.path
import xlsxwriter 
import os
def main(input_country):
    line=list()
    workbook = xlsxwriter.Workbook('C:\\Users\\Mandy\\Desktop\\country\\MonkeyTravel\\'+str(input_country)+'.xlsx') 
    worksheet = workbook.add_worksheet() 
    workbook.close() 
    write_wb=openpyxl.load_workbook('C:\\Users\\Mandy\\Desktop\\country\\MonkeyTravel\\'+str(input_country)+'.xlsx')#엑셀 파일 열기
    write_ws=write_wb.active
    filenames=os.listdir('C:\\Users\\Mandy\\Desktop\\MonkeyTravel\\'+str(input_country)+'')
    _count=1
    for filename in filenames:    
        print(filename+str(_count))
        f=open('C:\\Users\\Mandy\\Desktop\\MonkeyTravel\\'+str(input_country)+'\\'+filename, 'r',encoding='utf-8')
        rdr = csv.reader(f)
        for a in rdr:
            a.insert(4,_count)
            write_ws.append(a)        
        _count=_count+1    
        f.close()        
    write_wb.save('C:\\Users\\Mandy\\Desktop\\country\\MonkeyTravel\\'+str(input_country)+'.xlsx')
    print('finish')
    


# In[ ]:





# In[ ]:




