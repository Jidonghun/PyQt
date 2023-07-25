# pip install scipy
# pip install matplotlib
# pip install numpy

import sys 
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
from scipy.stats import pearsonr, stats
import matplotlib.pyplot as plt

x1 = input('양의 정수 입력(스페이스로 구분: ').split()
x2 =[]
for x in x1:
    x2.append(float(x))

y1 = input('양의 정수 입력(스페이스로 구분: ').split()
y2 =[]
for y in y1:
    y2.append(float(y))
    
x3 = np.array(x2)           # np.array로 변환

plt.scatter(x2, y2)         # 입력받은 변수들의 산점도
plt.title('correlation coefficient')        # 그래프 제목
plt.xlabel('X')         # x축 이름
plt.ylabel('Y')         # Y축 이름
        
r, p = stats.pearsonr(x2, y2)     # Pearson 상관계수
m, b = np.polyfit(x2, y2, 1)
plt.annotate('r = {:.2f}'.format(r), xy=(0.8, 0.9), xycoords='axes fraction')    
plt.plot(x2, m*x3+b, color='red') # 회귀식
plt.show()



# # 난수
# x = np.random.randn(30)
# y = np.random.randn(30)

# plt.scatter(x, y)
# plt.title('correlation coefficient')
# plt.xlabel('X')
# plt.ylabel('Y')

# r, p = stats.pearsonr(x, y)     #상관계수
# m, b = np.polyfit(x, y, 1)
# plt.annotate('r = {:.2f}'.format(r), xy=(0.8, 0.9), xycoords='axes fraction')    
# plt.plot(x, m*x+b, color='red') # 회귀식
# plt.show()