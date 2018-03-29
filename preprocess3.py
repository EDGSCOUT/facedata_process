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
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        pathDir1 = os.listdir(child)
        data1=[]
        data2=[]
        for allDir1 in pathDir1:
                child1 = os.path.join("%s\%s" % (child, allDir1))
                if  re.search('log', child1, re.M | re.I) != None:
                  print(child1)
                  #d='你好'
                  data1=readFile1(child1, filepath)
                  #print(data1)
                  #readFile1(child1, filepath)
                if re.search('test', child1, re.M | re.I) != None:
                  #print(child1)
                  data2=readFile2(child1,filepath)
                  #print(data2)
        #print(data1)
        #print(data2)

        file = child + '\\feature.csv'
        fp = open(file, 'w')
        print(type(data2))
        #data2=np.array(data2)
        y = data2.shape[1]
        print(y)
        for i in range(21):
         for j in range(y):
             if j==y-1:
                 fp.write(str(data1[i])+'\n')
             else:
                  fp.write(data2[i][j] + ',')
         #fp.write('\n')
            #print(d)

            # else:
            # os.remove(child)


# 读取文件内容并打印
def readFile1(filename,filepath):
 Line=[]
 fopen = open(filename, 'r', encoding='UTF-8') # r 代表read
 for eachLine in fopen:
    #print(eachLine)
    lines = eachLine.split(',')
    Line.append(lines)
 Lines=np.array(Line)
 #print(Lines)
 Sign=[0]*55
 for i in range(Lines.shape[0]):
      #print(Lines[i])
      if Lines[i]=='正性视频\n':
          Sign[i]=1
      if Lines[i]=='中性视频\n':
          Sign[i]=2
      if Lines[i]=='负性视频\n':
          Sign[i]=3
      if Lines[i] == '正性访谈问题1\n':
          Sign[i] = 4
      if Lines[i] == '正性访谈问题2\n':
          Sign[i] = 5
      if Lines[i] == '正性访谈问题3\n':
          Sign[i] = 6
      if Lines[i] == '中性访谈问题1\n':
          Sign[i] = 7
      if Lines[i] == '中性访谈问题2\n':
          Sign[i] = 8
      if Lines[i] == '中性访谈问题3\n':
          Sign[i] = 9
      if Lines[i] == '负性访谈问题1\n':
          Sign[i] = 10
      if Lines[i] == '负性访谈问题2\n':
          Sign[i] = 11
      if Lines[i] == '负性访谈问题3\n':
          Sign[i] = 12
      if Lines[i] == '正性朗读\n':
          Sign[i] = 13
      if Lines[i] == '中性朗读\n':
          Sign[i] = 14
      if Lines[i] == '负性朗读\n':
          Sign[i] = 15
      if Lines[i] == '正性表情图片\n':
          Sign[i] = 16
      if Lines[i] == '中性表情图片\n':
          Sign[i] = 17
      if Lines[i] == '负性表情图片\n':
          Sign[i] = 18
      if Lines[i] == '正性图片\n':
          Sign[i] = 19
      if Lines[i] == '中性图片\n':
          Sign[i] = 20
      if Lines[i] == '负性图片\n':
          Sign[i] = 21
 #print(Sign)
 Sign=Sign[0:21]
 return Sign

# 读取文件内容并打印
def readFile2(filename,filepath):
 Line=[]
 fopen = open(filename, 'r') # r 代表read
 for eachLine in fopen:
    lines=eachLine.split(',')
    Line.append(lines)
 fopen.close()
 Lines=np.array(Line)
 x=Lines.shape[0]
 y=Lines.shape[1]
 #print(Lines[1])
 print('Lines',type(Lines))
 return Lines




if __name__ == '__main__':
    filePathC = "E:\\AnDing\\VoiceData"
    filePath = "E:\\AnDing\\VoiceData\\2110104\\AU01.csv"
    filePathI = "D:\\FileDemo\\Python\\pt.py"

    eachFile(filePathC)