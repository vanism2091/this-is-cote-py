import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')


import mytest as te

dispatcher = {}

# 두 배열의 원소 교체
def prob1():
    def prob1_mine_before():
        import sys
        p = sys.stdin.readline()
        n, k = map(int, input().split())
        A = list(map(int, p().split()))
        B = list(map(int, p().split()))
        A.sort()
        B.sort()
        return sum(A[k:] + B[n-k:])

    # 안일했음을 깨닫고, 다시 짜보는 코드
    def prob1_mine():
        n, k = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.sort()
        B.sort()
        l = 0
        for _ in range(k):
            r = n-l-1
            if A[l] >= B[r]:
                break
            else:
                A[l], B[r] = B[r], A[l]
                l += 1
    
    def prob1_db(h):
        n, k = map(int, input().split()) # N과 K를 입력 받기
        a = list(map(int, input().split())) # 배열 A의 모든 원소 입력 받기
        b = list(map(int, input().split())) # 배열 B의 모든 원소 입력 받기

        a.sort() # A는 오름 차순 정렬 수행
        b.sort(reverse=True) # B는 내림 차순 정렬 수행

        # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
        for i in range(k):
            # A의 원소가 B의 원소보다 작은 경우
            if a[i] < b[i]:
                # 두 원소를 교체
                a[i], b[i] = b[i], a[i]
            else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
                break

        print(sum(a)) # 배열 A의 모든 원소의 합을 출력
    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db


dispatcher["prob1"] = prob1


def get_prob_input(prob_num):
    # return 값은 반드시 list나 tuple 형태로
    if prob_num == 1:
        return [1]

num_probs = 5
num_test = 10
test_res = list()
for i in range(1, num_probs+1):
    i, e = te.test_probs_ntimes(te.test_prob, num_test, prob_num=i, dispatcher=dispatcher, get_input=get_prob_input, show_input_info=False)
    test_res.append({"info":i, "exec_time":e})
    print("-------")


# import json
# 0번째 문제 1, 2번째 테스트 케이스 확인
# cases = [1, 2]
# for case_info in test_res[0]['info'][cases]:
#     print(json.dumps(case_info, sort_keys=True, indent=4))
