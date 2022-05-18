# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:10:10 2022

@author: ezgis
"""

import random 

aa = random.random() # Default olarak 0 ve 1 arasında float sayı üretir. 0 dahil 1 dahil değil
bb = random.uniform(1,10) # 1 ve 10 arasında float sayı üretir. 1 dahil 10 dahil değil
cc = random.randint(1,10) # 1 ve 10 arasında int sayı. 1 ve 10 dahil
dd = random.randrange(0,101,2) 

random.seed(2) # Rastgele sayı ürettikten sonra her bastığımızda değişmez

