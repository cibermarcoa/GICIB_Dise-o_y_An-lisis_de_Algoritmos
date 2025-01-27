def dfs(g):
    visited = set()
    dfsRec(0, visited, g)
    return len(visited)

def dfsRec(node, visited, g):
    visited.add(node)
    if g[node] or len(g) == len(visited):
        for neigh in g[node]:
            if neigh not in visited and not dfsRec(neigh, visited, g):
                return False
        return True
    return False

if __name__ == "__main__":
    g = []
    n, m = map(int, input().strip().split())
    for _ in range(n):
        g.append([])
    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)
    if n == dfs(g):
        print("PERFECTO")
    else:
        print("CAMBIA EL ITINERARIO")