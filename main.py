
from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pywhatkit
from datetime import datetime, timedelta

root = Tk()
root.geometry("600x650")

def OpenFile():
    
    global filename,dfdata
    
    fileopen = askopenfilename(filetypes=[("CSV Files","*.csv")])
    dfdata=[]
    filename = pd.read_csv(fileopen)
    for i in range(len(filename)) :
        dfdata.append(filename.loc[i, "Phone"])

    PathTextBox.delete("1.0",END)
    PathTextBox.insert(END,fileopen)

    DataTextBox.delete("1.0",END)
    DataTextBox.insert(END,filename)


def mainFunc():
    for i in range(len(filename)):
        phone_param=filename.loc[i, "Phone"]
        print(phone_param)
        messageData = inputtxt.get(1.0, "end-1c")
        ccdata=cctxt.get(1.0, "end-1c")
        now = datetime.now()
        now_plus = now + timedelta(minutes = 2) 
        finalstrhr=  now_plus.strftime("%H")
        finalstrmin= now_plus.strftime("%M")
        pywhatkit.sendwhatmsg(f'{ccdata}{phone_param}',messageData,int(finalstrhr), int(finalstrmin),7,True,7)
        time.sleep(10)


Title = root.title( "WhatsApp Bot By Rishabh")
path = StringVar()

InputLabel = Label(root,text = "Dataset:")
InputLabel.grid(row=2,column = 1,sticky=(W))

BrowseButton = Button(root,text="Browse",command = OpenFile)
BrowseButton.grid(row=2,column=1,sticky=(E))

PathLabel = Label(root,text = "Path:")
PathLabel.grid(row = 7,column=1,sticky=(W))

PathTextBox = Text(root,height = 2)
PathTextBox.grid(row = 8,column = 1)

DataLabel = Label(root,text = "Input Data:")
DataLabel.grid(row = 10,column=1,sticky=(W))

DataTextBox = Text(root,height = 15)
DataTextBox.grid(row = 11 ,column = 1,columnspan=2)

ccLabel = Label(root,text = "Country Code:")
ccLabel.grid(row=12,column = 1,sticky=(W))

cctxt = Text(root, height = 1,width=15)
cctxt.grid(row = 13,column = 1,sticky=(W))
cctxt.insert(INSERT,'+91')

MessageLabel = Label(root,text = "Message To Be Sent:")
MessageLabel.grid(row=15,column = 1,sticky=(W))

inputtxt = Text(root, height = 15)
inputtxt.grid(row = 16,column = 1)

SubmitButton = Button(root,text="Submit",command = mainFunc)
SubmitButton.grid(row = 20,column = 1,sticky=(E))

root.mainloop()