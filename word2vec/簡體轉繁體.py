# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:14:27 2019

@author: User
"""

from opencc import OpenCC

def translate(transFile,outputFile):
    cc = OpenCC('s2t')
    source = open(transFile, 'r', encoding = 'utf-8')
    result = open(outputFile, 'w', encoding = 'utf-8')
    #source就放純文字檔，轉完就放進去result
    count = 0
    while True:
        line = source.readline()
        line = cc.convert(line)
        if not line:  #readline會一直讀下去，這邊做的break
            break
        print(line)
        count = count +1
        result.write(line) 
        print('===已處理'+str(count)+'行===')
    source.close()        
    result.close()

translate("wiki_texts2.txt","wiki_zh_tw2.txt")