import math

def mochila(data, energia, n):
    candidates = []
    sol = 0
    i = 0
    while energia > 0 and i < n:
        ratio, identificador, estela, coste = data[i]
        if energia < coste:
            sol += (energia / ratio)
            energia -= energia
        else:
            sol += estela
            energia -= coste
        candidates.append(identificador)
        i += 1
    return sol, candidates

n, energia = map(int, input().strip().split())
data = []
for _ in range(n):
    a, b, c, = map(int, input().strip().split())
    data.append((c / b, a, b, c))
data.sort()
sol, candidates = mochila(data, energia, n)
print(math.floor(sol / 100))
candidates.sort()
for candidate in candidates:
    print(candidate, end=' ')