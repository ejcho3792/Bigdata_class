# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:28:07 2021

@author: eunji
"""
###############################
# 문자열 처리                  #
###############################
v1='abcde'
v1.upper()
'ABCDE'.lower()
'abc def'.title()
#
'abcd'[0]
'abcd'[-1]
'abcd'[0:3]
#
vtel='031)345-0834'
vtel[0:3]
#
v1.startswith('a')
v1.startswith('b',1)
v1[1:].startswith('b')
v1.startswith('ab',0,2)
v1.endswith('e')
v1.endswith('E')
#
'abc'=='abc'
' abc '.strip()
' a b c '.strip()
'abc'.strip('a')
'abaca'.strip('a')
' abcd'.lstrip()
' abcd '.rstrip()
#
'abcabc'.replace('a','A')
'abcabc'.replace('ab','AB')
'abcabc'.replace('ab','')
#
'a/b/c/d'.split('/')
'a/b/c/d'.split('/')[1]
#
'abcd'.find('b')
a=vtel.find(')')
vtel[0:a]
vtel[0:vtel.find(')')]
#
'abcabcabc'.count('a')
#
type(v1)
v1.isalpha()
v1.isnumeric()
v1.isupper()
v1.islower()
#
'a'+'b'
len(v1)
3/len(v1)
###############################
# 예제                        #
###############################
#
vname='ejcho'
vemail='kk13591@naver.com'
jumin='960404-1234567'
#
vname[1]=='m'
#
vemail[0:vemail.find('@')]
jumin[7]=='2'

# 3. 주민번호에서 여자인지 확인 (참고: 1: 남자 2: 여자)

jumin
jumin.split('-')[1][0] == 2
jumin.split('-')[1][0]
# '901026-111111'
list(jumin.split('-'))
# ['901026', '111111']
jumin[7] == '2'