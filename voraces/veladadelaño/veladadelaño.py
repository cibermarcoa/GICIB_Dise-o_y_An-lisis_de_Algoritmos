def greedy(activities):
    activities.sort()
    lastTime = -1
    sol = 0
    for end, init in activities:
        if lastTime < init:
            sol += 1
            lastTime = end
    return sol

n = int(input().strip())
activities = []

for _ in range(n):
    data = input().strip().split()
    init = int(data[1])
    end = int(data[2])
    activities.append((end, init))

sol = greedy(activities)
print(sol)