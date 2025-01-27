def greedy(people, n, k):
    people.sort()
    separator = min(k, n - k)
    for i in range(separator):
        print(people[i][1], end=" ")
    print()
    for i in range(separator, n):
        print(people[i][1], end=" ")

n, k = map(int, (input().strip().split()))
people = []

for _ in range(n):
    name, age = input().strip().split()
    age = int(age)
    people.append([age, name])

greedy(people, n, k)