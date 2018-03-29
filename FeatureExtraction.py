__author__ = 'zhangzhan'
# -*- coding: utf-8 -*-
# 每个点提取114个特征
# 2016.4.7
import sys
import numpy as np
import codecs
import csv
import os
from numpy import zeros
from numpy import genfromtxt
from scipy import stats
currentDir = os.getcwd()
# 从原始数据中读取数据
def dataExtractor(rootName, dirName):
    print("Data Reading............")
    # 点的序号
    result = []
    for i in ["03"]:
        print(i)
        with codecs.open("%s/%s/%s.csv" % (rootName, dirName, i), "r") as fp:

            for line in fp.readlines():
                line = line.strip("\r\t\n").split(",")
                res = []
                headX = line[4041]
                headY = line[4042]
                headZ = line[4043]

                for p in range(10):
                    valueX = float(line[3 * p]) - float(headX)
                    valueY = float(line[3 * p + 1]) - float(headY)
                    valueZ = float(line[3 * p + 2]) - float(headZ)

                    res.append(valueX)
                    res.append(valueY)
                    res.append(valueZ)
                result.append(res)
    data = np.array(result)
    print("Row = %d, Column = %d" % (data.shape[0], data.shape[1]))
    print(data)
    return data


if __name__ == "__main__":
    rootName = "C:\\Users\\Administrator\\Desktop\\abc.xlsx"
    dirList = os.listdir(rootName)
    usrList = []
    for dirName in dirList:
                # 读取面部数据
                faceData = dataExtractor(rootName, dirName)
