def toposort(g):
    n = len(g)
    aristas_entrantes = [0] * n
    for u in range(n):
        for v in g[u]:
            aristas_entrantes[v] += 1
    nodos_iniciales = []
    for i in range(n):
        if aristas_entrantes[i] == 0:
            nodos_iniciales.append(i)
    nodos_iniciales.sort()
    topological_sort = []
    while nodos_iniciales:
        origen = nodos_iniciales.pop(0)
        topological_sort.append(origen)
        for adj in g[origen]:
            aristas_entrantes[adj] -= 1
            if aristas_entrantes[adj] == 0:
                nodos_iniciales.append(adj)
                nodos_iniciales.sort()
    for node in topological_sort:
        print(node, end=" ")

if __name__ == "__main__":
    g = []
    n, m = map(int, input().strip().split())
    for _ in range(n):
        g.append([])
    for _ in range(m):
        a, b = map(int, input().strip().split())
        g[a].append(b)
    for lista in g:
        lista.sort()
    toposort(g)