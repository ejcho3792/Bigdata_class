# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:29:20 2021

@author: eunji
"""

# stack unstack, pivot_table

# 자료구조 형태
# 

import pandas as pd

kimchi=pd.read_csv('./data/kimchi_test.csv',encoding='cp949')

df1=kimchi.groupby(['판매년도','제품'])['수량'].sum()

df2=df1.unstack()

df2.stack()

df1.unstack(level=0)

kimchi.pivot_table(index='판매원',
                   columns='판매처',
                   values='수량',
                   aggfunc='sum')

# exe - kimchi데이터의 연도별, 제품별 판매금액의 총 합을 교차표로 작성

kimchi.pivot_table(index='판매년도',
                   columns='제품',
                   values='판매금액'
                   aggfunc='sum')
