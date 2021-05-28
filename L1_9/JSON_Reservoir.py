import urllib.request as urllib 
import json 

url='https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=50C8256D-30C5-4B8D-9B84-2E14D5C6DF71'
with urllib.urlopen(url) as jsondata:
     data = json.loads(jsondata.read().decode()) 
data = data['DailyOperationalStatisticsOfReservoirs_OPENDATA']
for d in data:
    print("{}:{}".format(d['ReservoirName'],d['EffectiveCapacity']))
