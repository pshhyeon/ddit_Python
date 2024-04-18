from random import random
def getHJ():
    # 삼항 조건문
    # return '홀' if random() > 0.5 else '짝'
    if random() > 0.5 :
        return '홀'
    return '짝'

com = getHJ()
print("com:",com)