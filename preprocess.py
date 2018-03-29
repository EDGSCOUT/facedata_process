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
# 遍历指定目录，显示目录下的所有文件名
def eachFile2(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        if os.path.isdir(child):
            eachFile(child)
        else:
            '''
             #if re.search('AU',child,re.M|re.I)!=None and re.search('test',child,re.M|re.I)==None:
             if re.search('AU', child, re.M | re.I) != None or \
                     re.search('log', child, re.M | re.I) != None\
                     or re.search('BDI', child, re.M | re.I) != None\
                      or re.search('实验记录表', child, re.M | re.I) != None:'''
            if re.search('log', child, re.M | re.I) != None:
                print(child)
                readFile1(child, filepath)
            # else:
            # os.remove(child)

#def readFile1(filename,filepath):


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        if os.path.isdir(child):
         eachFile(child)
        else:
            '''
             #if re.search('AU',child,re.M|re.I)!=None and re.search('test',child,re.M|re.I)==None:
             if re.search('AU', child, re.M | re.I) != None or \
                     re.search('log', child, re.M | re.I) != None\
                     or re.search('BDI', child, re.M | re.I) != None\
                      or re.search('实验记录表', child, re.M | re.I) != None:'''
            if re.search('AU', child, re.M | re.I) != None:
                 print(child)
                 readFile(child,filepath)
             #else:
                #os.remove(child)


# 读取文件内容并打印
def readFile(filename,filepath):
 Line=[]
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
 variance=[0]*19
 average=[0]*19
 print(sum)
 for j in range(0,y-1):
     for i in range(1,x):
        #print(Lines[i][j])
        sum[j]=float(Lines[i][j])+sum[j]
        if float(Lines[i][j])>max[j]:
             max[j]=float(Lines[i][j])
        if float(Lines[i][j])<min[j]:
              min[j]=float(Lines[i][j])
     average[j]=sum[j]/x
 for j in range(0, y - 1):
      for i in range(1, x):
        # print(Lines[i][j])
        variance[j] = (float(Lines[i][j]) -average[j])
 file=filepath+'\\test.csv'
 fp = open(file, 'a')
 '''print('总和', sum[j])
 print('均值', average[j])
 print('最大值', max[j])
 print('最小值', min[j])
 '''
 for j in range(0, y - 1):
     fp.write(str(sum[j])+',')
     fp.write(str(max[j]) + ',')
     fp.write(str(min[j]) + ',')
     fp.write( str(average[j]) + ',')
     fp.write( str(variance[j]) + ',')
 fp.write('\n')




if __name__ == '__main__':
    filePathC = "E:\\AnDing\\VoiceData"

    eachFile(filePathC)