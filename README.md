
# 1.기능   
채널, 국가를 선택하면 해당하는 채널, 국가의 여행 상품을 csv파일로 저장후 csv파일을 읽어 엑셀 파일을 생성하는 프로그램
#         
#                  
          

# 2.Prerequisites
```
1. python 3.7.4
2. pip install requests
3. pip install beautifulsoup
4. pip install xlsxwriter
5. pip install openpyxl
6. pip install urllib
```            
#         
#                  
              
# 3.프로그램 작동법   
***1. Choice_channel_nation.py 실행***    
***2. 원하는 채널, 국가 선택***         
***3. 'finish' 문구가 뜨면 지정한 폴더에 가서 excel파일 확인***    
#         
#                  
      

<div> <center><img src="https://user-images.githubusercontent.com/48399897/73320598-2bba4c80-4283-11ea-96e2-525d8f7d8cd3.PNG" width="30%" height="40%" title="Choice_channel_nation.py" alt="실행1"> </img><img src="https://user-images.githubusercontent.com/48399897/73322763-aa65b880-4288-11ea-989d-02b9ed222d41.PNG" width="60%" height="40%" title="저장되는 위치 출력" alt="실행1">     </img>  
</div>    

#           
#                     
      
# 4.주의사항(파일이 생성되는 위치 바꾸고 싶은 경우)    
## ***(case) TripAdvisor***  

<div>      
                                   
<img src="https://user-images.githubusercontent.com/48399897/73321545-290d2680-4286-11ea-8765-c51f2f830db9.PNG" width="50%" height="40%" title="regular2.py" alt="실행1">     </img><img src="https://user-images.githubusercontent.com/48399897/73321635-6ffb1c00-4286-11ea-87c6-e112573c7cf0.PNG" width="50%" height="40%" title="Ta_csvtoexcel.py" alt="실행1">     </img>    

<p>regular2.py, Ta_csvtoexcel.py 빨간 동그라미친 폴더 설정 부분을 원하는 폴더로 변경</p>
</div>

## ***(case) MonkeyTravel***
<div>      
                                   
<img src="https://user-images.githubusercontent.com/48399897/73322428-1eec2780-4288-11ea-9560-315067a468a4.PNG" width="50%" height="40%" title="choice_category.py" alt="실행1">     </img><img src="https://user-images.githubusercontent.com/48399897/73322428-1eec2780-4288-11ea-9560-315067a468a4.PNG" width="50%" height="40%" title="monkey.py" alt="실행1">     </img>    

<p>choice_category.py, monkey.py 빨간 동그라미친 폴더 설정 부분을 원하는 폴더로 변경</p>
</div>

## ***(case) Klook***
1. 실행 후 403에러 뜨면 klook사이트가서 봇 체크 풀어주기    
2. csv,excel파일 생성 폴더 변경시 4.주의사항의 tripadvisor, monkeytravel case처럼    
Klook_csv_to_excel.py, Klook_detail.py폴더 부분 수정

## ***(case)Trip Dot com***    
1. csv,excel파일 생성 폴더 변경시 4.주의사항의 tripadvisor, monkeytravel case처럼   
Tripdotcom_csv_to_excel.py, TripDotCom_detail.py폴더 부분 수정

#           
#                     
      
# 4.실행 결과    
## 
<div>      
                                   
<img src="https://user-images.githubusercontent.com/48399897/73332666-c5e1bb00-42aa-11ea-9d28-cbc88d0e388c.PNG" width="49%" height="40%" title="실행 결과" alt="실행결과">     </img>          
<img src="https://user-images.githubusercontent.com/48399897/73332565-7ac7a800-42aa-11ea-90f8-a8233366f3c8.PNG" width="49%" height="40%" title="실행 결과" alt="실행결과">     </img>
</div>


