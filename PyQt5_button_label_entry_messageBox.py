# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:49:58 2022

@author: ezgis
"""

from PyQt5.QtWidgets import *
""" PyQt5 in QWidget clasındaki her şeyi import etmiş oluruz"""
from PyQt5.QtGui import QFont

class Window(QWidget):
    """ inherit from QWidget = QWidget classında bulunan tüm methodları kullanabiliriz """
    def __init__(self):
        super().__init__()
        """ QWidget classımızdan inherit edeceğimiz kod satırı. Bunu yazdıktan sonra classtaki tüm widgetları kullanabilirz"""
        
        self.setGeometry(50,50,1080,640)    
        """ Pencere boyutu ayarlıyoruz. İlk kısım sol üst koşeden başlayacağını gösterir. Yani pencerenin 50,50 sinden başlaması gerektiğini gösterir. 1080,640 da eni ve boyu """
        self.setWindowTitle("PYQT5 App")
        
        """ self diye yazdığımız şey window. Burada da her fonksiyonu tek tek çağırmak lazım. Eğer çağırmazsak kod çalışmaz """
        self.button()
        self.label()
        self.entry()
        self.show()
        self.messageBox()
        self.font()
        self.show()
        """ Eğer bu metodu yazmazsak print etmez ekrana göstermez """
        
        # button
    def button(self):
        button = QPushButton("HelloWorld", self)
        button.setToolTip("This is hello world button")
        button.resize(100,50)
        button.move(50,50)
        button.clicked.connect(self.buttonFunction)
        """ butona tıklandığında buttonFunction ile bağlantı kur"""
        
    def buttonFunction(self):
        print("hello world")
        
    # Label
    def label(self):
        
        text1 = QLabel("hello" , self)
        self.text2 = QLabel("world" , self)
        """ eğer sadece text2 yazsaydık o zaman bu fonksiyon label fonksiyonu dışında kullnılamazda. Yani self eklemeliyiz ki parametreyi window üzerinde genel bir şekilde kullanabilelim"""
        
        # geometry manager
        text1.move(170,50)
        self.text2.move(170,50)        
        
        button1 = QPushButton("Change" , self)
        button1.move(170 , 100)
        button1.clicked.connect(self.button1Function)
        
    def button1Function(self):
        self.text2.setText("Hello World")
        self.text2.resize(200,25)
        """ Hello World yazmak için boyutu yetmedi biz de boyutunu arttırdık"""
        self.text2.setFont(QFont("Arial" , 25 , QFont.Bold))

    def entry(self):
        
        self.textBox = QLineEdit(self)
        """ QLineEdit object is the most commonly used input field. It provides a box in which one line of text can be entered."""
        self.textBox.setPlaceholderText("place holder")
        """ Place holder dediği şey text box ın içindeki ad soyad yazısı gibi olan şeffaf yazılar"""
        self.textBox.move(300,50)
        """ move zaten konumu belirliyor"""
        
        button1 = QPushButton("Save" , self)
        button1.move(300 , 75)
        button1.clicked.connect(self.saveFunction)

    def saveFunction(self):
        txt = self.textBox.text()
        """ self.textbox ın text inin oku"""
        if txt != "": 
            print(txt)
        else:
            print("write something")
        
    def messageBox(self):
        
        button1 = QPushButton("message" , self)
        button1.move(500,50)
        button1.clicked.connect(self , messageFunction)
        
        button2 = QPushButton("message2" , self)
        button2.move(500,75)
        button2.clicked.connect(self , messageFunction2)        
        
       
    def messageFunction(self):
        m_box = QMessageBox.question(self,"Question","Did you enjoy the course?", QMesssageBox.Yes | QMesssageBox.No | QMesssageBox.Cancel , QMesssageBox.No )

        if m_box == QMessageBox.Yes:
            print("yes")
        elif m_box == QMessageBox.No:
            print("no")
        else:
            print("cancel")
        """
        "self" = kodun window üzerinde olduğunu gösterir
        "Question" = Soru kutucuğunun ismi
        "Did you enjoy the course?" = Yarattığımız soru
        Cevapları da yes no ve cancel
        daha sonra bu fonksiyonların ne işe yaradıklarını girdik
        Eğer seçeneklerdeki vurguyu değiştirmek istersek en sona virgül koyup o seçeneği yazıyoruz
        Vurgu konusunda bir şey yazmazsak da ilk seçenek vurgulanıyor
        """    
        
    def messageFunction2(self):
        m_box = QMessageBox.information(self , "Information" , "Enjoy your course")
        
    def font(self):
        self.label = QLabel("Hello world" , self)
        self.label.move(700,100)
        """ move ile yerini belirliyoruz"""
        
        button2 = QPushButton("choose font", self)        
        button2.move(700,50)
        button2.clicked.connect(self.setfont)
        
    def setfont(self):
        font , ok = QFontDialog.getFont()
        """
        QFontDialog = Yazının boyutunu kalınlığını vs ayarlar
        2 tane variable return ediliyor 
        """
        if ok:
            self.label.setFont(font)
            self.label.resize(200,75)

    
if __name__ == '__main__':                       
    import sys 
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())                           