# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 10:20:54 2021

@author: danny
"""

num=int(input('金額:'));#輸入金額
hundred=int(num/100);#除一百得整數部分
num-=hundred*100;#扣除百位以上
fifty=int(num/50);#除五十得整數部分
num-=fifty*50;#扣除剩下五十的倍數
ten=int(num/10);#除十得整數部分
num-=ten*10;#扣除剩下十的倍數
print('可換:')
print('百元:',hundred,'五十:',fifty,'十元:',ten);#輸出答案