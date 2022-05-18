# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:12:59 2022

@author: ezgis
"""

import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.title("Geometry Manager")

#pack

red = tk.Button(window , text = "Red" , fg ="red")
red.pack(side = tk.LEFT)

green = tk.Button(window , text = "Green" , fg ="green")
green.pack(side = tk.LEFT)

blue = tk.Button(window , text = "Blue" , fg ="blue")
blue.pack(side = tk.LEFT)

black = tk.Button(window , text = "Black" , fg ="black")
black.pack(side = tk.BOTTOM)

cyan = tk.Button(window , text = "Cyan" , fg ="cyan")
cyan.pack(side = tk.TOP , fill = tk.BOTH , expand = True)

"""
BOTH, hem yatayda hem dikeyde doldurur
expand , tüm boş alanı doldurur
"""

#grid manager

for r in range(5):  #row
   for c in range(5):   #column
        label = tk.Label(window, text="R%s/C%s" %(r,c),borderwidth = 2)
        label.grid(row=r , column = c , padx = 3 , pady = 3)
        """padx ve pady yi yazmazsa birbirlerine gireceklerdi"""
#place

label1 = tk.Label(window , text="place1")
label1.place(x = 15 , y = 15)
"""
label1 yazısı x ve y den 15 piksel uzaklıkta yazılır
"""

label1 = tk.Label(window , text="place1")
label1.place(x = 30 , y = 30)

label1 = tk.Label(window , text="place1")
label1.place(x = 45 , y = 45)

label1 = tk.Label(window , text="place1")
label1.place(relx = 0 , rely = 0)

"""
bu durumu her seferinde x ve y değerlerine bir sayıgirerek yazmak istemezesek relx real x kullanılır
"""

window.mainloop()