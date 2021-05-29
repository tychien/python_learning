import pprint
import tkinter as tk
from tkinter import ttk
import urllib.request as urllib
import json

def getData():

    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'

    with urllib.urlopen(url) as jsondata:
        data = json.loads(jsondata.read().decode())

    County = "新竹縣"
    City = "新豐鄉"
    count = 0
    Date = ""
    toDate = ""
    for d in data:
        if d['縣市'] == County:
            if d['鄉鎮']== City:
                count += int(d['確定病例數'])
                toDate = d['個案研判日']
        Date = d['個案研判日']
    label.config(text='由20200122起\n確診病例數\n{}{}:{}\n該區最近確診日:{}\n更新日期:{}'.format(County,City,count,toDate,Date))

root = tk.Tk()
root.geometry('480x270')

labelLand = tk.Label(root,text = "縣市")
labelLand.grid(column=0, row=1, sticky=tk.W)
labelCity = tk.Label(root,text = "鄉鎮")
labelCity.grid(column=0,row=2,sticky=tk.W)
landString = tk.StringVar()
cityString = tk.StringVar()
entryLand = tk.Entry(root,width=20,textvariable=landString)
entryCity = tk.Entry(root,width=20,textvariable=cityString)
entryLand.grid(column=1, row=1, padx=10)
entryCity.grid(column=1, row=2, padx=10)


tk.Label(root,text='Covid-19',fg='white',bg='pink').grid(column=2, row =0 )
label = tk.Label(root)
label.grid(column=3, row=4)

tk.Button(root,text='Update Now',bg='red',command=getData).grid(column=3, row=5)

root.mainloop()
