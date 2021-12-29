# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:55:03 2021

@author: eunji
"""

# NA 결측치 처리 중복값 제거

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

s1=Series([1,2,3,np.nan])
s2=Series(['a','b','c',np.nan])

s1.mean()
s1.fillna(0)

s2.replace(np.nan,'a')
# 조건색인
s1[s1.isnull()]=0

s3=Series(['서울','.','대전','.','대구','.','부산'])
s3=s3.replace('.',np.nan)\
    
s3.fillna(method='ffill')

s3.fillna(method='bfill')

df1=DataFrame(np.arange(1,17).reshape(4,4),columns=list('ABCD'))
df1.iloc[0,0]=np.nan
df1.iloc[1,[0,1]]=np.nan
df1.iloc[2,[0,1,2]]=np.nan
df1.iloc[3,:]=np.nan

df1.dropna()
df1.dropna(how='any')
df1.dropna(how='all')

df1.dropna(thresh=2)
df1.dropna(axis=1,how='any')

df1.dropna(subset=['C'])


# 중복값 처리
s1=pd.Series([1,1,2,3,4])
s1.unique()

s1.duplicated()
s1.drop_duplicates()

df2=pd.DataFrame({'A':[1,1,3,4],'B':[10,10,30,40]})

df2.drop_duplicates()

df3=pd.DataFrame({'A':[1,1,3,4],'B':[10,10,30,40],'C':[100,200,300,400]})

df3.drop_duplicates()# 모든 컬럼 일치해야함

df3.drop_duplicates(subset=['A','B'])

df3.drop_duplicates(subset=['A','B'],keep='last')