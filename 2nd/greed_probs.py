
# 1이 될 때까지
def prob1():
    # O(N)
    def prob1_mine():
        a, b = map(int, input().split())

        cnt = 0

        while a > 1:
            if a % b == 0:
                a //= b
            else: 
                a -= 1
            cnt += 1

        print(cnt)

    # O(logN)
    def prob1_dblike():
        n, k = map(int, input().split())
        result = 0

        while True:
            # N이 K로 나누어떨어지는 수가 될 때까지 빼기
            # 
            target = (n//k) * k
            result += (n - target)
            n = target
            # N이 K보다 작을 때 반복문 탈출
            if n < k:
                break
            # k로 나누기
            result += 1
            n //= k

        # 마지막으로 남은 수에 대해 1씩 빼기
        result += (n-1)
        print(result)

# 문제 2 - 곱하기 혹은 더하기
def prob2():
    def prob2_mine():
        n = input()

        res = 0

        for i in n:
            curr = int(i)
            if res == 0 or res == 1\
            or curr == 0 or curr == 1:
                res += curr
                continue
            res *= curr

        print(res)

    def prob2_dblike():
        data = input()
        res = int(data[0])

        for i in data[1:]:
            num = int(i)
            if num <= 1 or res <= 1:
                res += num
            else:
                res *= num
        print(res)

def prob3():
    def prob3_mine():
        _ = int(input())
        li = list(map(int, input().split()))

        res = list()
        temp = list()

        for i in sorted(li):
            temp.append(i)
            if len(temp) == max(temp):
                res.append(temp)
                temp = list()

        print(len(res))


    def prob3_db():
        n = int(input())
        data = list(map(int, input().split()))
        data.sort()

        result = 0 # 총 그룹의 수
        count = 0 # 현재 그룹에 포함된 모험가의 수

        for i in data: #공포도 낮은 것부터 하나씩 확인하며
            count += 1 # 현재 그룹에 해당 모험가 포함시키기
            if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
                result += 1 # 총 그룹 수 증가
                count = 0 # 현재 그룹 초기화

        print(result) # 총 그룹 수 출력
    