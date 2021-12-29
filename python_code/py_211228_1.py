# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:16:06 2021

@author: eunji
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

pd.read_csv('./data/emp.csv')
emp.loc[emp['ename']=='scott']
emp.loc[~(emp['ename']=='scott'),:]
emp.drop(4,axis=0)

#emp에서 sal 컬럼 제외(iloc)
emp.drop('sal',axis=1)
emp.iloc[:,0:3]
emp.iloc[:,:-1]

emp.loc[:,'empno':'deptno']

emp.drop(['ename','deptno'],axis=1)

# shift
emp['sal'].shift()

# 데이터프레임에서 전일자 대비 증강율

s1=Series([3000,3500,4200,2000,3600],index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
((s1-s1.shift())/s1.shift())*100

# rename
emp.columns=['emptno','ename','deptno','salary']
emp

emp.rename({'salary':'sal','deptno':'dept_no'},axis=1)

# emp data ename을 index로 설정 후 scott을 SCOTT으로 변경

emp.set_index('ename').rename({'scott':'SCOTT'})
