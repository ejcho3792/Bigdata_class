###############################
#       1. 변수와 리스트       #
###############################
# 변수 : 값을 저장하기 위한 객체
# 변수의 명명 규칙 : 대소 구분, 숫자 시작 불가(숫자 포함 가능),
#                   특수기호 삽입 불가(_ 가능)
#                   예약어(함수명, 함수내 인자명, 패키지 이름, ..., if, for, while)
vsum1 = 1 
vsum1
v1 = 'abcd'
v2 = '''   
dfjldjf
jflsdfj
'''# 여러라인의 문자열 전달 시 ''' 사용 '''

###############################
# 모듈(module)                #
###############################
# 패키지(함수의 묶음)
# import라는 함수로 모듈 호출(로딩)
round(1.5)
trunc(1.5)   # 불가
# 1) 모듈 호출 : 하위 함수는 모듈명.함수명
import math
import math as ma
math.trunc(1.5)
# 2) 모듈 내 함수 직접 호출 : 함수명만 사용 가능
from math import trunc
trunc(2.9)
###############################
# 산술연산                     #
###############################
3 + 2
3 / 1.5
10 - 2
5 * 3
9//2     # 몫
9%2      # 나머지
3**2     # 거듭제곱
math.pow(3, 2)   # 3의 제곱

###############################
# 파이썬 자료 구조             #
###############################
# 1. 리스트 
# - 가장 기본 자료 구조(여러 상수를 동시 전달)
# - 1차원
# - 서로 다른 데이터 타입 가능

# 1) 리스트 생성
l1 = [1,2,3,4]
l2 = [1,2,3,'4']

t1 = (1,2,3,4)
t2 = 1,2,3,4

# 2) 색인(indexing)
l1[0]     # 정수 색인
l1[0:1]   # n:m => n부터 m-1까지
l1[0:2]   # n:m => n부터 m-1까지(슬라이스 색인)
l2[0,2]      # 여러 숫자 전달 불가
l2[[0,2]]    # 여러 숫자 전달 불가
l1[-1]       # reverse indexing

# 3) 수정
l1[0] = 10

# 4) 연산
l1 + 1    # 리스트와 정수 연산 불가
l1 > 1    # 조건 전달 불가
[1,2,3] + [10,20,30]   # 리스트 + 리스트 = 리스트 확장
l1 = l1 + [5]          # 원소의 추가
l1.append(6)           # 리턴은 되지 않고 즉시 객체 수정(원소의 추가)
# [ 참고 ]
'a' + 'b'              # 문자열끼리의 더하기는 문자열의 결합
'a' * 3                # 문자열의 곱하기는 문자열의 반복
# [ 참고 : 튜플의 수정 ]
t1[0] = 10             # 튜플은 수정 불가

# 5) 삭제
del(l1[0])             # 첫 번째 원소 삭제
del(l1)                # 객체 자체 삭제
l2 = []                # 리스트 내 모든 원소 삭제

###############################
# 함수와 메서드                #
###############################
# 메서드도 함수의 일부
# 인수의 전달 방식이 다름

sum([1,2,3])              # 함수 : 인수의 전달이 모두 괄호 안에서 진행

import numpy as np
a1 = np.array([1,2,3])
a1.sum()                  # 메서드 : 객체에서 호출 가능한 형태의 함수(값을 객체가 가지고 있음)


# 단축키
# f9 : 라인 단위 실행
# ctrl + 1 : 선택 영역 주석 처리 및 해제

# 변수, 리스트(생성, 색인, 수정,)
# 함수와 메서드의 차이
# 연산자