import openpyxl
import csv
import os.path
import xlsxwriter 
import os
#1.폴더 한벌 갈고
#2.유효할때만 카운트업
def extract(input_country):
    print('진행중...')
    _count=1
    workbook = xlsxwriter.Workbook('C:\\Users\\Mandy\\Desktop\\country\\mrt\\'+str(input_country)+'.xlsx') 
    worksheet = workbook.add_worksheet() 
    workbook.close() 
    write_wb=openpyxl.load_workbook('C:\\Users\\Mandy\\Desktop\\country\\mrt\\'+str(input_country)+'.xlsx')#엑셀 파일 열기
    write_ws=write_wb.active
    for i in range(0,80000):
        flag=0
        if i<50000:
            item=list()
            f = open('C:\\Users\\Mandy\\Desktop\\mrt\\all\\info' + str(i) + '.csv',  'r',encoding='utf-8')
            rdr = csv.reader(f)
            for a in rdr:
                if a[1]==input_country:
                    flag=1
                else: 
                    break
                del a[4]   
                a.insert(4,_count)
                item.append(a)
                for items in item:
                    write_ws.append(items) #ALL목록에 추가
            if flag==1:
                _count=_count+1
                
        else:
            item=list()
            f = open('C:\\Users\\Mandy\\Desktop\\mrt\\threadpool4(50000~79999)\\info' + str(i) + '.csv',  'r',encoding='utf-8')
            rdr = csv.reader(f)
            for a in rdr:
                if a[1]==input_country:
                    flag=1
                else: 
                    break    
                del a[4]       
                a.insert(4,_count)
                item.append(a)
                for items in item:
                    write_ws.append(items) #ALL목록에 추가
            if flag==1:    
                _count=_count+1
    write_wb.save('C:\\Users\\Mandy\\Desktop\\country\\mrt\\'+str(input_country)+'.xlsx')            
    f.close()  
    print('finish')