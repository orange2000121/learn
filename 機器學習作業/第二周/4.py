# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:22:34 2020

@author: danny
"""
#畫每個數字的圖
def one():
    print('  * ')
    print('  * ')
    print('  * ')
    print('  * ')
    print('  * ')
    return 0
def two():
    print('*** ')
    print('   *')
    print(' ** ')
    print('*   ')
    print('****')
    return 0
def three():
    print('*** ')
    print('   *')
    print('*** ')
    print('   *')
    print('*** ')
    return 0
def four():
    print('* * ')
    print('* * ')
    print('****')
    print('  * ')
    print('  * ')
    return 0
def five():
    print(' ***')
    print('*   ')
    print(' **')
    print('   *')
    print('*** ') 
    return 0
def six():
    print('  **')
    print(' ** ')
    print('*  *')
    print('*  *')
    print(' ** ')
    return 0
def seven():
    print('****')
    print('*  *')
    print('   *')
    print('   *')
    print('   *')
    return 0
def eight():
    print(' ** ')
    print('*  *')
    print(' ** ')
    print('*  *')
    print(' ** ')
    return 0
def nine():
    print(' ** ')
    print('*  *')
    print(' ** ')
    print('   *')
    print('  * ')
    return 0
def zero():
    print(' ** ')
    print('*  *')
    print('*  *')
    print('*  *')
    print(' ** ')
a=input('輸入一段整數')
for i in range(len(a)):
    if(a[i]=='1'):
        one()
        print()
    elif(a[i]=='2'):
        two()
        print()
    elif(a[i]=='3'):
        three()
        print()
    elif(a[i]=='4'):
        four()
        print()
    elif(a[i]=='5'):
        five()
        print()
    elif(a[i]=='6'):
        six()
        print()
    elif(a[i]=='7'):
        seven()
        print()
    elif(a[i]=='8'):
        eight()
        print()
    elif(a[i]=='9'):
        nine()
        print()
    elif(a[i]=='0'):
        zero()
        print()

















