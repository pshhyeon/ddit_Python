
# 인터프리터 언어이기 때문에 미리 정의가 되어있어야 함수를 사용할 수 있다!!!!!!!!!!!!!!!!!!!
def add(a, b):
    return a+b

def multiply(a, b):
    return a*b

def minus(a, b):
    return a-b

def divide(a, b):
    return a/b

def mod(a, b):
    return a%b

sum = add(4,2)
mul = multiply(4,2)
min = minus(4,2)
div = divide(4,2)
md = mod(4,2)

print("sum:", sum)
print("multiply:", mul)
print("minus:", min)
print("divide:", div)
print("mod:", md)

