def selectBestItem(visited, distances, n):
    bestItem = None
    distance = float('inf')
    for i in range(n):
        if not visited[i] and distances[i] < distance:
            distance = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, n, start, end):
    distances = [float('inf')] * n
    visited = [False] * n
    distances[start] = 0
    visited[start] = True
    rec = [-1] * n
    for (next, cost) in g[start]:
        distances[next] = cost
    for _ in range(1, n):
        bestItem = selectBestItem(visited, distances, n)
        visited[bestItem] = True
        for next, cost in g[bestItem]:
            if distances[next] > distances[bestItem] + cost:
                distances[next] = distances[bestItem] + cost
                rec[next] = bestItem
    return distances[end], rec

g = []
n, m = map(int, input().strip().split())
for _ in range(n):
    g.append([])
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append((b, c))
    g[b].append((a, c))
start, end = map(int, input().strip().split())
sol, rec = dijkstra(g, n, start, end)
print(sol)
i = rec[end]
prev = []
prev.append(end)
while i != -1:
    prev.append(i)
    i = rec[i]
prev.append(start)
for i in reversed(range(len(prev))):
    print(prev[i], end=' ')