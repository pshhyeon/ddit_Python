# 숫자 맞추기
# random으로 1~99 정수를 com 지정
# 50이라고 가정했을 경우
# '정수를 입력하시오'
# 업 / 다운 판단 맞추면 break
# 10번 넘을시 경고문 출력
from random import random

rnd = int(random()*99) + 1
flag_ans = False
print(rnd)


for i in range(10):
    num = int(input('1~99중 정수를 입력'))
    if num > rnd :
        print('{} DOWN'.format(num))
    elif num < rnd :
        print('{} UP'.format(num))
    else :
        print('정답입니다: ',num)
        flag_ans = True
        break

if not flag_ans : print('똑바로 하세요')
        


    