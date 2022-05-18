# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:55:58 2022

@author: ezgis
"""

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image #(PIL = Python Image Library)

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
""" In this case, we use TkAgg backend, which is made to integrate into Tkinter."""
"""The Figure class represents the drawing area on which matplotlib charts will be drawn.
   The FigureCanvasTkAgg class is an interface between the Figure and Tkinter Canvas.
   The NavigationToolbar2Tk is a built-in toolbar for the figure on the graph."""
   
window = tk.Tk()
window.geometry("500x800")

#file dialog
def openFile():
    file_name = filedialog.askopenfilename(initialdir = "C:\Tkinter\Tez" , title = "select a file..")
    """ ( initialdir = initial director = """
    print(file_name)
    """ buraya kadarki kısma göre resmi string return ettiğimiz için görsel bir şey değil hangi dosyada olduğunu görürüz"""
    img = Image.open(file_name) 
    """ burada görseli açtık"""
    img = ImageTk.PhotoImage(img)
    """ burada görseli image e çevirdik"""
    
    label = tk.Label(window, image = img)
    label.image = img
    label.pack(padx=15,pady=15)
    
button=tk.Button(window , text = "open file" , command = openFile)
button.pack()

#plot
fig = Figure(figsize=(5,4) , dpi = 50)
""" figsize ve dpi ile kaç tane piksele çizdireceğimizi belirleriz"""
""" örneğin 5inch*50=250 piksel, 4inch*50=200 piksel = 250 / 200 piksellik bir figur elde ederiz """
data = np.arange(0,3,0.1)
fig.add_subplot(111).plot(data,data*2+10)
""" (111) 1 satır 1 sütun ve 1 tane plot ekleyeceğimiz anlamına gelir"""
""" (data, data*2+10) demek (x,y) noktalarını kafamıza göre belirlemek demek"""
""" add a subplot to the figure and return the axes of the subplot"""
canvas = FigureCanvasTkAgg(fig,master=window)
""" Figure ümüzü window a koymak demek"""
""" FigureCanvasTkAgg object that connects the Figure object with a Tkinter’s Canvas object:"""
canvas.draw()
""" draw dedikten sonra figür görselleşmeye hazır hale gelir"""
canvas.get_tk_widget().pack()
""" figure_canvas.get_tk_widget().pack() , place the chart on the Tkinter’s root window"""

# mouse event

def leftClick(event):
    tk.Label(window , text = "left").pack()

def middleClick(event):
    tk.Label(window , text = "middle").pack()

def rightClick(event):
    tk.Label(window , text = "right").pack()

window.bind("<Button-1>" , leftClick)
window.bind("<Button-2>" , middleClick)
window.bind("<Button-3>" , rightClick)

window.mainloop()
