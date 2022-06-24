from math import ceil
import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')


import mytest as te

dispatcher = {}

"""
problem 1

문제 내용
	입력 조건
		첫째 줄: 떡 갯수 N: [1, 1e6] 요청 길이 M: [1, 2e9]
		둘째줄: 떡의 개별 높이
			떡 높이의 총합은 항상 M이상이다
			[0, 1e9]
		B의 원소들, (1, 10,000,000) 인 자연수
	출력 조건
		적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
	제한 조건
		2초
		메모리 128MB
	내용
		떡의 길이는 일정하지 않음. 한 봉지 안의 총 떡 길이는 절단기로 잘라서 맞춤
		절단기에 높이 H를 지정하면 떡을 한 번에 절단
        높이가 H보다 긴 떡은 H의 윗 부분이 잘릴 것
        19, 14, 10, 17이고 H가 15이면 15, 14, 10, 15가 됨
		잘린 떡의 길이는 4, 0, 0, 2이고 손님은 6만큼의 길이를 가져감
		손님이 요청한 총 길이가 M일 때,
		적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 숫 있는 높이의 최댓값은?
"""

# 1. 떡을 정렬한다.
# 2. 원하는 떡 레인지를 구한다
# 이건 bs로 하자
#  
# [1, 3, 10, 14] idx
# 높이가 0일때 먼저 쳐내볼까..
# [0, 2, 9, 13] 0 -> 24
# [0, 0, 7, 11] 1 (3)  -> 18
# [ 0, 0, 0, 4] 2 (10) -> 4
# [ 0, 0, 0, 0] 3 -> 0
# 10? 
# 18에서 4까지는 height: 3->10step 까지, step당 len(li)-1-idx 만큼 증가한다
# s_s:18, b_s:4, array[s]:3, array[b]:10
# s + ceil((s_s - target) / len(array)-b_i)

from bisect import bisect_left

def prob1():
    # 일단 예제는 맞았는데.. 흑흑....
    def prob1_mine(n):
        N, M = map(int, input().split())
        array = list(map(int, input().split()))
        array.sort()

        res = {}
        start, end = 0, N-1
        while start <= end:
            mid = (start+end) // 2
            if mid in res:
                break
            curr_sum = sum([i - array[mid] for i in array[mid+1:]])
            res[mid] = curr_sum # idx와 sum을 res에 저장
            if curr_sum > M:
                start = (mid+end) // 2
            elif curr_sum < M:
                start = (start+mid) // 2
            else:
                return array[mid]
        idxs = sorted(res.keys())
        heights = sorted(res.values(), reverse=True)
        s_i = idxs[bisect_left(heights, M)] - 1
        return array[s_i] + ceil((heights[s_i]-M)/(N-s_i-1))

    # ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 진짜 할말이 없닼ㅋㅋㅋㅋㅋㅋㅋㅋ
    # 풀이만 보고 구현을 보지 않은 상태에서 풀이대로 다시 한 번 구현해보자.

    # while 조건에서 = 를 빼면 절대 안됨
    # sum 구할 때 list comprehension + sum 보다
    # total을 구하는게 공간 복잡도 측면에서 더 좋을 듯

    def prob1_mine_2():
        N, M = map(int, input().split())
        array = list(map(int, input().split()))
        start, end = 0, max(array)
        answer = 0
        while start < end: # = 빼먹으면 절대 안됨...
            mid = (start+end) // 2
            sum = sum([i - mid for i in array if i-mid>0])
            if M > sum:
                end = mid - 1
            else:
                answer = mid
                start = mid + 1
        return answer

    def prob1_db(h):
        # 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
        n, m = list(map(int, input().split(' ')))
        # 각 떡의 개별 높이 정보를 입력
        array = list(map(int, input().split()))

        # 이진 탐색을 위한 시작점과 끝점 설정
        start = 0
        end = max(array)
        # 이진 탐색 수행(반복적)
        result = 0
        while (start<= end):
            total = 0
            mid = (start + end) // 2
            for x in array:
                # 잘랐을 때 떡의 양 계산
                if x > mid:
                    total += x - mid
            # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
            if total < m:
                end = mid - 1
            # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
            else:
                #최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
                result = mid
                start = mid + 1
        # 정답 출력
        print(result)
        pass

    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db


def prob2():
    def prob2_mine(n):
        N, target = map(int, input().split())
        array = list(map(int, input().split()))
        def bisect_right(array, target, start, end):
            res = -1
            while start <= end:
                mid = (start+end)//2
                if array[mid] > target:
                    end = mid - 1
                else: 
                    if array[mid] == target: res = mid
                    start = mid + 1
            return res

        def bisect_left(array, target, start, end):
            res = -1
            while start <= end:
                mid = (start+end)//2
                if array[mid] >= target:
                    if array[mid] == target: res = mid
                    end = mid - 1
                else: 
                    start = mid + 1
            return res
        left_idx = bisect_left(array, target, 0, N-1)
        return -1 if left_idx == -1 else bisect_right(array, target,0, N-1) - left_idx + 1
    
    def prob2_db(h):
        pass

    dispatcher["prob2_mine"] = prob2_mine
    dispatcher["prob2_db"] = prob2_db

