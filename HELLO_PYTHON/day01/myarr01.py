arr = ["aaa", "bbb"]

# 자바와 다르게 주소값이 나오지 않고 배열이 그대로 출력됨
print(arr)

# 뒤에다 붙이기 append
arr.append('ccc')
print(arr)

# index를 지정해서 삽입하기
arr.insert(0, "ddd")
print(arr)
arr.insert(3, "eee")
print(arr)

arr.sort()
print(arr)

arr.reverse()
print(arr)

arr.append('aaa')
print(arr.count('aaa'))

print(arr.index('aaa', 0, 5)) # 0~5사이의 'aaa'의 위치

print(len(arr)) # len(arr) arr의 길이 구하기
arr.insert(len(arr), "fff") # append와 같은기능 