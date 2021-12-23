# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:12:17 2021

@author: eunji
"""

import numpy as np 

np.array([1,2,3])
np.array([[1,2,3],[4,5,6],[7,8,9]])
np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
np.arange(1,26).reshape(5,5)
a1=np.arange(1,26)
type(a1)
#
a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2[1,:]
a2[:,1]   #정수색인;차원축소발생
a2[:,1:2] #슬라이스색인;차원축소없음
a2[[0,2],:]
a2[:,[0,2]]
a2[1,1]
a2[[1,2],[1,2]]
aa=a2[np.ix_([1,2],[1,2])]
aaa=a2[1:3,1:3]
a2[:,0]>5
a2[a2[:,0]>5]
#
a2.dtype
a2.shape
a2.shape[0]
a2.shape[1]

sum(np.diag(a2))
a=np.array([[1,2,3]])
np.swapaxes(a,0,1)
