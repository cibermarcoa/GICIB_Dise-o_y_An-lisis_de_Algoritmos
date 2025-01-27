def greedy(n, candidates):
    candidates.sort(reverse=True)
    bestItem = 0
    totalItems = 0
    count = 0
    solution = dict()

    while (n > 0 and bestItem < len(candidates)):
        count = 0
        while (n >= candidates[bestItem]):
            n -= candidates[bestItem]
            count += 1
            solution[candidates[bestItem]] = count
            totalItems += 1
        bestItem += 1

    return totalItems, solution

n = int(input().strip())
candidates = list(map(int, input().strip().split()))

totalItems, solution = greedy(n, candidates)
print(totalItems)
for key, value in solution.items():
    print(str(key) + ": " + str(value))