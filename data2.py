#라이브러리 import
import pandas as pd
import requests
import json
import streamlit as st
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=주엽동&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=KQRR%2BJLPRITcRv6CvRB1QUxmDQ%2BKmcKWMjK1A19g%2BiHLEbXTpqjWmut5pwHfKkH6O7KfqLSXxEmrLt6Ctooliw%3D%3D"

geturl = requests.get(url)
rawData = geturl.text

json_ob = json.loads(rawData)

jsonData = json_ob['response']['body']['items']
data = pd.DataFrame(jsonData)

data['환경 수치'] = pd.to_numeric(data['khaiValue'])
data['미세먼지'] = pd.to_numeric(data['pm10Value'])

time = data['dataTime']
figure = data['환경 수치']
fineDust = data['미세먼지']

st.write('# IoT 기말과제')
st.write('=============')
st.write('#### 일산 주엽동의 날씨 데이터')
st.line_chart(figure)
st.line_chart(fineDust)
st.bar_chart(figure)
st.bar_chart(fineDust)
