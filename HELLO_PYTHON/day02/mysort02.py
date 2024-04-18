from random import random
arr = [6, 5, 4, 3, 2, 1]

for i in range(3) :
    for j in range(3):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)