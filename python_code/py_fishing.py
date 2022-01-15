import time
import random
import numpy as np
import pandas as pd

# 데이터 확인
df = pd.read_excel("./data/텍스트게임.xlsx")
df.info()
df.describe()

# 낚시터 구현하기
id = 'mmm'
pw = '000'
def game_fishing_center():
    print("시작")
    fishing = pd.read_excel("./data/물고기표.xlsx")
    choose_fish = np.array(fishing).reshape(-1, 4)
    choose_fish_num = random.randint(0, len(fishing))
    choose_fish_wait_num = random.randint(choose_fish[choose_fish_num][0], choose_fish[choose_fish_num][1])
    time.sleep(choose_fish_wait_num)
    print("!!")
    print("{} 님, 물고기는 {} 입니다.".format("mmm", choose_fish[choose_fish_num][2]))

    df.loc[len(df)] = [id, pw, choose_fish[choose_fish_num][2], 1, choose_fish[choose_fish_num][-1], "미판매"]
    df.to_execel("./data/text_game.xlsx", sheet_name="낚았다 게임", index=None)

print(game_fishing_center())
################################################
id = 'mmm'
pw = '000'

def game_store(df, id, pw):
    print("현재 판매하지 않은 물고기는 {}개 입니다.".format(len(df[(df['ID'] == id) & (df['현황'] == '미판')])))
    미판_index = df[(df['ID'] == id) & (df['현황'] == '미판')].index

    if len(미판_index) != 0:  # 판매 안 된게 있으면,
        for i in range(len(미판_index)):
            print("{} 물고기를 판매했어요.".format(df[(df['ID'] == id) & (df['현황'] == '미판')]['물고기'][미판_index[i]]))

            # DB 저장 / 엑셀 저장
            df.loc[미판_index[i]] = [id, pw,
                                   df[(df['ID'] == id) & (df['현황'] == '미판')['물고기'][미판_index[i]]],
                                   df[(df['ID'] == id) & (df['현황'] == '미판')['수량'][미판_index[i]]],
                                   df[(df['ID'] == id) & (df['현황'] == '미판')['가격'][미판_index[i]]],
                                   "판매"]
    else:  # 빈 경우
        print("다 팔았네요, GOOD JOB")

    df.to_excel("./data/텍스트게임.xlsx", sheet_name="낚시게임", index=None)


game_store(df, id, pw)
현재
판매하지
않은
물고기는
0
개
입니다.
다
팔았네요, GOOD
JOB


# 낚시터 구현하기

def game_fishing_center():
    print("자자자~~~ 신중하게 낚시를 시작합니다. 월척하세요~")

    fishing = pd.read_excel("./data/물고기표.xlsx")

    choose_fish = np.array(fishing).reshape(-1, 4)

    choose_fish_num = random.randint(0, len(fishing))  # 0부터 전체 행까지 반복
    choose_fish_waiting_num = random.randint(choose_fish[choose_fish_num][0], choose_fish[choose_fish_num][1])

    time.sleep(choose_fish_waiting_num)  # 대기시간 추가

    print("야~ 낚았네요! 월척이길 바래요")
    print("[축하(이모티콘 추가)]{} 님이 낚은 물고기는 {} 입니다.".format("닥터윌", choose_fish[choose_fish_num][2]))


print(game_fishing_center())
자자자
~~~ 신중하게
낚시를
시작합니다.월척하세요
~
야
~ 낚았네요! 월척이길
바래요
[축하(이모티콘 추가)]닥터윌
님이
낚은
물고기는
거룻배가자미
입니다.
None


# 낚시터 구현하기

def game_fishing_center(df, id, pw):
    print("자자자~~~ 신중하게 낚시를 시작합니다. 월척하세요~")

    fishing = pd.read_excel("./data/물고기표.xlsx")

    choose_fish = np.array(fishing).reshape(-1, 4)

    choose_fish_num = random.randint(0, len(fishing))  # 0부터 전체 행까지 반복
    choose_fish_waiting_num = random.randint(choose_fish[choose_fish_num][0], choose_fish[choose_fish_num][1])

    time.sleep(choose_fish_waiting_num)  # 대기시간 추가

    print("야~ 낚았네요! 월척이길 바래요")
    print("[축]{} 님이 낚은 물고기는 {} 입니다.".format("닥터윌", choose_fish[choose_fish_num][2]))

    df.loc[len(df)] = [id, pw, choose_fish[choose_fish_num][2], 1, choose_fish[choose_fish_num][-1], "미판"]
    df.to_excel("./data/text_game.xlsx", sheet_name="낚시게임", index=None)


game_fishing_center(df, 'kim', '1234')
# 계정정보

계정정보 = []

df = pd.read_excel("./data/텍스트게임.xlsx")

계정 = int(input("로그인(1)/회원가입(2)"))

if 계정 == 1:  # 로그인
    계정정보.append(input("ID 입력:"))
    계정정보.append(int(input("패스워드 입력:")))

    if 계정정보[0] in df['ID'].unique() and 계정정보[1] in df['PW'].unique():  # unique() :중복제거
        print("게임을 시작합니다.")
        game_play(계정정보[0], 계정정보[1])
    else:
        print("ID 또는 패스워드가 없어요")
        pass

elif 계정 == 2:  # 회원 가입
    계정정보.append(input("ID 입력"))
    계정정보.append(int(input("패스워드 입력:")))

    print("[축하합니다] 회원가입 완료")
    print("게임의 세계로 오실까요?")
    game_play(계정정보[0], 계정정보[1])