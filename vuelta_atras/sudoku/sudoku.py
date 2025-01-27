def estaEnCuadro(sol, f, c, num):
    esta = False
    fInf = 3 * (f // 3)
    fSup = 3 + fInf
    cInf = 3 * (c // 3)
    cSup = 3 + cInf
    f = fInf
    while not esta and f < fSup:
        c = cInf
        while not esta and c < cSup:
            esta = sol[f][c] == num
            c += 1
        f += 1
    return esta

def esFactible(sol, f, c, num):
    filaOk = not estaEnFila(sol, f, num)
    columnaOk = not estaEnColumna(sol, c, num)
    cuadroOk = not estaEnCuadro(sol, f, c, num)
    return filaOk and columnaOk and cuadroOk

def estaEnColumna(sol, c, num):
    for i in range(9):
        if sol[i][c] == num:
            return True
    return False

def estaEnFila(sol, f, num):
    return num in sol[f]

def esSolucion(sol, i):
    return i >= len(sol) ** 2

def sudoku(sol, i):
    if esSolucion(sol, i):
        esSol = True
    else:
        esSol = False
        f = i // 9
        c = i % 9
        if sol[f][c] != 0:
            [sol, esSol] = sudoku(sol, i + 1)
        else:
            num = 1
            while not esSol and num <= 9:
                if esFactible(sol, f, c, num):
                    sol[f][c] = num
                    [sol, esSol] = sudoku(sol, i + 1)
                    if not esSol:
                        sol[f][c] = 0
                num += 1
    return sol, esSol
sol = []

for _ in range(9):
    fila = list(map(int, input().strip().split()))
    sol.append(fila)

sol, esSol = sudoku(sol, 0)


for i in range(9**2):
    f = i // 9
    c = i % 9
    print(sol[f][c], end=" ")
    if c == 8:
        print()