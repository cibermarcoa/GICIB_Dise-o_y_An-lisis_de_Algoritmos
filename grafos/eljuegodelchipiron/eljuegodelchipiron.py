from collections import deque

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs_aux(graph, visited, n, m):
    visited[0][0] = True
    if graph[0][0] == 2:
        return 1
    q = deque([(0, 0, 1)])
    while q:
        x, y, turn = q.popleft()
        if graph[x][y] == 2:
            return turn - 1
        for dx, dy in mov:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if (not visited[nx][ny]) and ((graph[nx][ny] != -1) or (turn % 2)):
                    visited[nx][ny] = True
                    q.append((nx, ny, turn + 1))
    return -1

def bfs(graph, n, m):
    visited = []
    for _ in range(n):
        fila = []
        for _ in range(m):
            fila.append(False)
        visited.append(fila)

    return bfs_aux(graph, visited, n, m)

n, m = map(int, input().strip().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().strip().split())))
print(bfs(g, n, m))
