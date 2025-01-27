from collections import deque

def bfs(g, m):
    visited = set()
    q = deque([(0, 1)])
    while q:
        aux, d = q.popleft()
        visited.add(aux)
        if d < m:
            for neighbor in g[aux]:
                if neighbor not in visited:
                    q.append((neighbor, d + 1))
    return len(visited)

if __name__ == "__main__":
    g = []
    n = int(input().strip())
    for i in range(n):
        g.append([])
        m, k, c = map(int, input().strip().split())
        for _ in range(k):
            g[i].append([])
        for _ in range(c):
            a, b = map(int, input().strip().split())
            g[i][a].append(b)
            g[i][b].append(a)
        print(bfs(g[i], m))
