import tkinter as tk
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

tk.Label(root,text='Covid-19',fg='white',bg='pink').pack(fill=tk.BOTH)
tk.Button(root,text='Update Now',bg='red',command=getData).pack()
label = tk.Label(root)

label.pack()

root.mainloop()
