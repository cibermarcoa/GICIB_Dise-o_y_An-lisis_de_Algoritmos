def esSolucion(countEnemigos, maxEnemigos):
    return countEnemigos == maxEnemigos

def esFactible(tablero, x, y, n, m, turno, maxDistance):
    if 0 <= x < m and 0 <= y < n and turno <= maxDistance:
        return tablero[y][x] == 1 or tablero[y][x] == 0

def laberinto(tablero, esSol, n, m, countEnemigos, maxEnemigos, initx, inity, maxDistance, turno):
    if esSolucion(countEnemigos, maxEnemigos):
        esSol = True
    else:
        posiciones = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for dx, dy in posiciones:
            if esFactible(tablero, initx + dx, inity + dy, n, m, turno, maxDistance):
                enemigos = []
                if tablero[inity + dy][initx + dx] == 1:
                    countEnemigos += 1
                    enemigos.append((inity + dy, initx + dx))
                tablero[inity + dy][initx + dx] = 2
                esSol = laberinto(tablero, esSol, n, m, countEnemigos, maxEnemigos, initx + dx, inity + dy, maxDistance, turno + 1)
                tablero[inity + dy][initx + dx] = 0
                for ey, ex in enemigos:
                    tablero[ey][ex] = 1
    return esSol

n, m, maxEnemigos = map(int, input().strip().split())
tablero = []
for _ in range(n):
    linea = list(map(int, input().strip().split()))
    tablero.append(linea)
inity, initx, maxDistance = map(int, input().strip().split())

countEnemigos = 0
if tablero[inity][initx] == 1:
    countEnemigos += 1
tablero[inity][initx] = 2
esSol = laberinto(tablero, False, n, m, countEnemigos, maxEnemigos, initx, inity, maxDistance, 1)
if esSol:
    print("ATACA")
else:
    print("CORRE")