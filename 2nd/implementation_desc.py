import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')

import random
import numpy as np
import mytest as te

dispatcher = {}

def description():
    def using_orientation_vector():
        # 동, 북, 서, 남
        dx = [0, -1, 0, 1] # 행
        dy = [1, 0, -1, 0] # 열

        # 현재 위치
        x, y = 2, 2

        for i in range(4):
            # 다음 위치
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
        
    def udlr():
        def mine(N, plan_list):
            # N = int(input())
            # plan_list = input().split()

            x, y = 1, 1

            moves_dict = {
                "L": (0, -1),
                "R": (0, 1),
                "U": (-1, 0),
                "D": (1, 0),
            }

            for plan in plan_list:
                dx, dy = moves_dict[plan]
                ax, ay = x+dx, y+dy
                if ax < 1 or ax > N or ay < 1 or ay > N:
                    continue
                x, y = ax, ay

            print(ax, ay)

        def db(n, plans):
            # N 입력 받기
            # n = int(input())
            x, y = 1, 1
            # plans = input().split()

            # L, R, U, D에 따른 이동 방향
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            move_types = ['L', 'R', 'U', 'D']

            # 이동 계획을 하나씩 확인하기
            for plan in plans:
                # 이동 후 좌표 구하기
                for i in range(len(move_types)):
                    if plan == move_types[i]:
                        # python은 nx, ny를 사전에 초기화 하지 않아도
                        # for 문 밖에서 참조 가능하다
                        nx = x + dx[i]
                        ny = y + dy[i]
                # 공간을 벗어나는 경우 무시
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                x, y = nx, ny
            
            print(x, y)
        dispatcher["udlr_mine"] = mine
        dispatcher["udlr_db"] = db
    udlr()

def getTestPlans(n):
    move_types = ['L', 'R', 'U', 'D']
    return "".join(random.choices(move_types, k=n))

def test_udlr(n):
    plans = getTestPlans(n)
    print(plans)
    description()
    exec_time = []
    exec_time.append(te.exec_time_check(dispatcher["udlr_mine"], n, plans))
    exec_time.append(te.exec_time_check(dispatcher["udlr_db"], n, plans))
    return exec_time



te.test_ntimes(test_method=test_udlr, ntimes=10, params=[100])
# n=100 일 때, 10번 테스트의 평균 
#   [3.26395035e-05 8.77857208e-05]
# n=1e3 일 때, 10번
#   [0.00027978 0.00096345]
# n=1e4일 때, 10번 평균 
#   [0.00336039 0.01014864]

# 수행 시간 체크를 위한 공용 함수를 만들어볼까...
# *args 활용해서...