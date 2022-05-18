# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:02:03 2022

@author: ezgis
"""

## Matplotlib  -  Çizim kütüphanesi

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)      
y=np.linspace(-5,5,100)

fig = plt.figure()
ax = fig.add_subplot(111) # => satır , sütun , grid boyutuna göre kaç tane resim geleceği
                          # => parantez içi (236) olsaydı o zaman da 2*3 ten 6 resim koyulabilirdi

ax.plot(x,y, color = "red" , linewidth=3)

ax.scatter(x,y,color = "green" , marker = "*") # => saçmak, dağıtmak

plt.xlabel("x")
plt.xlabel("x")
plt.title("x vs y")
plt.savefig("x_y.png") # => fig = figure
plt.show()


## Seaborn - Görselleştirme kütüphanesi - High Level Interface

import seaborn as sns
a = np.random.randint(5,size=1000)

plt.figure()
sns.countplot(a) # countplot => sayım grafiği    

