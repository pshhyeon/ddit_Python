# 홀 / 짝을 입력하세요 홀
# 나: 홀
# 컴: 짝
# 결과: 짐
from random import random


com = ""
mine = ""
result = ""

# 삼항 연산자
# [변수(생략가능)] = [참일때 반환값] if [조건] else [거짓일때 반환값]

if random() >= 0.5 : 
    com = '홀'
else :
    com = '짝'
    
# print(com)

mine = input('홀 / 짝을 입력하세요.')
print('mine:',mine)
print('com:',com)
print('이김' if mine == com else '짐')
