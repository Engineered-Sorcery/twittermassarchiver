import shutil
import tempfile
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve
import json
import tkinter as tk
import tkinter.ttk as ttk
import os
from tkinter import scrolledtext
def parse_URL(msg):
    url=msg.replace("twitter","api.vxtwitter")

    response = urlopen(url)

    data_json = json.loads(response.read())

    sanitized_string="".join(ch for ch in data_json["user_screen_name"] if ch.isalnum() or ch==" ")

    print("User: "+sanitized_string+"Time: "+str(data_json["date_epoch"]))
    a=0;

    for x in data_json["media_extended"]:
        user_path=sanitized_string
        if not os.path.isdir(user_path):
            os.makedirs(user_path)
        user_path=user_path+"/"
        print(data_json["media_extended"])
        match (x["type"]):
            case "image":
                print("Image: "+x["url"])
                filename = user_path+sanitized_string+str(data_json["date_epoch"])+"["+str(a)+"]"+".png"
                urlretrieve(x["url"],filename)               
            case "video":
                print("Video: "+x["url"])
                filename = user_path+sanitized_string+str(data_json["date_epoch"])+"["+str(a)+"]"+".mp4"
                urlretrieve(x["url"],filename)  
            case "gif":
                print("GIF: "+x["url"])
                filename = user_path+sanitized_string+str(data_json["date_epoch"])+"["+str(a)+"]"+".mp4"
                urlretrieve(x["url"],filename)
        a=a+1




def onButtonPress():
    # Do a thing
    print("Button pressed")
    INPUT = t.get("1.0", "end-1c")
    inputted_URLs=INPUT.split("\n")
    for x in inputted_URLs:
        parse_URL(x)
        
    
    
window = tk.Tk()
window.title("Twitter Archiver")
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
ttk.Label(window,text="Please Input URLs with a newline in between, then press Ok",font="Helvetica 16 bold").grid(row=15,column=0,pady=25)
t = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=100, height=20, font="Helvetica 16 bold")
t.grid(column=0, row=16)
ttk.Button(window, text="Ok", command=lambda:onButtonPress()).grid(row=17,column=0,pady=25)
window.mainloop()
    



