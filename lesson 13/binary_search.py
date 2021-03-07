a = [1,3,4,6,8,7,5]
value = int(input())
mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <=high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No number")
else:
    print("Number =", mid)
