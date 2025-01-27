def esFactible(mapa, nuevaFila, nuevaColumna):
    return 0 <= nuevaFila < len(mapa) and 0 <= nuevaColumna < len(mapa[0]) and (mapa[nuevaFila][nuevaColumna] == 0 or mapa[nuevaFila][nuevaColumna] == 1 or mapa[nuevaFila][nuevaColumna] == 2)

def esSolucion(sx, sy, ex, ey, total_anillos, cont_anillos):
    return sx == ex and sy == ey and total_anillos == cont_anillos

def encontrarEnemigos(mapa, sx, sy, ex, ey, total_anillos, cont_anillos, tiempoi, tiempof, visited):
    visited.add((sx, sy))
    if esSolucion(sx, sy, ex, ey, total_anillos, cont_anillos):
        tiempof = min(tiempof, tiempoi)
    else:
        desplazamientos = [[1,0],[0,1],[-1,0],[0,-1]]
        for x, y in desplazamientos:
            nuevaFila = sx + x
            nuevaColumna = sy + y
            if esFactible(mapa, nuevaFila, nuevaColumna):
                while esFactible(mapa, nuevaFila, nuevaColumna):
                    cont_anillos += mapa[nuevaFila][nuevaColumna] == 1
                    tiempoi = tiempoi + 1
                    nuevaFila = nuevaFila + x
                    nuevaColumna = nuevaColumna + y
                nuevaFila -= x
                nuevaColumna -= y
                if (nuevaFila, nuevaColumna) not in visited:
                    tiempof = encontrarEnemigos(mapa, nuevaFila, nuevaColumna, ex, ey, total_anillos, cont_anillos, tiempoi, tiempof, visited)
                while sx != nuevaFila or sy != nuevaColumna:
                    cont_anillos -= mapa[nuevaFila][nuevaColumna] == 1
                    tiempoi = tiempoi - 1
                    nuevaFila = nuevaFila - x
                    nuevaColumna = nuevaColumna - y

    visited.remove((sx, sy))
    return tiempof

n = int(input().strip())
mapa = []
total_anillos = 0
for _ in range(n):
    linea = list(map(int, input().strip().split()))
    if 1 in linea:
        total_anillos += linea.count(1)
    mapa.append(linea)
sx, sy, ex, ey = map(int, input().strip().split())

tiempoi = 0
tiempof = float('inf')
sol = 0
cont_anillos = 0
if mapa[sx][sy] == 1:
    cont_anillos += 1
visited = set()
sol = encontrarEnemigos(mapa, sx, sy, ex, ey, total_anillos, cont_anillos, tiempoi, tiempof, visited)
print(sol+1)