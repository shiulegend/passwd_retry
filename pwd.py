# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:36:25 2023

@author: shiul
"""
#for i in range(1, 10):
 #   for j in range(1, 10):
  #      print("%d * %d = %d" % (i, j, i*j))
   # print()
   
password = '123456789'
i =  3 
while i > 0 :
    i = i - 1
    pwd = input('請輸入密碼 : ')
    if pwd == password:
        print('登入成功!')
        break
    else :
        print ('密碼錯誤~還有' )
        if i > 0 :
            print ('還有'  ,  i , '次機會')
        else :
            print ('沒有機會了')
   