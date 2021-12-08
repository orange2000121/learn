# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:16:41 2021

@author: danny
"""
#畫每個數字的圖
def one(case):
    if case==0:  
        print('  * ',end=' ')
    elif case==1:  
        print('  * ',end=' ')
    elif case==2:
        print('  * ',end=' ')
    elif case==3:
        print('  * ',end=' ')
    else:
        print('  * ',end=' ')
    return 0
def two(case):
    if case==0:  
        print('*** ',end=' ')
    elif case==1:  
        print('   *',end=' ')
    elif case==2:
        print(' ** ',end=' ')
    elif case==3:
        print('*   ',end=' ')
    else:
        print('****',end=' ')
    return 0
def three(case):
    if case==0:  
        print('*** ',end=' ')
    elif case==1:  
        print('   *',end=' ')
    elif case==2:
        print('*** ',end=' ')
    elif case==3:
        print('   *',end=' ')
    else:
        print('*** ',end=' ')
    return 0
def four(case):
    if case==0:  
        print('* * ',end=' ')
    elif case==1:  
        print('* * ',end=' ')
    elif case==2:
        print('****',end=' ')
    elif case==3:
        print('  * ',end=' ')
    else:
        print('  * ',end=' ')
    return 0
def five(case):
    if case==0:  
        print(' ***',end='  ')
    elif case==1:  
        print('*   ',end='  ')
    elif case==2:
        print(' ** ',end='  ')
    elif case==3:
        print('   *',end='  ')
    else:
        print('*** ',end='  ') 
    return 0
def six(case):
    if case==0:  
         print('  **',end=' ')
    elif case==1:  
        print(' ** ',end=' ')
    elif case==2:
         print('*  *',end=' ')
    elif case==3:
        print('*  *',end=' ')
    else:
        print(' ** ',end=' ')
    return 0
def seven(case):
    if case==0:  
        print('****',end=' ')
    elif case==1:  
       print('*  *',end=' ')
    elif case==2:
        print('   *',end=' ')
    elif case==3:
        print('   *',end=' ')
    else:
        print('   *',end=' ')
    
    
    
    
    
    return 0
def eight(case):
    if case==0:  
        print(' ** ',end=' ')
    elif case==1:  
       print('*  *',end=' ')
    elif case==2:
        print(' ** ',end=' ')
    elif case==3:
        print('*  *',end=' ')
    else:
        print(' ** ',end=' ')
    
    
    
    
    
    return 0
def nine(case):
    if case==0:  
        print(' ** ',end=' ')
    elif case==1:  
       print('*  *',end=' ')
    elif case==2:
        print(' ** ',end=' ')
    elif case==3:
        print('   *',end=' ')
    else:
        print('  * ',end=' ')
    
    
    
    
    
    return 0
def zero(case):
    if case==0:  
        print(' ** ',end=' ')
    elif case==1:  
       print('*  *',end=' ')
    elif case==2:
         print('*  *',end=' ')
    elif case==3:
        print('*  *',end=' ')
    else:
        print(' ** ',end=' ')
    
    
   
    
    
a=input('輸入一段整數')
for j in range(5):#每個數字一段一段印出來
    for i in range(len(a)):
        if(a[i]=='1'):
            one(j)
        elif(a[i]=='2'):
            two(j)
        elif(a[i]=='3'):
            three(j)
        elif(a[i]=='4'):
            four(j)
        elif(a[i]=='5'):
            five(j)
        elif(a[i]=='6'):
            six(j)
        elif(a[i]=='7'):
            seven(j)
        elif(a[i]=='8'):
            eight(j)
        elif(a[i]=='9'):
            nine(j)
        elif(a[i]=='0'):
            zero(j)
    print()

















