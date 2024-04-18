
# 인터프리터 언어이기 때문에 미리 정의가 되어있어야 함수를 사용할 수 있다!!!!!!!!!!!!!!!!!!!
def add_min_mul_div(a, b):
    return a+b, a-b, a*b, a/b

# sum, min, mul, div = add_min_mul_div(4, 2)
sum = add_min_mul_div(4, 2)
# sum: (6, 2, 8, 2.0)
# 멀티리턴은 튜플로 반환


print("sum:", sum)
print("sum:", sum[3])
# print("multiply:", mul)
# print("minus:", min)
# print("divide:", div)

