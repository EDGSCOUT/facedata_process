import sys
import numpy as np
import codecs
import csv
import os
from numpy import zeros
from numpy import genfromtxt
from scipy import stats

fopen = open("C:\\Users\\Administrator\\Desktop\\AU05.csv", 'r')  # r 代表read
Line=[]
Lines=[]
for eachLine in fopen:
    lines = eachLine.split(',')
    Line.append(lines)
#print(Line)
Line=np.array(Line)
I = np.argsort(Line[:,2])
P=Line[I,:]
print(Line)
print(P)


#[b,I] = sortrows(a,i)

#I = argsort(a[:,i]), b=a[I,:]
''' Line.append(lines)
  fopen.close()
  Lines=np.array(Line)
  x=Lines.shape[0]
  y=Lines.shape[1]'''


