# -*- coding: UTF-8 -*-
import os
import re
import csv
import pandas as pd
import numpy as np
import pyexcel_io
from pyexcel_xls import get_data
from pyexcel_xls import save_data
import xlrd

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        if os.path.isdir(child):
         eachFile(child)
        else:
            if re.search('feature', child, re.M | re.I) != None:
                #print(child)
                readFile(child,filepath)
             #else:
                #os.remove(child)



def readFile(filename,child):
 Line=[]
 fopen = open(filename, 'r') # r 代表read
 for eachLine in fopen:
    lines=eachLine.split(',')
    Line.append(lines)
 fopen.close()
 Lines=np.array(Line)
 x=Lines.shape[0]
 y=Lines.shape[1]
 Q=np.array(Lines)
 for i in range(x):
     for j in range(y):
         if(j==y-1):
             Q[i][j] = int(Lines[i][j])
         else:
            Q[i][j]=float(Lines[i][j])
 I = np.argsort(Q[:,68])
 P=Q[I,:]
 #print(filepath)
 #print(Lines)
 file = child + '\\order.csv'
 fp = open(file, 'w')
 x=P.shape[0]
 y = P.shape[1]
 print(y)
 for i in range(x):
     for j in range(y):
         if j == y - 1:
             fp.write(P[i][j]+'\n')
         else:
             fp.write(P[i][j] + ',')
     # fp.write('\n')
     # print(d)


if __name__ == '__main__':
     filePathC = "E:\\AnDing\\VoiceData"

     eachFile(filePathC)