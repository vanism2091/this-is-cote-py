from math import ceil
import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')


import mytest as te

dispatcher = {}

"""
    # d[1] 즉, 내 코드에서 d[2]일 때.. max(0, 1) 해야 함..!!!!
    ??
"""
# 개미 전사
# f(n) = max(f(n-1), f(n-2)+d[n])
def prob1():
    # bottom-up
    def prob1_mine(n):
        N = int(input())
        foods = list(map(int, input().split()))
        dp = [0, *foods[:2]] + [0] * (N-2)
        for i in range(3, N):
            dp[i] = max(dp[i-2]+foods[i], dp[i-1])
        return dp[N]
    
    def prob1_mine_2(n):
        N = int(input())
        foods = list(map(int, input().split()))
        dp = [0, *foods[:2]] + [0] * (N-2)
        def get_res(n):
            if dp[n] != 0:
                return dp[n]
            dp[n] = max(get_res(n-2)+foods[n], get_res(n-1))
        return dp[N]

        pass
    
    def prob1_db(h):
        # 정수 N을 입력 받기
        n = int(input())
        # 모든 식량 정보 입력 받기
        array = list(map(int, input().split()))
        
        # 압서 계산된 결과를 저장하기 위한 DP 테이블 초기화
        d = [0] * 100

        # 다이나믹 프로그래밍 (Dynamic Programming) 진행 (바텀업)
        d[0] = array[0]
        d[1] = max(array[0], array[1]) # 와.. 맞네;;;; 가 아니고... 3일때 그럼.. max를 해버리면, 2, 3 인 경우 있는거 아님? 응 아님;
        for i in range(2, n):
            d[i] = max(d[i-1], d[i-2] + array[i])

        # 계산된 결과 출력
        print(d[n-1])
        pass
    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db


