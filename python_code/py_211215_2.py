# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:38:25 2021

@author: eunji
"""
###############################
# 조건문과 반복문              #
###############################
#
v1=1
(v1>=3)and(v1<=7)
(v1>=3)&(v1<=7)
(v1<=3)or(v1>=7)
(v1<=3)|(v1>=7)
not(v1==1)
#
v1=10
if v1>5:
    print('A')
else:
    print('B')
l1=[1,3,5,7,8]
if l1>5:
    print('A')
else:
    print('B')
#
for i in range(10):
    print(i+1)
#
l1=[1,3,5,15,25]
for i in l1:
    if i>5:
        print('A')
    else:
        print('B')
for i in l1:
    print(i+10)
l2=[]
for i in l1:
    l2.append(i+10)
#
i=1
while i<=10:
    print(i)
    i+=1
isum=0
for i in range(101):
    isum+=i
print(isum)
isum=0
for i in range(101):
    if i%2==0:
        isum+=i
    print(isum)
for i in range(1,11):
    if i==5:
        continue
    print(i)
v1=1
if v1>10:
    pass
else:
    print('b')
#############
isum=0
for i in range(1,101):
    isum+=i
    if isum>=2000:
        print('k = ',i,'sum = ',isum)
        break


























