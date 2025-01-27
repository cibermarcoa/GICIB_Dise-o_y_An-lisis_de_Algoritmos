def selectBestItems(visited, distances, n):
    bestItem = 0
    distance = float('inf')
    for i in range(n):
        if not visited[i] and distance > distances[i]:
            distance = distances[i]
            bestItem = i
    return bestItem

def dijikstra(g, n, initial):
    distances = [float('inf')] * n
    visited = [False] * n
    visited[initial] = True
    distances[initial] = 0
    sol = 0
    for (next, cost) in g[initial]:
        distances[next] = cost
    for _ in range(1, n):
        bestItem = selectBestItems(visited, distances, n)
        visited[bestItem] = True
        for (next, cost) in g[bestItem]:
            distances[next] = min(distances[next], distances[bestItem] + cost)
    for i in range(n):
        if distances[i] > sol:
            sol = distances[i]
    return sol

g = []
n, m = map(int, input().strip().split())
sol = 0
for _ in range(n):
    g.append([])
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append((b, c))
    g[b].append((a, c))
for i in range(n):
    cost = dijikstra(g, n, i)
    if cost > sol:
        sol = cost
print(sol)