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
from sklearn import linear_model

def eachFile(filepath):
    data1=[]
    data2=[]
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        if os.path.isdir(child):
         eachFile(child)
        else:
            #print(child)
            if re.search('order', child, re.M | re.I) != None:
                 print(child)
                 #data1=readFile(child,filepath)
            if re.search('实验记录表', child, re.M | re.I) != None:
                 print(child)
                 readFile1(child,filepath)


def readFile1(filename,filepath):
 print(filename)
 #filname=filename.encode('utf-8')
 Line=[]
 #print(filename)
 fopen = open(filename, 'r',encoding= 'utf-8') # r 代表read
# P=fopen.readline()

 #print(P)
 for eachLine in fopen:
     #lines = eachLine.split(',')
     #eachLine=eachLine.encode('utf-8')
     #print(eachLine)
     if re.search('PHQ-9分数', eachLine, re.M | re.I)!=None:
        print(eachLine)
        line=eachLine.split('：')
        print(line[1])
 fopen.close()


if __name__ == '__main__':

    filePathC = "E:\\AnDing\\VoiceData"

    eachFile(filePathC)
    #print(reg.coef_)