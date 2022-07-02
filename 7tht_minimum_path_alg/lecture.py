"""
최단경로 알고리즘

- 1. 다익스트라 알고리즘
    1.1. 간단한 다익스트라 알고리즘
        - 수행 시간 분석
    1.2. 우선순위 큐를 이용한 다익스트라 알고리즘
"""

def dijkstra_alg():
    # 구현 방법을 듣고 내가 직접 구현 해본
    # 입력 받는 부분은 강의를 따른다.
    import sys
    input = sys.stdin.readline
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

    # 노드의 개수, 간선의 개수 입력 받기
    n, m = map(int, input().split())
    # 시작 노드 번호를 입력 받기
    start = int(input())
    #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for i in range(n+1)]
    #방문한 적이 있는지 체크하는 목적의 리스트 만들기
    visited = [False] * (n+1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)
    
    # 모든 간선 정보를 입력 받기
    for _ in range(m):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b,c))

    # 1. 시작노드는 0으로, 
    #       시작 노드에 연결된 친구들  
    def mine():
        # 방문하지 않은 노드 중 distance가 가장 작은 node 반환
        def get_smallest_node():
            min_cost = INF
            for i in range(1, n+1):
                if not visited[i] and min_cost > distance[i]:
                    min_cost = distance[i]
                    node = i
            return node
        distance[start] = 0
        while visited.count(True) != n-1: # 0과 마지막 노드를 제외했을 때
            a = get_smallest_node()
            for b, c in graph[a]:
                distance[b] = min(distance[b], distance[a]+c)
            visited[a] = True
        print(distance)

    def lecture():
        # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
        def get_smallest_node():
            min_value = INF
            index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
            for i in range(1, n+1):
                if distance[i] < min_value and not visited[i]:
                    min_value = distance[i]
                    index = i
            return index
        def dijstra(start):
            # 시작 노드에 대해서 초기화
            distance[start] = 0
            visited[start] = True
            
            for j in graph[start]:
                distance[j[0]] = j[1]
            
            # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
            for i in range(n-1):
                # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
                now = get_smallest_node()
                visited[now] = True
                # 현재 노드와 연결된 다른 노드를 확인
                for j in graph[now]:
                    cost = distance[now] + j[1]
                    # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
                    if cost < distance[j[0]]:
                        distance[j[0]] = cost

        # 다익스트라 알고리즘 수행
        dijstra(start)
        # 모든 노드로 가기 위한 최단 거리를 출력
        for i in range(1, n+1):
            # 도달할 수 없는 경우, 무한이라고 출력
            if distance[i] == INF:
                print("INFINITY")
            # 도달할 수 있는 경우 거리를 출력
            else:
                print(distance[i])
        pass

    # 당연히 생각했지만 귀찮아서 구현하지 않았던..
    # 출발 노드에 대해서 미리 연산한 후에 반복문으로 추가 연산하는 것...
    # 코드는 길어지지만 시간복잡도 측면에서 연산이 훨씬 적게 되므로 시작은 미리 해두자.
    #   첫 시작 노드때 get_small~ 노드를 구할 필요가 없으므로 V만큼 덜함


# 우선순위 큐
"""
# 힙 라이브러리 사용 예제: 최소 힙
파이썬 내의 힙 라이브러리
hippush: 힙에 데이터를 넣음 
    hippush(h, value)
    h라는 리스트에 value라는 데이터를 넣음
hippop: 데이터를 꺼냄
    hippop(h) h에서 1개를 pop함

우선순위가 높은 것부터 나온다는 특징 때문에 힙 라이브러리를 사용하여 정렬을 수행할 수 있다.
heapq는 min-heap 방식으로 구현되어 있기 때문에, 우선 순위가 낮은 원소부터 꺼내지게 된다.

자료를 넣을 때 O(logN)
n개의 자료를 넣을 때 O(NlogN)

즉, 오름차순으로 정렬하고 싶다
    == 그냥 힙 라이브러리에서 다 넣고 그대로 다 빼면 됨



내림차순으로 정렬하고 싶다. (큰 애부터 pop하고 싶다)

- 힙 라이브러리 사용 예제: 최대 힙
    - 넣을때, 꺼낼 때, 부호를 바꾸면 내부적으로 최소힙으로 동작하지만
        결과적으로 최대힙으로 됨
"""


