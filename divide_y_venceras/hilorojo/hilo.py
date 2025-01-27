
def bin_rec(v, num, low, high):
    if low > high:
        return -1
    mid = (low + high) //2
    if v[mid] == num:
        return mid
    elif num < v[mid]:
        return bin_rec(v, num, low, mid - 1)
    else:
        return bin_rec(v, num, mid + 1, high)

def binarySearch(v1, num, n):
    return bin_rec(v1, num, 0, n - 1)

n1 = int(input())
v1 = list(map(int, input().strip().split()))
n2 = int(input())
v2 = list(map(int, input().strip().split()))
m = int(input())
parejas = []
for _ in range(m):
    a, b = map(int, input().strip().split())
    parejas.append((a, b))

for (a, b) in parejas:
    sol1 = binarySearch(v1, a, n1)
    sol2 = binarySearch(v2, b, n2)
    if sol1 == -1 or sol2 == -1:
        print("SIN DESTINO")
    else:
        print(str(sol1) + " " + str(sol2))
