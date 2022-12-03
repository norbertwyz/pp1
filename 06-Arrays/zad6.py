arr = [2, 3, 7, 5, 4]

print(f' a. {arr}')

print(f' b. {len(arr)}')

print(f' c. {arr[0]}')

print(f' d. {arr[1]}')

print(f' e. {arr[-1]}')

print(f' f. {arr[-2]}')

print(f' g. {arr[0] + arr[-1]}')

print(f' h. {arr[len(arr)//2]}')

print("i. ")
for x in arr:
    print(x, end=" ")
print("")
print("j. ")
for x in range(0,int(len(arr)/2) + 1):
    print(arr[x], end=" ")