def prob2():
    def prob2_mine(x):
        # x = int(input())
        d = [0, 0, 1, 1, 2, 1] + [0] * (x-5)
        for i in range(6, x+1):
            m_one = 999999 if i%5 else d[i//5] + 1
            m_two = 999999 if i%3 else d[i//3] + 1
            m_three = 99999 if i%2 else d[i//2] + 1
            m_four = d[i-1] + 1
            d[i] = min(m_one, m_two, m_three, m_four)
        print(d[x])
            
    def prob2_db(h):
        # 정수 x를 입력 받기
        x = int(input())
        # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화. x는 3만까지 들어올 수 있다
        d = [0] * 30001

        # 다이나믹 프로그래밍 (바텀업)
        for i in range(2, x+1):
            # 현재 수에서 1을 빼는 경우
            d[i] = d[i-1] + 1    
            # 현재의 수가 2로 나누어 떨어지는 경우
            if i % 2 == 0:
                d[i] = min(d[i], d[i//2]+1)
            # 현재의 수가 3으로 나누어 떨어지는 경우
            if i % 3 == 0:
                d[i] = min(d[i], d[i//3]+1)
            # 현재의 수가 4로 나누어 떨어지는 경우
            if i % 5 == 0:
                d[i] = min(d[i], d[i//5]+1)

        # 2, 3, 5가 최대공약수가 1이라서 가능함.. 이렇게 할 수도 있구나
        # 나는 굳이 모듈라 연산을 매번 해야함 계속 해야함.
        pass

    dispatcher["prob2_mine"] = prob2_mine
    dispatcher["prob2_db"] = prob2_db


"""
효율적인 화폐 구성

"""
def prob3():
    import sys
    def prob3_mine(n):
        N, M = map(int, input().split())
        coins = list(map(int, sys.stdin.readlines()))
        d = [-1] * (10001)
        min_coin = 10001
        for coin in coins:
            if coin < min_coin:
                min_coin = coin
            d[coin] = 1
        for i in range(min_coin * 2, M+1):
            possible_coins = [d[i-coin] for coin in coins if i > coin and d[i-coin] != -1]
            if not possible_coins:
                continue
            d[i] = min(possible_coins) + 1
        print(d[M])
        pass
    
    def prob3_db(h):
        # 정수 N, M 입력 받기
        n, m = map(int, input().split())
        # N개의 화폐 단위 정보를 입력 받기
        array = []
        for i in range(n):
            array.append(int(input()))

        # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
        d = [10001] * (m+1)
        # 다이나믹 프로그래밍 진행
        d[0] = 0
        for i in range(n):
            ### 이 부분 때문에 내 코드보다 평균적으로 더 효율적일 가능성이 있음
            for j in range(array[i], m+1):
                if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
                    d[j] = min(d[j], d[j-array[i]] + 1)

        # 계산된 결과 출력
        if d[m] == 10001:
            print(-1)
        else:
            print(d[m])
        pass

    dispatcher["prob3_mine"] = prob3_mine
    dispatcher["prob3_db"] = prob3_db


# 금광문제
def prob4():
    def prob4_mine(n):
        cases = int(input())
        for _ in cases:
            n, m = map(int,input().split())
            # 1 3 3 2 2 1 4 1 0 6 4 7
            # 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
            golds = list(map(int, input().split()))
            # index = m*i + j
            # [i-1, j-1] [0, j-1], [i+1, j-1]
            # index 제대로... :)
            for i in range(1, m):
                for j in range(n):
                    curr_idx = m*j + i
                    print(golds[m*j + i], i, j)
                    possible_cases = [golds[m*(j+c)+(i-1)] for c in [-1, 0, 1] if j+c>= 0 and j+c < n]
                    print("\t", possible_cases)
                    golds[m*j + i] += max(possible_cases)
            print(max([golds[m*(j+1)-1] for j in range(n)]))
        pass
    
    # test case 이런 식으로 처리할 수 있구나 굿
    def prob4_db(h):
        # 테스트 케이스(Test case) 입력
        for tc in range(int(input())):
            # 금광 정보 입력
            n, m = map(int, input().split())
            array = list(map(int, input().split()))
            # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
            dp = []
            index = 0
            for i in range(n):
                dp.append(array[index:index + m])
                index += m
            # for i in range(n):
            #     dp.append(array[m*i:m*(i+1)])
            
            # 다이나믹 프로그래밍 진행
            for j in range(1, m):
                for i in range(n):
                    # 왼쪽 위에서 오는 경우
                    if i == 0: left_up = 0
                    else: left_up = dp[i-1][j-1]

                    # 왼쪽 아래에서 오는 경우
                    if i == n-1: left_down = 0
                    else: left_down = dp[i+1][j-1]
                    
                    # 왼쪽에서 오는 경우
                    left = dp[i][j-1]
                    dp[i][j] += max(left_up, left, left_down)
           
            # 리스트 컴프리헨션으로 해도 괜찮지않을까? 
            # 음.. 근데 저렇게 하는게 더 시간 복잡도가 덜하긴 함.
            # 왜냐면, 나는 총 2N list comprehension O(N), max: O(N)
            # 강의는 N에 할 수 있음
            result = 0
            if i in range(n):
                result = max(result, dp[i][m-1])

            print(result)
        pass

    dispatcher["prob4_mine"] = prob4_mine
    dispatcher["prob4_db"] = prob4_db

# 7
# 15 11 4 8 5 2 4

# 2

def prob5():
    def prob5_mine(n):
        from bisect import bisect_right
        n = int(input())
        soldiers = list(map(int, input().split()))
        d = [0] * (n)
        for i in range(2, n):
            if soldiers[i] > soldiers[i-1]:
                # i-1번째 원소를 빼거나
                #  - solders[:i] 리스트 순회하며 i번째 원소보다 작은 값의 수를 구한다
                # 위의 값이 d[i-1]+1보다 작으면 i번째 원소를 뺀다.
                # bisect의 bisect_right를 이용하자. 그럼 들어가야하는 인덱스가 나옴.
                # i - b_r_idx
                print("if",i)
                # 오름차순이 아니라 내림차순이라 bisect_right로 간단하게 구하는건
                # 더 연구가 필요함...  우선은... O(n^2)으로 풀어보자
                # d[i] = min(d[i-1]+1, i - bisect_right(soldiers[i-1::-1], soldiers[i]))
                d[i] = min(d[i-1]+1, len([e for e in d[:i] if e < soldiers[i]]))
            else:
                print("else", i)
                d[i] = d[i-1]
            pass
        pass

    def prob5_after_idea():
        n = int(input())
        soldiers = list(map(int, input().split()))[::-1]
        d = [1] * n
        for i in range(1, n):
            for j in range(i):
                if soldiers[i] > soldiers[j]:
                    d[i] = max(d[i], d[j]+1)
        print(n - max(d))
        
    def prob5_db(h):
        n = int(input())
        array = list(map(int, input().split()))
        # 순서를 뒤집어 '최장 증가 부분 수열' 문제로 치환
        array.reverse()

        # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
        dp = [1] * n
        # 가장 긴 증가하는 부분 수열 알고리즘 수행
        for i in range(1, n):
            for j in range(i):
                if array[j] < array[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # 열외해야 하는 병사의 최소 수를 출력
        print(n - max(dp))
        pass

    dispatcher["prob5_mine"] = prob5_mine
    dispatcher["prob5_db"] = prob5_db



dispatcher["prob1"] = prob1
dispatcher["prob2"] = prob2
dispatcher["prob3"] = prob3
dispatcher["prob4"] = prob4
dispatcher["prob5"] = prob5

prob2()
dispatcher["prob2_mine"](26)