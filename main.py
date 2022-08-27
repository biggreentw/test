import requests
from io import BytesIO
from lxml import etree
html =requests.get("https://ebus.tycg.gov.tw/xmlptx/routes/123/shape")
html.encoding= 'UTF-8'
xml_bytes= html.content  #擷取xml的純文字內容
f= BytesIO(xml_bytes)  #以bytes資料型態儲存
tree = etree.parse(f)
root= tree.getroot()
print(root[3][0][0].text)  #讀取Route_ID
print(root[3][0][4].text)  #讀取Geometry

#---輸出excel檔案---# 
path1= './123.xlsx'
import pandas as pd
import openpyxl
col1= 'ID'
col2= 'WKT'
list1= [root[3][0][0].text]
list2= [root[3][0][4].text]
data= pd.DataFrame({col1:list1, col2:list2})
print(data.shape)  #回傳列數與欄數
print(data.columns)  #回傳欄位名稱
print(data.info)  #回傳資料內容
data.to_excel(path1, index=False)

#---輸出txt檔案---#
import pandas as pd
path2= './123.txt'
a= open(path2, 'w')
pd.set_option('max_colwidth', 10000)  #設置value的長度, 默認=50
a.write(data.to_string())
a.close()