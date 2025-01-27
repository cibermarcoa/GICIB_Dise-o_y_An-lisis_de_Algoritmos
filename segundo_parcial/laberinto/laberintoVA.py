import copy

def esSolucion(initx, inity, endx, endy, enemigosEliminados, enemigosMaximos):
    return initx == endx and inity == endy and enemigosEliminados == enemigosMaximos

def esMejor(laberinto, mejorSol, endx, endy):
    if laberinto[endy][endx] < mejorSol[endy][endx]:
        return copy.deepcopy(laberinto)
    else:
        return mejorSol

def esFactible(laberinto, x, y, n, m):
    if 0 <= x < m and 0 <= y < n:
        return laberinto[y][x] == -1 or laberinto[y][x] == 0

def poda(mejorSol, x, y, turno):
    return turno < mejorSol[y][x]

def laberintoVA(laberinto, mejorSol, initx, inity, endx, endy, turno, n, m, enemigosEliminados, enemigosMaximos):
    if esSolucion(initx, inity, endx, endy, enemigosEliminados, enemigosMaximos):
        mejorSol = esMejor(laberinto, mejorSol, endx, endy)
    else:
        if poda(mejorSol, endx, endy, turno):
            movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in movimientos:
                if esFactible(laberinto, initx + dx, inity + dy, n, m):
                    enemigos = []
                    if laberinto[inity + dy][initx + dx] == -1:
                        enemigosEliminados += 1
                        enemigos.append((initx + dx, inity + dy))
                    laberinto[inity + dy][initx + dx] = turno
                    mejorSol = laberintoVA(laberinto, mejorSol, initx + dx, inity + dy, endx, endy, turno + 1, n, m, enemigosEliminados, enemigosMaximos)
                    laberinto[inity + dy][initx + dx] = 0
                    while enemigos:
                        (ex, ey) = enemigos.pop()
                        laberinto[ey][ex] = -1
                        enemigosEliminados -= 1
    return mejorSol

laberinto = []
n, m, enemigosMaximos = map(int, input().strip().split())
inity, initx = map(int, input().strip().split())
endy, endx = map(int, input().strip().split())
for _ in range(n):
    linea = list(map(int, input().strip().split()))
    laberinto.append(linea)
mejorSol = copy.deepcopy(laberinto)
mejorSol[endy][endx] = float('inf')
laberinto[inity][initx] = 1
enemigosEliminados = 0
sol = laberintoVA(laberinto, mejorSol, initx, inity, endx, endy, 2, n, m, enemigosEliminados, enemigosMaximos)
print(sol[endy][endx])
