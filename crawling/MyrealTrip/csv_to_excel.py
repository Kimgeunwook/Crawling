#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv
import openpyxl
import os.path
line=list()
write_wb=openpyxl.load_workbook('C:\\Users\\Mandy\\Desktop\\threadpool\\new.xlsx')#엑셀 파일 열기
write_ws=write_wb.active

for i in range(0,100):
    if os.path.exists('C:\\Users\\Mandy\\Desktop\\threadpool\\info' + str(i) + '.csv'):
        f = open('C:\\Users\\Mandy\\Desktop\\threadpool\\info'+str(i)+'.csv', 'r')
        rdr = csv.reader(f)
        for a in rdr:
          line.append(a)
f.close()

for item in line:   
    write_ws.append(item) #ALL목록에 추가
    flag=0  #시트 목록에 이미 있는 나라인지 확인하는 플래그
    for sheet in write_wb:
        if str(sheet)==str('<Worksheet "'+item[1]+'">'):#기존에 있는거면
            flag=1
            sheet.append(item)
    if flag==0: #없으면 시트 추가
        sheet2=write_wb.create_sheet(item[1])
        sheet2.append(item)    
write_wb.save('C:\\Users\\Mandy\\Desktop\\threadpool\\new.xlsx')
print('finish')


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




