arr = [-15, 8, -31, 47, -2, 19]
max = arr[0]
min = arr[0]

for x in arr:
    if(x>max):
        max = x
    if(x<min):
        min = x

print("max", max)
print("min", min)