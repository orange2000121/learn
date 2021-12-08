# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:54:56 2020

@author: danny
"""

class Node():
    '''節點'''
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Linked_list():
    '''鏈結串列'''
    def __init__(self):
        self.head=None
        
    def print_list(self):
        '''列印鏈結串列'''
        ptr=self.head
        while ptr:
            print(ptr.data)
            ptr=ptr.next
    
    def length(self):
        '''計算長度'''
        ptr=self.head
        count=1
        while ptr:
            if(ptr.next):
                count+=1
            ptr=ptr.next
        print('length:',count)

link=Linked_list()
link.head=Node(5)
n2=Node(15)
n3=Node(25)
link.head.next=n2
n2.next=n3
link.print_list()
link.length()