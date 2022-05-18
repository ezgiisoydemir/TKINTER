# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:53:34 2022

@author: ezgis
"""

from PyQt5.QtWidgets import *


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 520, 320)
        self.setWindowTitle("Menu App")
        
        self.menubar()
        self.show()
        
    def manubar(self):
        
        bar =self.menuBar()
        
        file = bar.addMenu("File")
        file.addAction("New")
        
        save = QAction("Save" , self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        
        data = file.addMenu("Data")
        data.addAction("Export")
        data.addAction("Import")
        
        file.triggered[QAction].connect(self.progressTrig)
        
    def progressTrig(self,q):
        print(q.text())
        
 
        
window = Window()