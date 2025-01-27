import copy

def esFactible(sol, i, datos):
    return sol['Objeto'][i] < 1 and sol['PesoAc'] + datos['Peso'][i] <= datos['P']

def mejor(sol, mejorSol):
    if sol['ValorAc'] > mejorSol['ValorAc']:
        return copy.deepcopy(sol)
    return mejorSol

def esSolucion(sol, datos):
    return sol['PesoAc'] + min(datos['Peso']) > datos['P']

def poner(sol, i, datos):
    sol['ValorAc'] += datos['Valor'][i]
    sol['PesoAc'] += datos['Peso'][i]
    sol['Objeto'][i] += 1
    return sol

def borrar(sol, i, datos):
    sol['ValorAc'] -= datos['Valor'][i]
    sol['PesoAc'] -= datos['Peso'][i]
    sol['Objeto'][i] -= 1
    return sol

def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos):
        mejorSol = mejor(sol, mejorSol)
    else:
        for i in range(k, datos['N']):
            if esFactible(sol, i, datos):
                sol = poner(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i)
                sol = borrar(sol, i, datos)
    return mejorSol

def inicializarSol(n):
    sol = {}
    sol['ValorAc'] = 0
    sol['PesoAc'] = 0
    sol['Objeto'] = [0] * n
    return sol

def inicializarDatos(read, n, p):
    datos = {}
    datos['N'] = n
    datos['P'] = p
    datos['Nombre'] = []
    datos['Peso'] = []
    datos['Valor'] = []
    for nombre, peso, valor in read:
        datos['Nombre'].append(nombre)
        datos['Peso'].append(peso)
        datos['Valor'].append(valor)
    return datos

n, p, b = map(int, input().strip().split())
read = []
for _ in range(n):
    data = list(input().strip().split())
    read.append((data[0], int(data[1]), int(data[2])))
read.sort()
datos = inicializarDatos(read, n, p)
sol = inicializarSol(n)
mejorSol = inicializarSol(n)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
totalValue = 0
totalWeight = 0
for i in range(n):
    if mejorSol['Objeto'][i] == 1:
        print(datos['Nombre'][i], end=" ")
        totalValue += datos['Valor'][i]
        totalWeight += datos['Peso'][i]
print("\n" + str(totalWeight) + " " + str(totalValue))
if mejorSol['ValorAc'] > b:
    print("SE VA")
else:
    print("VUELVE")
