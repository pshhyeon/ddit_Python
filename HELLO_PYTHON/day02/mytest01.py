# 구구단
# 출력단수를 입력하시오 6
# 6*1=6 
# ···
# 6*9=54

dan = int(input('출력단수를 입력하시오'))
for i in range(1,9+1):
    print('{}*{}={}'.format(dan, i, (dan*i)))

print()

print('{}*{}={}'.format(dan, 1, (dan*1)))
print('{}*{}={}'.format(dan, 2, (dan*2)))
print('{}*{}={}'.format(dan, 3, (dan*3)))
print('{}*{}={}'.format(dan, 4, (dan*4)))
print('{}*{}={}'.format(dan, 5, (dan*5)))
print('{}*{}={}'.format(dan, 6, (dan*6)))
print('{}*{}={}'.format(dan, 7, (dan*7)))
print('{}*{}={}'.format(dan, 8, (dan*8)))
print('{}*{}={}'.format(dan, 9, (dan*9)))