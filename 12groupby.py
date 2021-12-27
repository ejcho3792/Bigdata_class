# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:03:22 2021

@author: eunji
"""

# groupby method

import pandas as pd
from pandas import Series, DataFrame

kimchi=pd.read_csv('D:/빅데이터기반지능형서비스개발/12월/12월수업자료/data_bigdata_cert/kimchi_test.csv',encoding=('cp949'))

# kimchi.groupby?
'''
kimchi.groupby(
    by=None,                                                     # 그룹 할 column(기준이 됨)
    axis=0,                                                      # 연산 방향
    level=None,                                                  # 멀티 인덱스의 경우 사용
    as_index: 'bool' = True,
    sort: 'bool' = True,
    group_keys: 'bool' = True,
    squeeze: 'bool' = <object object at 0x00000195DE2B7730>,
    observed: 'bool' = False,
    dropna: 'bool' = True,
) -> 'DataFrameGroupBy'
'''
kimchi.groupby(['제품','판매처'])['수량'].sum()
kimchi.groupby(['제품'])['수량','판매금액'].sum()
kimchi2=kimchi.groupby(['제품','판매처'])['수량'].sum()
kimchi.groupby(['제품','판매처'])['수량'].agg(['sum','mean'])

kimchi.groupby(['제품','판매처'])['수량','판매금액'].agg(['sum','mean'])
kimchi.groupby(['제품','판매처'])['수량','판매금액'].agg(['sum','mean'])

kimchi.groupby(['제품','판매처'])['수량','판매금액'].agg({'수량':'sum','판매금액':'mean'})

type(kimchi2)
kimchi2.groupby(level=0).sum()
kimchi2.groupby(level='제품').sum()
kimchi2.groupby(level=1).sum()

