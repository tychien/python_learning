import pprint
import tkinter as tk
from tkinter import ttk
import urllib.request as urllib
import json

def getData():

    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'

    with urllib.urlopen(url) as jsondata:
        data = json.loads(jsondata.read().decode())

    #County = "桃園市"
    #City = "平鎮區"
    County = landString.get()
    City   = cityString.get()
    count = 0
    Date = ""
    toDate = ""
    for d in data:
        if d['縣市'] == County:
            if d['鄉鎮']== City:
                count += int(d['確定病例數'])
                toDate = d['個案研判日']
        Date = d['個案研判日']
    labelLU.config(text='由20200122起')
    labelLM.config(text='{}{}:'.format(County,City))
    labelLL.config(text='該區最近確診日:'.format(toDate))
    labelRU.config(text='至{}止'.format(Date))
    labelRM.config(text='{}例'.format(count))
    labelRL.config(text='{}'.format(toDate))
'''
    if(labelR.winfo_exists() ==1):
        labelL.destroy()
        labelR.destroy()
'''

def getDateData():
    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
    with urllib.urlopen(url) as jsondata:
        data = json.loads(jsondata.read().decode())
    Date = dateString.get()
    count = 0

    for d in data:
        if d['個案研判日'] == Date:
            count += int(d['確定病例數'])
    labelL.config(text='{}:'.format(Date))
    labelR.config(text='{}例'.format(count))
'''
    if(labelLU.winfo_exists() == 1):
        labelLU.destroy()
        labelLM.destroy()
        labelLL.destroy()
        labelRU.destroy()
        labelRM.destroy()
        labelRL.destroy()
'''



root = tk.Tk()
root.geometry('280x270')

labelLand = tk.Label(root,text = "縣市")
labelLand.grid(column=1, row=1,sticky="E")
labelCity = tk.Label(root,text = "鄉鎮")
labelCity.grid(column=1,row=2 ,sticky=tk.E)
labelDate = tk.Label(root,text = "日期")
labelDate.grid(column=1,row=3, sticky=tk.E)
landString = tk.StringVar()
cityString = tk.StringVar()
dateString = tk.StringVar()
entryLand = tk.Entry(root,width=10,textvariable=landString)
entryLand.insert(0,'台北市')
entryCity = tk.Entry(root,width=10,textvariable=cityString)
entryCity.insert(0, '萬華區')
entryDate = tk.Entry(root,width=10,textvariable=dateString)
entryDate.insert(0, '20210511')
entryLand.grid(column=2, row=1, padx=3)
entryCity.grid(column=2, row=2, padx=3)
entryDate.grid(column=2, row=3, padx=3)

tk.Label(root,text='Covid-19 確診病例數',fg='white',bg='pink').grid(column=0, row = 0,columnspan=3,padx=5,pady=10, sticky="WE")
labelLU = tk.Label(root)
labelLM = tk.Label(root)
labelLL = tk.Label(root)
labelRU = tk.Label(root)
labelRM = tk.Label(root)
labelRL = tk.Label(root)
labelL  = tk.Label(root)
labelR  = tk.Label(root)

labelLU.grid(column=0, row=5,sticky="E")
labelLM.grid(column=0, row=6,sticky="E")
labelLL.grid(column=0, row=7,sticky="E")
labelRU.grid(column=2, row=5,padx=10,sticky="W")
labelRM.grid(column=2, row=6,padx=10,sticky="W")
labelRL.grid(column=2, row=7,padx=10,sticky="W")
labelL.grid(column=0,  row=4,padx=10,sticky="E")
labelR.grid(column=2,  row=4,padx=10,sticky="W")


tk.Button(root,text='當地確診總數',bg='red',command=getData).grid(column=0, row=2, padx=5,sticky="WE")
tk.Button(root,text='全台當日確診數',bg='red',command=getDateData).grid(column=0, row=3,padx=5,sticky="WE")
root.mainloop()
