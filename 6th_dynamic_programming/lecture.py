


"""
피보나치 수열
- 재귀적 구현
    - 재귀 함수는 종료 조건을 잘 명시해야 한다.
피보나치 수열의 시간 복잡도 분석

"""

# 단순 재귀 소스코드
def fibo_recursive():
    def mine(n):
        if n in (1, 2):
            return 1
        return mine(n-1)+ mine(n-2)
    # 피보나치 함수를 재귀 함수로 구현
    def lecture(x):
        if x == 1 or x == 2:
            return 1
        return lecture(x-1) + lecture(x-2)

# 다이나믹 프로그래밍, 탑다운. 재귀 이용. 디피
def fibo_dp():
    # 설명만 듣고 내가 구현해보는 코드
    dp_mine = [0, 1, 1]
    def mine(n):
        if len(dp_mine) >= n:
            return dp_mine[n]
        else:
            dp_mine.append(mine(n-1) + mine(n-2))
            return dp_mine[n]
    
    # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
    d = [0] * 100
    # 피보나치 함수를 재귀적으로 구현 (탑다운 다이나믹 프로그래밍)
    def lecture(x):
        # 종료 조건 (1 혹은 2 일때 1을 반환)
        if x == 1 or x == 2:
            return 1
        # 이미 계산한 적 있는 문제라면 그대로 반환
        if d[x] != 0:
            return d[x]
        # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
        d[x] = lecture(x-1) + lecture(x-2)
        return d[x]
    
    # 미리 길이가 N인 수열을 해놓는구낭.. 
    # 만약 나처럼 저렇게 해뒀ㅅ다면... 풀리나? 궁금쓰

    # 99일때
    def mine_bottom_up(n):
        d = [0, 1, 1] + [0] * n-2
        for i in range(3, n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]
    def lecture_bu(n):
        # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
        d = [0] * 100
        # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
        d[1] = 1
        d[2] = 1
        n = 99
        
        # 피보나치 함수 반복문으로 구현 (바텀 업 다이나믹 프로그래밍)
        # 작은 문제를 먼저 해결 후 큰 문제를 해결한다.
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2]
        print(d[n])
            
    
