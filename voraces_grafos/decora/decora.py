def selectBestItem(distances, visited, n):
    bestItem = 0
    cost = float('inf')
    for i in range(1, n):
        if not visited[i] and distances[i] < cost:
            cost = distances[i]
            bestItem = i
    return bestItem

def dijkstra(g, n):
    visited = [False] * n
    distances = [float('inf')] * n
    visited[0] = True
    distances[0] = 0
    sol = 0
    for init, end, cost in g[0]:
        distances[end] = cost
    for _ in range(1, n):
        bestItem = selectBestItem(distances, visited, n)
        visited[bestItem] = True
        for (init, end, cost) in g[bestItem]:
            distances[end] = min(distances[end], distances[bestItem] + cost)
    for _ in range(1,n):
        sol += distances[_]
    return sol

g = []
n, m, t = map(int, input().strip().split())
for _ in range(n):
    g.append([])
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append((a,b,c))
    g[b].append((b,a,c))
sol = dijkstra(g, n)
if sol <= t:
    print(sol)
else:
    print("Aleg, ¡a decorar!")