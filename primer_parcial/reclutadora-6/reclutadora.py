def greedyBackpack(n, candidates, money):
    total = 0
    sol = []
    i = 0
    while money > 0 and i < n:
        ratio, candidate, salary = candidates[i]
        if salary <= money:
            money -= salary
            total += ratio * salary
        else:
            total += ratio * money
            money = 0
        sol.append(candidate)
        i += 1
    print("{:.2f}".format(total))
    for i in range(len(sol)):
        print(sol[i], end=" ")
    print()

n = int(input().strip())
pentester = []
crayontester = []
penciltester = []
for _ in range(n):
    data = input().strip().split()
    name = data[0]
    a = int(data[1])
    s = int(data[2])
    i = int(data[3])
    g = int(data[4])
    pentester.append(((a/g), name, g))
    crayontester.append(((s / g), name, g))
    penciltester.append(((i / g), name, g))
pentester.sort(reverse=True)
crayontester.sort(reverse=True)
penciltester.sort(reverse=True)
nEquipos = int(input().strip())
for _ in range(nEquipos):
    team, maxMoney = map(int, input().strip().split())
    if team == 0:
        greedyBackpack(n, pentester, maxMoney)
    if team == 1:
        greedyBackpack(n, crayontester, maxMoney)
    if team == 2:
        greedyBackpack(n, penciltester, maxMoney)