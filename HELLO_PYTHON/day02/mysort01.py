arr = [10, 1, 37, 3, 23, 14]
print(arr)

for i in range(len(arr)) :
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

# arr.sort()
print(arr)


'''
# Python버블정렬 로직 ==> n(n²-n)/2
for i in range(len(arr)) :
    # 마지막 요소는 이미 정렬되어 있으므로 (n-i-1)까지만 반복
    for j in range(0, len(arr)-i-1) :
        if arr[j] > arr[j+1] :
            # 병렬 교환
            arr[j], arr[j+1] = arr[j+1], arr[j]
'''