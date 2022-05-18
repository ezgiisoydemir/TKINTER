# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:35:02 2022

@author: ezgis
"""

## i/o

save_txt = "hello world"
text_file = open ("save_string.txt" , "w")
text_file.write(save_txt)
text_file.close()

## load
load_file = open("save_string.txt","r")
print(load_file.read())                       