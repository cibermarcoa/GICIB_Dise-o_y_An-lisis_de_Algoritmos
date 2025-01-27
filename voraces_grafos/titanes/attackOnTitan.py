import math

def updateComponents(components, new_id, old_id):
    for i in range(1, len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(aristas, n):
    components_in_mst = list(range(n))
    nComponentsInMST = n
    i = 0
    cost = 0
    while nComponentsInMST > 1 and i < len(aristas):
        origin = aristas[i][1]
        dest = aristas[i][2]
        peso = aristas[i][0]
        if components_in_mst[origin] != components_in_mst[dest]:
            cost += peso
            nComponentsInMST -= 1
            updateComponents(components_in_mst, origin, dest)
        i += 1
    return cost

n, m = map(int, input().strip().split())
aristas = []
for _ in range(m):
    o, d, p = map(int, input().strip().split())
    aristas.append([p, o, d])
    aristas.append([p, d, o])
aristas.sort()
cost = kruskal(aristas, n)
gas = math.ceil(cost / 5)
print(gas)