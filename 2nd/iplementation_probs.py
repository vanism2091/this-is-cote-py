import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')


import mytest as te

dispatcher = {}


# 1. 시각
def prob1():
    def prob1_mine(n):
        # n = int(input())
        def getNum(until, num_pow, num_add):
            res = 0
            for i in range(until+1):
                if "3" in str(i):
                    res += 60 ** num_pow
                else:
                    res += num_add
            return res
        sec = getNum(59, 0, 0)
        min = getNum(59, 1, sec)
        res = getNum(n, 2, min)
        return res

    def prob1_db(h):
        # H 입력 받기
        # h = int(input())

        count = 0
        for i in range(h+1):
            for j in range(60):
                for k in range(60):
                    # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                    if '3' in str(i)+str(j)+str(k):
                        count += 1
        return count

    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db

# 수행 시간 test 결과
# n=23일 때 10번 실행 평균 수행 시간
# [6.47544861e-05 8.07682514e-02]

# 왕실의 나이트
def prob2():
    def prob2_mine(n):
        # n = input()
        dy = [2, 2, 1, -1, -2, -2, 1, -1]
        dx = [1, -1, -2, -2, 1, -1, 2, 2]
        def pos_to_idx(x, y): return ord(x) - ord(y)
        y, x = pos_to_idx(n[0], "a"), pos_to_idx(n[1], "1")
        cnt = 0
        for i in range(8):
            nx, ny = dx[i]+x, dy[i]+y
            if nx < 0 or nx > 7 or ny < 0 or ny > 7:
                continue
            cnt += 1
        return cnt

    def prob2_db(input_data):
        # 현재 나이트의 위치 입력 받기
        # input_data = input()
        row = int(input_data[1])
        column = int(ord(input_data[0])) - int(ord('a')) + 1

        # 나이트가 이동할 수 있는 8가지 방향 정의
        steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

        # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
        result = 0
        for step in steps:
            # 이동하고자 하는 위치 확인
            next_row = row + step[0]
            next_column = column + step[1]
            # 해당 위치로 이동이 가능하다면 카운트 증가
            if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
                result += 1
        return result

    dispatcher["prob2_mine"] = prob2_mine
    dispatcher["prob2_db"] = prob2_db

# 배울점
# 방향 벡터를 튜플의 리스트로 정의하는 방법도 있구나. 직관적이고 괜찮은 듯


# 문자열 재정렬
def prob3():
    def prob3_mine(s):
        # s = input()
        # res = ""
        res = []
        has_digit = False
        num = 0
        asc9, asc0 = ord('9'), ord('0')
        for c in s:
            if ord(c) <= asc9:
                if not has_digit:
                    has_digit = True
                num += (ord(c)-asc0)
            else:
                # res += c
                res.append(c)
        res.sort()
        if has_digit:
            res.append(str(num))
        # res = "".join(sorted(res)) + (str(num) if has_digit else "")
        return "".join(res)
        # return res
# 0.03122 arr.sort()
# 0.03139 sorted(arr)
# arr.sort()와 sorted(arr) 의 시간적 차이는 없지만 이 문제에서 굳이 새 공간을 할당할 필요는 없을 것 같아서 arr.sort()가 좋은 듯
# 내 코드를 일부 수정해가며 실험했는데
# 그 결과, str + operator를 계속 취하는 것 보다 list append 후 join 하는 게 더 빠르다.

    def prob3_db(data):
        # data = input()
        result = []
        value = 0

        # 문자를 하나씩 확인하여
        for x in data:
            # 알파벳인 경우 결과 리스트에 삽입
            if x.isalpha():
                result.append(x)
            # 숫자는 따로 더하기
            else:
                value += int(x)

        # 알파벳을 오름차순으로 정렬
        result.sort()

        # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
        if value != 0:
            result.append(str(value))

        #최종 결과 출력 (리스트를 문자열로 변환하여 출력)
        return ''.join(result)

    dispatcher["prob3_mine"] = prob3_mine
    dispatcher["prob3_db"] = prob3_db

# 숫자가 없을 수도 있다는 예외 케이스를 생각하지 못했다.
# 숫자가 0이 하나만 있는 경우, 맨 뒤에 0이 출력되어야 하는데
# 동빈님 코드는 그렇지 않은 것 같다.
# 문자열과 리스트로 나뉘었는데, 속도가 뭐가 더 빠른지 궁금하다.
# 테스트하는 함수를 만들어봐야겠다. -> 만들었음
# [0.00417764 0.00296221]
# 리스트 승

dispatcher["prob1"] = prob1
dispatcher["prob2"] = prob2
dispatcher["prob3"] = prob3


def get_prob_input(prob_num):
    # return 값은 반드시 list나 tuple 형태로
    if prob_num == 1:
        return (23,)
    elif prob_num == 2:
        li1, li2 = [*range(ord("a"), ord("i")+1)], [*range(ord("1"), ord("8") + 1)]
        return ["".join(map(chr, te.get_choices(li1)+te.get_choices(li2)))]
    elif prob_num == 3:
        li = [*range(ord("0"), ord("9")+1), *range(ord("A"), ord("Z")+1)]
        # 숫자는 0만 선택하는 경우
        # li = [*range(ord("0"), ord("0")+1), *range(ord("A"), ord("Z")+1)]
        return ["".join(map(chr, te.get_choices(li, 10000)))]
    pass


test_res = list()
for i in range(1, 4):
    i, e = te.test_probs_ntimes(te.test_prob, 10, prob_num=i, dispatcher=dispatcher, get_input=get_prob_input)
    test_res.append((i, e))
    print("-------")
# info1, et1 = te.test_probs_ntimes(te.test_prob, 10, get_test_param(1))
# info2, et2 = te.test_probs_ntimes(te.test_prob, 10, get_test_param(2))
# info3 ,et3 = te.test_probs_ntimes(te.test_prob, 10, get_test_param(3))