# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:05:00 2022

@author: ezgis
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox # Bunu import etmek önemli

window = tk.Tk()    # Tkinter kütüphanesinden Tk classını çağırdık ve window objesi yaratmış oluruz
window.geometry("500x400")
window.title("Welcome The First App")

def buttonFunction():
    print("Push Button")
    
    # label   
    label.config(text="hello world",
                 fg = "black",
                 bg = "red",
                 font = "Times 25")
    
    # entry
    value = entry.get()
    print(value)
    label.configure(text=value)
    entry.configure(state = "disabled")
"""
entry üzerine yazdığımız değerleri get metodu ile çekeriz
config == configure ikisini de yazabiliriz
"""    
    # message 
#    message_box = messagebox.showinfo(title = "info" , message="information")
#    message_box = messagebox.askretrycancel(title = "info" , message="information")
#    message_box = messagebox.askquestion(title = "info" , message="information")
#    message_box = messagebox.askyesnocancel(title = "info" , message="information")
message_box = messagebox.showerror(title = "info" , message="information")
print(message_box)

    
## button
button = tk.Button(window, text = "First Button" , activebackground = "red",
                   bg = "black" , fg = "white" , activeforeground = "black",
                   height = 15 , width = 50 ,
                   command = buttonFunction)
""" 
window butonun içindeki ilk parametre çünkü button window un üstünde
activebackground, butona basıldığında oluşacak renk
bg, background demek. Direkt arka plan rengi
fg, Default yazı rengi. Yani hiçbir butona basmadığımızda görünen renk
activeforeground, bastıktan sonraki yazı rengi
command, butona basıldığında command parametresi bizi buttonFunction fonksiyon isimli methoda yönlendirir.

"""
button.pack()
"""
Pack, kodu windowa ekleneceğini pack yardımıyla öğrenir. Eğer bunu yazmazsak biz eklendiğini biliriz fakar sistem görmez.
geometry manager lardan bir tanesidir
widget ı window a ekler 
"""

## label
    
label = tk.Label(window , text = "Hi World" , font = "Times 16" , fg="white",
                 bg = "black" , wraplength = 150)
label.pack(side = tk.RIGHT , padx = 25)
"""
padx,sağ tarafta 25 cmlik boşluk yarattı 
"""
"""
tk.label , tkinter kütüphanesinden label class ını çağırdık
"""
    ## entry
entry = tk.Entry(window,width=50)
entry.insert(string = "write something only one time" , index=0)
entry.pack(side=tk.LEFT, padx=25)

window.mainloop()

"""
MAİNLOOP
Root. mainloop() is simply a method in the main window that executes what we wish to execute in an application. 
As the name implies it will loop forever until the user exits the window or waits for any events from the user. 
The mainloop automatically receives events from the window system and deliver them to the application widgets. 
This gets quit when we click on the close button of the title bar. 
So, any code after this mainloop() method will not run.
When a GUI is gets started with the mainloop() a method call, 
Tkinter python automatically initiates an infinite loop named as an event loop. 
So, after this article, we will be able to use all the widgets to develop an application in Python. 
Different widgets are Combo box, button, label, Check button, Message Box, Images, and Icons.
"""

