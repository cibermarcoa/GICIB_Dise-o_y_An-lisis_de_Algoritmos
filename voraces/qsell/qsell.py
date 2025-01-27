def greedy(tiempo, parejas):
    for i in range(len(parejas)):
        benefit = 0
        parejas[i].sort(reverse=True)
        j = 0
        while (tiempo[i] != 0 and j < len(parejas[i])):
            if tiempo[i] > parejas[i][j][2]:
                tiempo[i] -= parejas[i][j][2]
                benefit += parejas[i][j][0] * parejas[i][j][2]
            elif tiempo[i] <= parejas[i][j][2]:
                benefit += parejas[i][j][0] * tiempo[i]
                tiempo[i] = 0
            print(parejas[i][j][1], end=" ")
            j += 1
        print()
        print(format(benefit, ".2f"))

tiempo = []
parejas = []
numConcursantes = int(input().strip())
for _ in range(numConcursantes):
    cualidadBuscada = input().strip()
    t = int(input().strip())
    tiempo.append(t)
    numPosiblesParejas = int(input().strip())
    posiblesParejas = []
    for _ in range(numPosiblesParejas):
        data = input().strip().split()
        name = data[0]
        if cualidadBuscada == 'beauty':
            cuality = int(data[1])
        elif cualidadBuscada == 'intelligence':
            cuality = int(data[2])
        elif cualidadBuscada == 'kindness':
            cuality = int(data[3])
        time = int(data[4])
        posiblesParejas.append((cuality / time, name, time))
    parejas.append(posiblesParejas)

greedy(tiempo, parejas)
