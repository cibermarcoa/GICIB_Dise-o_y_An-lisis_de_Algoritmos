def obtenerFin(actividad):
    return actividad[1]

def maxActividades(g, i):
    sol = 0
    g[i].sort(key=obtenerFin)
    last_max = 0

    for init, last in g[i]:
        if init >= last_max:
            sol += 1
            last_max = last

    return sol

actividades = []

T = int(input())

for i in range(T):
    actividades.append([])
    N = int(input())
    datos = list(map(int, input().strip().split()))

    for j in range(0, N * 2, 2):
        a = datos[j]
        b = datos[j + 1]
        actividades[i].append((a, b))

for i in range(T):
    solution = maxActividades(actividades, i)
    print(solution)