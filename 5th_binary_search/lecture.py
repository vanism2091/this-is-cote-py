

array = [ 1, 2, 3, 4, 5 ]
# 1. 재귀적
def binary_search():
    # mid 를 start+end //2 로 해야..!!!
    # target이 없는 경우를 누락함
    def mine_recursive(array, target, start, end):
        mid = end // 2
        if target == array[mid]:
            return mid
        elif target> array[mid]: 
            return mine_recursive(array, target, mid+1, end)
        else: 
            return mine_recursive(array,target, start, mid-1)
        
    def lecture_recursive(array, target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간 점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            return lecture_recursive(array, target, start, mid-1)
        # 중간 점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            return lecture_recursive(array, target, mid+1, end)


    # 이건 동일하다 :)
    def mine_iterative(array, target, start, end):
        while start <= end:
            mid = (start+end) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                end = mid -1
            else: 
                start = mid + 1
        return None
    
    def lectture_iterative(array, target, start, end):
        while start <= end:
            mid = (start+end) // 2
            # 찾은 경우 중간점 인덱스 반환
            if array[mid] == target:
                return mid
            # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            elif array[mid] > target:
                end = mid - 1
            # 중간점 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else: 
                start = mid + 1
        return None
        
    pass

"""
파이썬 이진 탐색 라이브러리

이진 탐색 문제를 위해 알아두면 좋은 라이브러리

- bisect_left(a, x)
	- 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x)
	- 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

time complexity of bisect O(logN)
"""
def bisect_introduction():
    from bisect import bisect_left, bisect_right
    a = [1, 2, 4, 4, 8]
    x = 4

    print(bisect_left(a, x)) # 2
    print(bisect_right(a, x)) # 4

"""
값이 특정 범위에 속하는 데이터 개수 구하기
"""

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    def mine():
        return bisect_right(array, right_value) - bisect_left(array, left_value)

    def lecture():
        right_index = bisect_right(array, right_value)
        left_index = bisect_left(array, left_value)
        return right_index - left_index

"""
- 파라메트릭 서치
	- 최적화 문제를 결정문제(예/아니오)로 바꾸어 해결하는 기법
		- 특정한 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화문제
        - 최적화문제: 어떤 함수의 값을 max, min으로 만드는..
        - 이를 여러 번의 결정 문제로 바꾸어서 해결
        - 탐색 범위를 좁혀가며 빠르게 해결
	- 일반적으로 코테에서 이 문제는 이진 탐색을 이용하여 해결할 수 있음
"""