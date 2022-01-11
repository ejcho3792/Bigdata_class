import pandas as pd
card = pd.read_csv('./data/card.csv', encoding='cp949')
card = card.set_index('NUM')

# 문제) 일자별 총 지출 금액을 구해서(행끼리 더해라 axis=1로)
# , 마지막 컬럼에 추가
# 천 단위 구분기호 제거 후 숫자 컬럼 변경하시오
card.applymap(lambda x:float(x.replace(',', ''))).sum(axis=0)# axis = 0 서로다른 행끼리
card = card.applymap(lambda x:int(x.replace(',', '')))  # axis = 1 서로다른 열끼리
# 총 지출 금액
card['total'] = card.sum(axis=1)
card

# 식료품 컬럼에만 적용
card_new = pd.read_csv('./data/card.csv', encoding='cp949')
card_new = card_new.set_index('NUM')

# dataframe의 한 컬럼: map 함수를 사용
f2 = lambda x: int(x.replace(',', ''))
card_new['식료품'] = card_new['식료품'].map(f2)

# 형변환, 타입 변환
card_new['의복'] = card_new['의복'].str.replace(',', '')
card_new['의복'] = card_new['의복'].str.replace(',', '').astype('int')
card_new['책값'].replace(',', '')

# ','와 완전히 일지하는 값을 변경 또는 삭제
card = pd.read_csv('./data/card.csv', encoding='cp949')
card = card.set_index('NUM')
card = card.applymap(lambda x: int(x.replace(',', '')))

## 2) 일자별로 각 품목별 지출 비율을 출력
card.iloc[0,]
card.iloc[0,].sum()
card.iloc[0,]
card.iloc[0,].sum()

# apply 사용
f3 = lambda x: (x, x.sum())*100
card.apply(f3, axis=1)

# 문제) 각 구매 마다 POINT 컬럼 생성
# POINT는 주문금액 50000 미만 1%, 5만원 이상 10만원 미만 2% 10만 이상 3%
df1 = pd.read_csv('./data/card.csv', encoding = 'cp949')
result = []