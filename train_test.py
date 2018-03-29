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
reg = linear_model.LinearRegression()
reg.fit ([[0, 0]], [0])
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(reg.coef_)

