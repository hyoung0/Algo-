import sys
from collections import deque


# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()
        for i in range(1, 7):
            dice = target + i

            if dice > 100:
                continue

            cnt = graph[dice]

            if visited[cnt] == 0:
                queue.append(cnt)
                visited[cnt] = visited[target] + 1

                if cnt == 100:
                    return


n, m = map(int, sys.stdin.readline().split())

graph = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] = b

visited = [0] * 101

bfs(1)

print(visited[100] - 1)