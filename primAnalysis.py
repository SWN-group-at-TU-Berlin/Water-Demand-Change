#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:06:00 2020

@author: aco
"""

from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt


import numpy as np

import time
import pdb
import pickle
import random
import datetime 

import seaborn as sns 

import prim

import warnings; warnings.simplefilter('ignore')#


#%% drought vs all


in_file = 'data/drought_vs_all.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)
# norm_X = norm_X.iloc[:,:-9]

# Defining the Y vector
y = allFeat['Y']
y = y+1; # Activate only for binary y. PRIM has problem with 0 values apparently. 

# For discrete y
p = prim.Prim(norm_X, y, threshold=2, threshold_type="=")


box = p.find_box()
box.show_tradeoff()

plt.show()


#%% drought longterm vs rebound


in_file = 'data/drought_longterm_vs_rebound.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)
norm_X = norm_X.iloc[:,:-9]

# Defining the Y vector
y = allFeat['Y']
y = y+1; # Activate only for binary y. PRIM has problem with 0 values apparently. 

# For discrete y
p = prim.Prim(norm_X, y, threshold=5, threshold_type="=")


box = p.find_box()
box.show_tradeoff()

plt.show()



#%% drought vs recession


in_file = 'data/drought_vs_recession.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)
# norm_X.drop(columns=['group_MB', 'group_MD', 'group_SB', 'group_SD', 'consumption_extreme' ], inplace=True)
norm_X = norm_X.iloc[:,:-9]

# Defining the Y vector
y = allFeat['Y']
y.replace([1,3,4,5], [1,2,1,2], inplace=True) # Activate only for binary y. PRIM has problem with 0 values apparently. 


# For discrete y
p = prim.Prim(norm_X, y, threshold=2, threshold_type="=")


box = p.find_box()
box.show_tradeoff()

# plt.show()


#%% increase vs decrease


in_file = 'data/increase_vs_decrease.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)
norm_X = norm_X.iloc[:,:-9]

# Defining the Y vector
y = allFeat['Y']
y = y+1 # Activate only for binary y. PRIM has problem with 0 values apparently. 


# For discrete y
p = prim.Prim(norm_X, y, threshold=1, threshold_type="=")


box = p.find_box()
box.show_tradeoff()

plt.show()


#%% COVID increase vs decrease


in_file = 'data/COVID_final.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# drop no change
allFeat = allFeat.loc[(allFeat.Y_covid == 1) | (allFeat.Y_covid == 2)]

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
X = X.iloc[:,:-2]
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)


# Defining the Y vector
y = allFeat['Y_covid']
y = y+1 # Activate only for binary y. PRIM has problem with 0 values apparently. 


# For discrete y
p = prim.Prim(norm_X, y, threshold=2, threshold_type="=")  # target is increase


box = p.find_box()
box.show_tradeoff()

plt.show()

#%% COVID change vs no change


in_file = 'data/COVID_final.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()



# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
X = X.iloc[:,:-2]
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)


# Defining the Y vector
y = allFeat['Y_covid']
y = y+1 # Activate only for binary y. PRIM has problem with 0 values apparently. 


# For discrete y
p = prim.Prim(norm_X, y, threshold=1, threshold_type="=") # target is no change


box = p.find_box()
box.show_tradeoff()

plt.show()

#%% COVID increase vs no change


in_file = 'data/COVID_final.txt' # customers that decreased during the drought 


allFeat = pd.read_csv(in_file, sep=' ', engine='python')
# allFeat = allFeat.dropna()

# drop decrease
allFeat = allFeat.loc[(allFeat.Y_covid == 1) | (allFeat.Y_covid == 0)]

# delete race features
allFeat = allFeat.drop(columns=['White %', 'Black %', 'American Native %', 'Asian %', 'Hawaiin %'])



# Defining the X matrix
X = allFeat.iloc[:,0:-1] 

# Standardize features
scaled_X = (allFeat-allFeat.mean())/allFeat.std() 

# MinMax scaling features
X = X.iloc[:,:-2]
norm_X = (X-X.min())/ (X.max()-X.min())
norm_X.fillna(0, inplace=True)


# Defining the Y vector
y = allFeat['Y_covid']
y = y+1 # Activate only for binary y. PRIM has problem with 0 values apparently. 


# For discrete y
p = prim.Prim(norm_X, y, threshold=1, threshold_type="=") # target is no change


box = p.find_box()
box.show_tradeoff()

plt.show()


#%%

# For discrete y
p = prim.Prim(norm_X, y, threshold=5, threshold_type="=")


box = p.find_box()
box.show_tradeoff()

plt.show()


