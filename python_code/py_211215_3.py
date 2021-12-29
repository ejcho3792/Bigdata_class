# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:23:24 2021

@author: eunji
"""
###############################
# 사용자 정의 함수             #
###############################
#
def f_nul(x):
    v1=x*10
    return v1
f_nul(100)
def f_2_nul(x,y):
    res=x*y
    return res
f_2_nul(2,10)
#
f1=lambda x: x*10
f1(6)
f2=lambda x,y,z:(x+y)*z
f2(2,5,3)
#
f1=lambda x:x*10
f1(4)
l1=[1,2,5,10]
f1(l1)
#
l2=[]
for i in l1:
    l2.append(i+10)
print(l2)
#
f1(4)
list(map(f1,l1))
#
l2=[3,5,7,10]

def f3(x):
    if x>10:
        v1=x*3
    else:
        v1=x*2
    return v1
list(map(f3,l2))
