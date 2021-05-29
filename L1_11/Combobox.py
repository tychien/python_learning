import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('200x100')

labelTop = tk.Label(root,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(root,
                            values=[
                                    "January",
                                    "February",
                                    "March",
                                    "April"],
                            state="readonly")

comboExample.grid(column=0, row=1)
comboExample.current(0)

print(comboExample.current(), comboExample.get())

root.mainloop()
