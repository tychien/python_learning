import tkinter as tk 
import urllib.request as urllib
import json

def getData():
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
    for d in data2:
        if d['ReservoirIdentifier']=='10201':
            Time = d['ObservationTime']
            CapNow = float(d['EffectiveWaterStorageCapacity'])

    Percentage = (CapNow/CapFull*100)
    label.config(text='更新時間:{}\nPercentage:\t{:04.2f} % \n{}萬立方公尺'.format(Time,Percentage,CapNow))

root = tk.Tk() 
root.geometry('480x270')

tk.Label(root,text='石門水庫',fg='white',bg='lightblue').pack(fill=tk.BOTH) 
tk.Button(root,text='Update Now',bg='red',command=getData).pack()
label = tk.Label(root)

label.pack()

root.mainloop() 