import heapq

# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

test_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = heapsort(test_list)
print(result)

# 내림차순 힙 정렬
def heapsort_desc(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort_desc(test_list)
result

"""
- 다익스트라 알고리즘: 개선된 구현 방법
	- 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료 구조를 이용
	- 다익스트라 알고리즘이 동작하는 기본 원리는 동일하다
		- 현재 가장 가까운 노드를 저장해 놓기 위해 힙 자료구조를 추가적으로 이용한다는 점만 다르다
		- 현재의 최단 거리가 가장 짧은 노드 선택 - 최소 힙

힙 요소는 튜플일 수 있다. (value, label) 
    [heapq 문서](https://docs.python.org/ko/3/library/heapq.html)

## 등호 붙이고 빼고 주의
"""

def dijkstra_alg_improved():
    # 구현 방법을 듣고 내가 직접 구현 해본
    # 입력 받는 부분은 강의를 따른다.
    import heapq
    import sys
    input = sys.stdin.readline
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

    # 노드의 개수, 간선의 개수 입력 받기
    n, m = map(int, input().split())
    # 시작 노드 번호를 입력 받기
    start = int(input())
    #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
    graph = [[] for _ in range(n+1)]
    # 방문한 적이 있는지 체크하는 목적의 리스트 만들기
    # heap을 쓸때는 필요가 없음
    visited = [False] * (n+1)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)
    h = []
    
    # 모든 간선 정보를 입력 받기
    for _ in range(m):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
        graph[a].append((b,c))

    # 1. 시작노드는 0으로, 
    #       시작 노드에 연결된 친구들  
    def mine():
        # 방문하지 않은 노드 중 distance가 가장 작은 node 반환
        def get_smallest_node():
            while True:
                (cost, node) = heapq.heappop(h)
                if not visited[node]:
                    break
            return cost, node
        distance[start] = 0
        for node, cost in graph[start]:
            distance[node] = cost
            heapq.heappush(h, (cost, node))
        # 최종 최단 거리를 구하기 위해 총 n-1번, 시작(1) + 나머지(n-2)번 하면 된다.
        for _ in range(n-1):
            curr_cost, curr_node = get_smallest_node()
            visited[curr_node] = True
            for node, cost in graph[curr_node]:
                c = curr_cost + cost
                if distance[node] > c:
                    distance[node] = c
                    # 갱신이 일어날 때에만 push하면 될 것 같다 :)
                    heapq.push((c, node))
        print(distance)

    # 다익스트라 동작 과정 살펴보기(우선순위 큐) 본 후
    # visited 없어도 될 듯.
    # while heapq

    # 다시 짜볼까..
    def mine_2():
        distance[start] = 0
        heapq.heappush(h, (0, start))
        while h:
            curr_cost, curr_node = heapq.heappop(h)
            # 등호를 하면 안될듯 ㅇㅇㅇㅇ
            # 누락의 가능성이 있음
            if curr_cost >= distance[curr_node]: 
                continue
            for node, cost in graph[curr_node]:
                c = curr_cost + cost
                if distance[node] > c:
                    distance[node] = c
                    # 갱신이 일어날 때에만 push하면 될 것 같다 :)
                    heapq.push((c, node))
        print(distance)


    def lecture(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q: # q가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적 있는 노드라면 무시
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        # 다익스트라 알고리즘 수행
        lecture(start)
        
        # 모든 노드로 가기 위한 최단 거리를 출력
        for i in range(1, n+1):
            # 도달할 수 없는 경우, 무한이라고 출력
            if distance[i] == INF:
                print("INFINITY")
            # 도달할 수 있는 경우 거리를 출력
            else:
                print(distance[i])
        pass
