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
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def eachFile(filepath):
    data1=[]
    data2=[]
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join("%s\%s" % (filepath, allDir))
        if os.path.isdir(child):
         eachFile(child)
        else:
            if re.search('order', child, re.M | re.I) != None:
                 print(child)
                 readFile(child,filepath)
            if re.search('实验记录表', child, re.M | re.I) != None:
                 print(child)
                 readFile1(child,filepath)

    #train(data1,data2)


             #else:
                #os.remove(child)
    #reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

# 读取文件内容并打印
def readFile1(filename,filepath):
 Line=[]
 fopen = open(filename, 'r', encoding='UTF-8') # r 代表read

 for eachLine in fopen:
     #lines = eachLine.split(',')
     if re.search('PHQ-9分数',eachLine, re.M | re.I)!=None:
        #print(eachLine)
        line=eachLine.split('：')
        #print(line[1])
        PK.append(float(line[1]))

 fopen.close()
 #print(P)
 #return P

def train(X,Y):
    reg.fit(X,Y)

def readFile(filename,filepath):
    Line = []
    fopen = open(filename, 'r')  # r 代表read
    for eachLine in fopen:
        lines = eachLine.split(',')
        Line.append(lines)
    fopen.close()
    Lines = np.array(Line)
    x=Lines.shape[0]
    y=Lines.shape[1]
    k=0
    P=[0]*(x*y)
    #P=np.array(P,type=float)
    for i in range(x):
        for j in range(y):
            P[k]=float(Lines[i][j])
            k=k+1
    #print(P)
    Q.append(P)
    #T=np.array(Q)
    #print(T)
    #return T



if __name__ == '__main__':
    reg = linear_model.LinearRegression()
    filePathC = "E:\\AnDing\\VoiceData"
    Q=[]
    PK = []
    #print(Q)
    eachFile(filePathC)
    Q=np.array(Q)
    print(Q.shape[0])
    #print('--------',Q)
    PK=np.array(PK)



    #print('--------',PK.shape[0])
    #train(Q,PK)
    #print(len(reg.coef_))
   # for i in range(len(reg.coef_)):
    #    print(reg.coef_[i])
    #print(len(reg.coef_))
    #Q=np.array(reg.coef_).tostring()
    #print(Q)
    #fp = open("test", 'w')
    #fp.write(Q)
    '''
    diabetes_train = Q[:-4]
    diabetes_test = Q[-4:]
    #print(type(diabetes_test))
    # Split the targets into training/testing sets
    diabetes_y_train = PK[:-4]
    diabetes_y_test = PK[-4:]
    #print(type(diabetes_y_test))
    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(Q,PK)
    '''
    '''
    print('diabetes_X_train')
    print(diabetes_train)
    print('diabetes_y_train')
    print(diabetes_y_train)
    '''
    # Make predictions using the testing set
    #diabetes_y_pred = regr.predict(diabetes_X_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    #print("Mean squared error: %.2f"
    #      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # Explained variance score: 1 is perfect prediction
   # print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
   '''