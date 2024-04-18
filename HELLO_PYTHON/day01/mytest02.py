# 첫 수를 입력하시오 : 1 5 8
# 끝 수를 입력하시오 : 3 3 8
# 1은 3보다 작다
# 5는 3보다 크다
# 8과 8은 같다

a = int(input("첫 수를 입력하시오"))
b = int(input("끝 수를 입력하시오"))

if a < b : 
    print("{}은(는) {}보다 작다".format(a, b))
elif a > b : 
    print("{}은(는) {}보다 크다".format(a, b))
else : 
    print("{}은(는) {}과 같다".format(a, b))