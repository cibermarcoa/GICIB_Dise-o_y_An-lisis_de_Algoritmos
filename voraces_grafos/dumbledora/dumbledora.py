def updateComponents(components, new_id, old_id):
    for i in range(len(components)):
        if components[i] == new_id:
            components[i] = old_id

def kruskal(g, n, costes):
    sol = 0
    candidates = g
    components = list(range(n))
    count = len(components)

    i = 0
    while i < len(candidates) and count > 0:
        (cost, init, end) = candidates[i]
        if components[init] != components[end]:
            updateComponents(components, components[init], components[end])
            count -= 1
            costes[init] += cost
            costes[end] += cost
            sol += cost
        i += 1
    return sol

n, m = map(int, input().strip().split())
g = []
costes = []
for _ in range(n):
    costes.append(0)
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    g.append((c, a, b))
    g.append((c, b, a))

g.sort()
sol = kruskal(g, n, costes)

print("Coste total: " + str(sol))
for i in range(n):
    print("H"+str(i)+": " + str(costes[i]))