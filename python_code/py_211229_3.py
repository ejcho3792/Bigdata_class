# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:04:35 2021

@author: eunji
"""

#pandas 연습
import pandas as pd
df1=pd.read_csv('./data/cancer_test.csv')
df1.columns
df1.dtypes
df1.head()
df1.info
df1.describe()
############################################################################1번
# radius_mean, texture_mean, texture_se, smoothness_se
# nan 제거하고 총 행의 수 리턴

df1['radius_mean'].isnull().sum()
df1['texture_mean'].isnull().sum()
df1['texture_se'].isnull().sum()
df1['smoothness_se'].isnull().sum()

# 1)
vbool=df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum()
df1.loc[vbool,:]
# print(df1.shape[0]-vbool.sum())
print(df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all').shape[0])

############################################################################2번
# concavity_mean의 standard scaling(표준화) 후 결과가 0.1이상인 개수 출력
v_sc=(df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean'].std()
print((v_sc>0.1).sum())

########################################################################3####3번
# 이상치 건수 확인
# 이상0치 :  nan 제외 상위 10%일때
# 이상치(상위 10%)를 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

import numpy as np
nx=int(np.trunc(df1['texture_se'].dropna().shape[0]*0.1)) #상위 10% 개수 56개
ran=df1['texture_se'].rank(ascending=False, method='first')
df1.loc[ran>nx,'texture_se']           # 정상 데이터
mx=df1.loc[ran>nx,'texture_se'] .max()
df1.loc[~(ran>nx),'texture_se']        # 이상치

df1.loc[~(ran>nx),'texture_se']=mx

print('%.2f'%df1['texture_se'].mean())

#######################################4번
#symmetry_mean의 결측치를 최솟값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력
df1['symmetry_mean'].min()

from numpy import nan
ddd=df1['symmetry_mean']
df1['symmetry_mean']=df1['symmetry_mean'].replace(['-','.','pass'],nan)
df1['symmetry_mean']=df1['symmetry_mean'].astype('float').min()
df1['symmetry_mean']=df1['symmetry_mean'].fillna(df1['symmetry_mean'].min())

print('%.2f'%df1['symmetry_mean'].mean())






