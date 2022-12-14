import pandas
import requests
import json
import streamlit as st
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=주엽동&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=KQRR%2BJLPRITcRv6CvRB1QUxmDQ%2BKmcKWMjK1A19g%2BiHLEbXTpqjWmut5pwHfKkH6O7KfqLSXxEmrLt6Ctooliw%3D%3D"

geturl = requests.get(url)
rawData = geturl.text

json_ob = json.loads(rawData)

jsonData = json_ob['response']['body']['items']
data = pandas.DataFrame(jsonData)

for i in range(len(data['khaiValue'])):
    if data['khaiValue'][i] == '-':
        data['khaiValue'][i] = '0'
for i in range(len(data['pm10Value'])):
    if data['pm10Value'][i] == '-':
        data['pm10Value'][i] = '0'      
for i in range(len(data['coValue'])):
    if data['coValue'][i] == '-':
        data['coValue'][i] = '0'  
for i in range(len(data['so2Value'])):
    if data['so2Value'][i] == '-':
        data['so2Value'][i] = '0'   
for i in range(len(data['o3Value'])):
    if data['o3Value'][i] == '-':
        data['o3Value'][i] = '0'  
for i in range(len(data['no2Value'])):
    if data['no2Value'][i] == '-':
        data['no2Value'][i] = '0'  

data['환경 수치'] = pandas.to_numeric(data['khaiValue'])
data['미세먼지'] = pandas.to_numeric(data['pm10Value'])
data['일산화탄소'] = pandas.to_numeric(data['coValue'])
data['아황산가스'] = pandas.to_numeric(data['so2Value'])
data['오존'] = pandas.to_numeric(data['o3Value'])
data['이산화질소'] = pandas.to_numeric(data['no2Value'])

time = data['dataTime']
figure = data['환경 수치']
fineDust = data['미세먼지']
co = data['일산화탄소']
so2 = data['아황산가스']
o3 = data['오존']
no2 = data['이산화질소']

st.write('# 일산 주엽동 대기질')
st.write('***')
st.write('#### 선 그래프')
st.line_chart(figure)
st.line_chart(fineDust)
st.line_chart(co)
st.line_chart(so2)
st.line_chart(o3)
st.line_chart(no2)
st.write('***')
st.write('#### 막대 그래프')
st.bar_chart(figure)
st.bar_chart(fineDust)
st.bar_chart(co)
st.bar_chart(so2)
st.bar_chart(o3)
st.bar_chart(no2)
