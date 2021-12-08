# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:11:00 2020

@author: danny
"""
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

df_test=pd.read_csv('titanic_test.csv')
df_train=pd.read_csv('titanic_train.csv')

model=Sequential()
model.add(Dense(10,input_shape=(8,),activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
model.summary()