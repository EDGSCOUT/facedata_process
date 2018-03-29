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
             #if re.search('AU',child,re.M|re.I)!=None and re.search('test',child,re.M|re.I)==None:
             if re.search('AU', child, re.M | re.I) != None or \
                     re.search('log', child, re.M | re.I) != None\
                     or re.search('BDI', child, re.M | re.I) != None\
                      or re.search('实验记录表', child, re.M | re.I) != None:
                 continue
             else:
              os.remove(child)


if __name__ == '__main__':
    filePathC = "E:\\AnDing\\VoiceData"

    eachFile(filePathC)