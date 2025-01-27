def greedy(users, n, selectedName):
    users.sort()
    selector = True
    sol = 0
    for i in range(n):
        print(users[i][1])
        if users[i][1] == selectedName:
            selector = False
        if selector:
            sol += users[i][2]
    return sol

n = int(input().strip())
users = []
selectedName = None
for _ in range(n):
    user = []
    data = input().strip().split()
    if selectedName == None or data[0] < selectedName:
        selectedName = data[0]
    user.append(int(data[1])/int(data[2]))
    user.append(data[0])
    user.append(int(data[3]))
    users.append(user)

sol = greedy(users, n, selectedName)
print(sol)