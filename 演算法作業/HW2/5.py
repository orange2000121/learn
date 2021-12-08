# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:54:33 2020

@author: danny
"""

class CreatBankAccount:
    #定義id name balance
    def __init__(self,ide=None,name=None,balance=0):
        self.ide=ide
        self.name=name
        self.balance=balance
    #提款
    def Withdrawal(self,money):
        self.balance-=money
        print('name:',self.name,'餘額:',self.balance)
    #存款
    def deposit(self,money):
        self.balance+=money
        print('name:',self.name,'餘額:',self.balance)
    #匯款
    def remittance(self,to,money):
        self.Withdrawal(money)
        to.deposit(money)

s1=CreatBankAccount(ide='001',name='Joe')
s2=CreatBankAccount(ide='002',name='marry')
print('存1000')
s1.deposit(1000)
print('提100')
s1.Withdrawal(100)
print('Joe賄款給Marry50')
s1.remittance(s2, 50)