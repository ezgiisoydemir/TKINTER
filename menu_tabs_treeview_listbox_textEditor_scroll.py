# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:49:49 2022

@author: ezgis
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("800x600")

#menu

def fileFunction():
    print("here")
    
menubar = tk.Menu(window)
window.config(menu = menubar)   # menubar ı window un menusune ekle
"""Burada “config” metodu yardımıyla öncelikle “menu” adlı aracı “pencere”ye baglıyoruz."""
file = tk.Menu(menubar)
edit = tk.Menu(menubar)

menubar.add_cascade(label = "file" , menu = file)
menubar.add_cascade(label = "edit" , menu = edit)
""" casacade , Creates a new hierarchical menu by associating a given menu to a parent menu (associating = ilişkilendirme )"""
"""cascade = çağlayan, kademeli, şelale"""
file.add_command(label = "new file" , command = fileFunction)
edit.add_command(label = "undo" , command = fileFunction)
""" command , Adds a menu item to the menu. """

#tabs

tabs = ttk.Notebook(window , width = 540 , height = 300 )
tabs.place(x=25,y=25)

"""
ttk.Notebook widget allows you to select pages of contents by clicking on tabs:
When you click one of these tabs, the Notebook widget will display a child pane associated with the selected tab. 
Typically, a child pane is a Frame widget.
(display = görüntülemek)(assosiate = ilişkilendirme)
"""
tab1 =ttk.Frame(tabs , width = 50 , height = 50)
tab2 =ttk.Frame(tabs , width = 50 , height = 50)
tab3 =ttk.Frame(tabs , width = 50 , height = 50)
"""
A frame is a widget that displays as a simple rectangle.
Typically, you use a frame to organize other widgets both visually and at the coding level.
"""
tk.Label(tab1 , text = "tab1").pack()
tk.Label(tab2 , text = "tab2").pack()
#tk.Label(tab3 , text = "tab3").pack()
"""
Tkinter Label widget is used to display a text or image on the screen
"""
tabs.add(tab1 , text = "treeview")
tabs.add(tab2 , text = "listbox")
tabs.add(tab3 , text = "text editor")

#tree view 
"""
A Treeview widget allows you to display data in both tabular and hierarchical structures
"""
treeview = ttk.Treeview(tab1)
treeview.place(x=5,y=5)

treeview.insert("","0","item1",text="Spain")
""" ilk dal hiçbir şeyin altında olmayacak o yüzden "", indeksi 0 olacak ve ismi item1 olacak """
treeview.insert("item1","1","item2",text="Madrid")
""" madrid yazısı item1 in altında ve 1inci indeks olarak yazılır. """
treeview.insert("","2","item3",text="France")
treeview.insert("item3","3","item4",text="Paris")
"""(insert = sokmak , eklemek , girmek , ilave sayfalar , ilan , vermek)"""

def callback(event):
    """
       ben window da herhangi bir hareket yaptığım zaman bu event bunun farkına varacak ve bana bu hareketi return edecek
    """
    item = treeview.identify("item", event.x, event.y)
    """
    ben treeview in üzerine geldiğim zaman bir item seçtiğim zaman bu x ve y üzerinden hangisi olduğunu item üzerine yazdırabiliyoru
    """
    print(item)
    
 
treeview.bind("<Double-1>" , callback)
"""
(bind = bağlamak , ciltlemek , tutturmak , engel olmak)
bind, callback fonksiyonunu çağırmak için yazdık
treevieew üzerinde mouse ile çift tıklama gerçekleştirilirse hemen callback fonksiyonunu çağır
"""

#listbox
""" item ları depolamak için kullandığımız listelerdir """
listBox = tk.Listbox(tab2, selectmode = tk.MULTIPLE)
""" MULTİPLE yaptığımızda birden fazla şeyi aynı anda seçebiliyoruz. """
listBox.insert(0,"Spain")
""" ilki index diğeri item ımızın ismi """
listBox.insert(1,"France")
listBox.insert(2,"China")
## insert = sokmak eklemek atmak girmek

listBox.place(x=5 , y=5)

def getItem():
    index_list = listBox.curselection() #listbox ımıza erişmek için yazdık
    """curselection is mainly used when multiple values need to be fetched."""
    print(index_list)
    for each in index_list:
        print(listBox.get(each))
        
button = tk.Button(tab2 , text = "button" ,command = getItem)
button.place(x=150,y=5)     #yerleştirme yaptı       
        

# text editor

textEditor = tk.Text(tab3 , width = 25 , height = 25 , wrap = tk.WORD)
""" tk.Word, kelimeler ile işlem yapacağımız anlamına gelir"""
textEditor.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

def textFunction():
    print(textEditor.get(1.0 , tk.END))
    
button = tk.Button(tab3 , text = "save" , command = textFunction)
button.grid(row = 0 , column = 2 , padx = 10 , pady = 10)

#scroll

scroll = tk.Scrollbar(tab3 , orient = tk.VERTICAL , command = textEditor.yview)
scroll.grid(row = 0 , column = 1 , sticky = tk.N + tk.S)
"""
scroll u bağlamak için kuzey ve güney yonlerini girdik
"""
textEditor.config(yscrollcomman = scroll.set)
"""
yarattığımız scroll set edilmiş oldu
"""

window.mainloop()

