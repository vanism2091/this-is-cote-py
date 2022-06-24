import sys
import os 
 
sys.path.insert(0, os.getcwd()+'/myutils')

import mytest as te

dispatcher = {}

from collections import deque
# 음료수 얼려먹기
# 상 하 좌 우 다 해야함..! 하, 우 만으로는 커버 못하는 경우도 있음 ( e.g. 역 ㄴ )
# TODO: 나중에 까먹을 것 같을 때 다시 짜보자.
def prob1():
    def prob1_mine(str):
        a, *tray = str.splitlines()
        n, m = map(int, a.split())
        def bfs(graph, start, visited):
            q = deque([start])
            while q:
                i, j = q.popleft()
                if i+1 < n and graph[i+1][j] == '0':
                    q.append((i+1, j))
                    visited[i+1][j] = True
                if j+1 < m and graph[i][j+1] == '0':
                    q.append((i,j+1))
                    visited[i][j+1] = True

        # n, m = map(int, input().split())
        # tray = [input() for _ in range(n)]
        visited = [[False]*m for _ in range(n) ]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if tray[i][j] == '0' and not visited[i][j]:
                    visited[i][j] = True
                    cnt += 1
                    bfs(tray, (i,j), visited)
        return cnt
    
    def prob1_db(str):
        a, *graph = str.splitlines()
        n, m = map(int, a.split())
        graph = [list(map(int, i)) for i in graph]
        def dfs(x, y):
            if x<= -1 or x>= n or y <= -1 or y>= m:
                return False
            # 현재 노드를 아직 방문하지 않았다면
            if graph[x][y] == 0:
                # 해당 노드 방문 처리
                graph[x][y] = 1
                # 4 방향에서 재귀적 호출
                dfs(x - 1, y) # 상
                dfs(x, y - 1) # 좌
                dfs(x + 1, y) # 하
                dfs(x, y + 1) # 우
                return True
            return False
        
        # n, m = map(int, input().split())
        # graph = []
        # for _ in range(n):
        #     graph.append(list(map(int, input())))
        
        # 모든 노드(위치)에 대하여 음료수 채우기
        result = 0
        for i in range(n):
            for j in range(m):
                # 현재 위치에서 dfs 수행
                if dfs(i, j) == True:
                    result += 1
        return result

    dispatcher["prob1_mine"] = prob1_mine
    dispatcher["prob1_db"] = prob1_db


# 미로 탈출
# 이건 리얼 BFS다 :)
def prob2():
    def prob2_mine():
        n, m = map(int, input().split())
        graph = [[0]*(m+1)]+[[0]+list(map(int,input())) for _ in range(n)]
        
        q = deque([(1, 1, 1)])
        while q:
            i, j, s = q.popleft()
            if i == n and j == m:
                return s
            graph[i][j] = 0
            cases = [(i - 1, j), (i + 1, j), (i, j-1), (i, j+1)]
            for x, y in cases:
                if x <= 0 or x > n or y <= 0 or y > m:
                    continue
                if graph[x][y] == 1:
                    q.append((x, y, s+1))
    print(prob2_mine())
    
    def prob2_db(h):
        # BFS 소스코드 구현
        def bfs(x, y):
            # 큐(Queue) 구현을 위해 deque라이브러리 사용
            queue = deque()
            queue.append((x, y))
            # 큐가 빌 때까지 반복
            while queue:
                x, y = queue.popleft()
                # 현재 위치에서 4가지 방향으로 위치 확인
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 미로 찾기 공간을 벗어난 경우 무시
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    # 벽인 경우 무시
                    if graph[nx][ny] == 0:
                        continue
                    # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
            return graph[n-1][m-1]
        
        n, m = map(int, input().split())
        graph = [list(map(int, input())) for _ in range(n)]
        # 이동할 네 가지 방향 벡터 정의 (상, 하, 좌, 우)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        #BFS 수행
        return bfs(0,0)

    dispatcher["prob2_mine"] = prob2_mine
    dispatcher["prob2_db"] = prob2_db

    # 방향 벡터를 사용하자
    #   나는 그때그때 case를 하는데 이게 메모리상, 그리고 연산 상 덜 유리할듯
    # 거리 값을 그래프 상에서 증가함으로써 뎈에 s를 굳이 넣지 않아도 됨 -> 메모리상 이득
    
dispatcher["prob1"] = prob1
dispatcher["prob2"] = prob2


def get_prob_input(prob_num):
    # return 값은 반드시 list나 tuple 형태로
    if prob_num == 1:
        res = "10 10\n"
        temp = []
        for _ in range(10):
            li = ['0', '1']
            temp.append("".join(list(te.get_choices(li, 10))+['\n']))
        return [res+"".join(temp)]
    elif prob_num == 2:
        return 2
    pass

num_probs = 1
num_test = 3
test_res = list()
for i in range(1, num_probs+1):
    i, e = te.test_probs_ntimes(te.test_prob, num_test, prob_num=i, dispatcher=dispatcher, get_input=get_prob_input, show_input_info=False)
    test_res.append({"info":i, "exec_time":e})
    print("-------")

import json
# 0번째 문제 1, 2번째 테스트 케이스 확인
cases = [1, 2]
for case_info in test_res[0]['info'][cases]:
    print(json.dumps(case_info, sort_keys=True, indent=4))
