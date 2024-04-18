# 첫 별수를 입력하시오 >> 3
# 끝 별수를 입력하시오 >> 5
# ★★★
# ★★★★
# ★★★★★

def printStar(cnt):
    ret = ""
    for i in range(cnt):
        ret += "★"
    return ret
            
            
a = int(input('첫 별수를 입력하시오'))
b = int(input('끝 별수를 입력하시오'))

for i in range(a, b+1):
    print(printStar(i))

