def dfsRec(graph, v, desc, low, time, art_points):
    desc[v] = low[v] = time[0]
    time[0] += 1
    for neigh in graph[v]:
        if not desc[neigh]:
            dfsRec(graph, neigh, desc, low, time, art_points)
            low[v] = min(low[v], low[neigh])
            if v and desc[v] <= low[neigh]:
                art_points.add(v)
        elif desc[v] > desc[neigh]:
            low[v] = min(low[v], desc[neigh])


def dfs(graph):
    n = len(graph)
    desc = [0] * n
    low = [0] * n
    time = [1]
    art_points = set()
    for v in range(n):
        if not desc[v]:
            dfsRec(graph, v, desc, low, time, art_points)
    return list(art_points)


if __name__ == "__main__":
    graph = []
    cost = []
    sum = 0

    n, m = map(int, input().strip().split())

    for i in range(n):
        cost.append([])
        graph.append([])
        c = int(input())
        cost[i] = c

    for i in range(m):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    sol = dfs(graph)
    for i in sol:
        sum += cost[i]
    print(sum)