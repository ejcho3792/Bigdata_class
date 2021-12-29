# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:26:08 2021

@author: eunji
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

np.arange(1,7)
np.arange(1,7).reshape(2,3)

df1=DataFrame(np.arange(1,7).reshape(2,3),columns=['A','B','C'])
df2=DataFrame(np.arange(10,61,10).reshape(2,3),columns=['A','B','C'])

# concat
pd.concat([df1,df2])
pd.concat([df1,df2],axis=1)
pd.concat([df1,df2],ignore_index=True)

#emp
emp=pd.read_csv('D:/빅데이터기반지능형서비스개발/12월/12월수업자료/data_bigdata_cert/emp.csv')
emp


#merge
df_dept=DataFrame({'deptno':[10,20,30],'dname':['인사부','총무부','IT부서']})
pd.merge(emp,df_dept, on='deptno')

df_dept_new=DataFrame({'deptno':[10,20],'dname':['인사총무','IT']})
pd.merge(emp,df_dept_new, on='deptno')
pd.merge(emp,df_dept_new, on='deptno',how='outer')
pd.merge(emp,df_dept_new, on='deptno',how='left')
