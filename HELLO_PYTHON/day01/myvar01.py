a = 1
b = 1.1
c = '3'

print(a + b) # unsupported operand type ==> 자바와 다르게 숫자와 문자를 연결해서 붙혀주지 않는다
print(str(a) +c)
print(a + int(c))

# python은 3~4글자 명령어가 많다