import os
import re
import csv
import pandas as pd
import numpy as np
import pyexcel_io
from pyexcel_xls import get_data
from pyexcel_xls import save_data
import xlrd
Line=[]
L=[]
def readFile(filename):
 fopen = open(filename, 'r') # r 代表read
 for eachLine in fopen:
    lines=eachLine.split(',')
    Line.append(lines)
 fopen.close()
 Lines=np.array(Line)
 x=Lines.shape[0]
 y=Lines.shape[1]
 #print(x)
 #print(y)
 sum=[0]*19
 max=[-100]*19
 min=[100]*19
 print(sum)
 for j in range(0,y-1):
     for i in range(1,x):
        #print(Lines[i][j])
        sum[j]=float(Lines[i][j])+sum[j]
        if float(Lines[i][j])>max[j]:
             max[j]=float(Lines[i][j])
        if float(Lines[i][j])<min[j]:
              min[j]=float(Lines[i][j])
     print(sum[j])
     print(sum[j]/x)
     print(max[j])
     print(min[j])
 return Lines




#滑动平均滤波，窗口大小设置为3
def removeNoise(Lines):

    print ("Denoising............")
    #矩阵的行数与列数
    x = data.shape[0]
    y= data.shape[1]

    for j in range(0, y - 1):
        for i in range(1, x):
            # print(Lines[i][j])
            sum[j] = float(Lines[i][j]) + sum[j]
            if float(Lines[i][j]) > max[j]:
                max[j] = float(Lines[i][j])
            if float(Lines[i][j]) < min[j]:
                min[j] = float(Lines[i][j])


















if __name__ == '__main__':
    filePath = "C:\\Users\\Administrator\\Desktop\\AU05.csv"
    #filePath = "AU12.csv"
    data=readFile(filePath)
    removeNoise(data)

