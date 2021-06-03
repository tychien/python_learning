import tkinter as tk
from tkinter import *
import urllib.request as urllib
import json
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



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
    arr = {}
    arrT = []
    arrP = []
    Time = ""

    for d in data1:
        if d['ReservoirName'] == '寶山第二水庫':
            CapFull = float(d['EffectiveCapacity'])
    for d in data2:
        if d['ReservoirIdentifier']=='10405':
            Time = d['ObservationTime']
            T = Time.replace('T','\n')
            CapNow = float(d['EffectiveWaterStorageCapacity'])
            Percentage = (CapNow/CapFull*100)
            arrT.append(T)
            arrP.append(Percentage)
            print('{:04.2f}%'.format(Percentage))
            label.config(text='更新時間:{}\nPercentage:\t{:04.2f} % \n{}萬立方公尺'.format(Time,Percentage,CapNow))
    arr = {'Time':arrT,'Percent':arrP}
    df1 = DataFrame(arr,columns=['Time','Percent'])
    figure1 = plt.Figure(figsize=(15,4),dpi=70)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)

    line1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    df1 = df1[['Time','Percent']].groupby('Time').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='b',marker='o', fontsize=10,rot=270)
    ax1.set_title('BaoShan Second Reservoir')
root = tk.Tk()
root.geometry('480x600')

tk.Label(root,text='寶山第二水庫',fg='white',bg='lightblue').pack(fill=tk.BOTH)
tk.Button(root,text='Update Now',bg='red',command=getData).pack()
label = tk.Label(root)

label.pack()



root.mainloop()
