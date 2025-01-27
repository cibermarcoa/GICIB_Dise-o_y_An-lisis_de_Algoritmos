from collections import deque


def selectBestItem(visited, distances, n):
    bestItem = None
    distance = float('inf')
    for i in range(n):
        if not visited[i] and distance > distances[i]:
            bestItem = i
            distance = distances[i]
    return bestItem

def dijkstra(g, n, initial):
    visited = [False] * n
    distances = [float('inf')] * n
    visited[initial] = True
    distances[initial] = 0
    prev = [-1] * n
    sol = 0
    bestItem = None
    for next, cost in g[initial]:
        distances[next] = cost
    for _ in range(1,n):
        bestItem = selectBestItem(visited, distances, n)
        visited[bestItem] = True
        for next, cost in g[bestItem]:
            if distances[next] > cost + distances[bestItem]:
                distances[next] = cost + distances[bestItem]
                prev[next] = bestItem
    for i in range(n):
        sol += distances[i]
    return sol, prev, bestItem

g = []
n, m = map(int, input().strip().split())
for _ in range(n):
    g.append([])
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append((b, c))
    g[b].append((a, c))
nIds = int(input().strip())
ids = [False] * n
for _ in range(nIds):
    p = int(input().strip())
    ids[p] = True


maxLatency = 0
bestNode = None
bestRec = []
last = None
for i in range(n):
    sol, rec, last = dijkstra(g, n, i)
    if sol > maxLatency:
        maxLatency = sol
        bestNode = i
        bestRec = rec
print(bestNode, maxLatency)
i = last
trueRec = []
while i != -1:
    trueRec.append(i)
    i = bestRec[i]
trueRec.append(bestNode)
for i in range(len(trueRec) - 1, 0, -1):
    print(trueRec[i], end=" ")
