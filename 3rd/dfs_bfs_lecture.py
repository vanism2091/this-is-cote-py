# Recursive Function
# - 종료 조건
# - 예시
#   - Factorial
#   - gcd


def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 10:
        return
    print(f'{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(f'{i}번째 재귀 함수를 종료합니다')

recursive_function(1)

def rf_print_output():
    # 1번째 재귀함수에서 2번째 재귀함수를 호출합니다.
    # 2번째 재귀함수에서 3번째 재귀함수를 호출합니다.
    # 3번째 재귀함수에서 4번째 재귀함수를 호출합니다.
    # 4번째 재귀함수에서 5번째 재귀함수를 호출합니다.
    # 5번째 재귀함수에서 6번째 재귀함수를 호출합니다.
    # 6번째 재귀함수에서 7번째 재귀함수를 호출합니다.
    # 7번째 재귀함수에서 8번째 재귀함수를 호출합니다.
    # 8번째 재귀함수에서 9번째 재귀함수를 호출합니다.
    # 9번째 재귀함수에서 10번째 재귀함수를 호출합니다.
    # 9번째 재귀 함수를 종료합니다
    # 8번째 재귀 함수를 종료합니다
    # 7번째 재귀 함수를 종료합니다
    # 6번째 재귀 함수를 종료합니다
    # 5번째 재귀 함수를 종료합니다
    # 4번째 재귀 함수를 종료합니다
    # 3번째 재귀 함수를 종료합니다
    # 2번째 재귀 함수를 종료합니다
    # 1번째 재귀 함수를 종료합니다
    pass

# 재귀함수를 이용하게 되면 스택에 데이터를 넣었다가 꺼내는 것과 마찬가지로
# 각각의 함수에 대한 정보가 실제로 스택 프레임에 재귀 함수기 담기게 되어서 
# 차례대로 호출되었다가 가장 마지막에 호출된 함수부터 차례대로 종료된다.
# https://leehyungi0622.github.io/2021/04/22/202104/210422-Algorithm_stack_frame_and_recursive_function/


# Factorial 구현 예제
# 반복으로 구현
def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= 1
    return result

# 재귀로 구현
def factorial_recursive(n):
    # n이 1이하인 경우 1 반환
    if n <= 1:
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)


# 두 개의 자연수에 대한 최대 공약수 계산
# 유클리드 호제법
# - 두 자연수 A, B에 대해 (A > B) A를 B로 나눈 나머지를 R이라고 하자
# - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다

# 문제를 보고 내가 구현
def gcd(a, b):
    if b == 0: return a
    r = a % b
    return gcd(b, r)

print(gcd(192, 162))

# 강의에서 구현
def gcd_lect(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
# 훨씬 더 깔끔하다. 재귀 횟수와 변수를 최적화하는 방법을 항상 고민해보자.

"""
DFS

- 구현 비교 및 내가 얻을 점
    - print(s, end=' ') 잊지 말자 굳이 res[]를 정의할 필요가 없다
    - return도 필요하지는 않음. 어차피 무한 재귀가 아니기 때문
    - 노드가 1부터 시작한다면 index 0 은 그냥 안쓰는게 더 직관적일 수 있다
"""


graph = [
    # 각 노드가 연결된 정보를 표현 (2차원 리스트)
    # idx i 노드와 연결된 노드 리스트
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited= [False]*9

# 설명만 보고 내가 해본 구현
res = []
def dfs(graph, v, visited):
    visited[v] = True
    res.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return

# 강의 구현
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

"""
BFS

- 구현 비교 및 내가 얻을 점
    - print(s, end=' ')를 두 번 쓸 필요가 없음
    - queue를 init할 때 node를 넣어두면 코드 한 줄 줄일 수 있음 
    - while 이후 조건문 python답게 하자
"""

from collections import deque
def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True
    print(v, end=" ")
    while len(q) != 0:
        for i in graph[q.popleft()]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                print(i, end=" ")

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

