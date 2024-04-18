from random import random

# arr = [1, 2, 3, ···, 43, 44, 45]
#함수형 배열을 리스트로 변환하여 배열 초기화
# arr = list(range(1, 45 +1))

# 로또번호임을 인지시켜주기위해 손수 작성하면 다른사람이 알기 쉬움
arr = [
       1,  2,  3,  4,  5,  6,  7,  8,  9, 10 
    , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 
    , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 
    , 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 
    , 41, 42, 43, 44, 45 
]
for i in range(999) :
    rnd = int(random() * 45)
    temp = arr[0]
    arr[0] = arr[rnd]
    arr[rnd] = temp

# 기본값은 end='\n' ==> end=',' 로 변경하여 이어서 출력 
print(arr[0], end=',')
print(arr[1], end=',')
print(arr[2], end=',')
print(arr[3], end=',')
print(arr[4], end=',')
print(arr[5])