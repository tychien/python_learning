import urllib.request as urllib
import json

url1='https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=50C8256D-30C5-4B8D-9B84-2E14D5C6DF71'
url2='https://data.wra.gov.tw/Service/OpenData.aspx?format=json&id=1602CA19-B224-4CC3-AA31-11B1B124530F'

with urllib.urlopen(url1) as jsondata1:
     data1 = json.loads(jsondata1.read().decode())
with urllib.urlopen(url2) as jsondata1:
     data2 = json.loads(jsondata1.read().decode())

data1 = data1['DailyOperationalStatisticsOfReservoirs_OPENDATA']
data2 = data2['ReservoirConditionData_OPENDATA']

CapFull = 0
CapNow  = 0
Time = ""
for d in data1:
    if d['ReservoirName'] == '石門水庫':
        CapFull = float(d['EffectiveCapacity']) 
#        print("{}:Capacity:{},FullLevel:{}".format(d['ReservoirName'],d['EffectiveCapacity'],d['FullWaterLevel']))
for d in data2:
    if d['ReservoirIdentifier']=='10201':
        Time = d['ObservationTime']
        CapNow = float(d['EffectiveWaterStorageCapacity'])
#        print("{}:{}:WaterLevel:{},StorageCapacity:{}".format(d['ObservationTime'],d['ReservoirIdentifier'],d['WaterLevel'],d['EffectiveWaterStorageCapacity']))


print("石門水庫:\t{:04.2f} % \tat \t{}".format((CapNow/CapFull*100),Time))
