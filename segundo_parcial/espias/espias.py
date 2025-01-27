def updateComponents(components, oldid, newid):
    for i in range(len(components)):
        if components[i] == oldid:
            components[i] = newid

def kruskal(g, n):
    count = n
    i = 0
    sol = 0
    components = list(range(n))
    espias = [0] * n
    while i < len(g) and count > 1:
        cost, init, end = g[i]
        if components[init] != components[end]:
            sol += cost
            espias[init] += 1
            espias[end] += 1
            count -= 1
            updateComponents(components, components[init], components[end])
        i += 1
    return sol, espias

n, m = map(int, input().strip().split())
g = []
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g.append((c, a, b))
g.sort()
sol, espias = kruskal(g, n)
print(sol)
for espia in espias:
    print(espia, end=' ')