# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:31:02 2021

@author: danny
"""

#真值表
from typing_extensions import NotRequired
import random

input=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
target=[0,0,0,1,0,1,1,1]

class Node:
    theta=random.uniform(-1,1)
    previous=[]#前面的Link
    next=[]#後面的Link
    out=0
    def output(self):
        for input in self.previous:
            self.out+=input.fromNode.out*input.weight
        self.out+=self.theta
        return self.out
    def makeInputNode(self,out):
        self.out=out
        self.theta=0

class Link:
    fromNode=Node()
    toNote=Node()
    weight=random.uniform(-1,1)
    delta=0
    def __init__(self,fromNode,toNode):
        self.toNote=toNode
        self.fromNode=fromNode
    def trainWeight(self,target):
        temp=0
        if len(self.toNote.next)==0:
            temp=self.toNote.out-target
        else:
            for link in self.toNote.next:
                temp+=link.weight*link.delta
        self.delta=self.toNote.out*(1-self.toNote.out)*temp



















