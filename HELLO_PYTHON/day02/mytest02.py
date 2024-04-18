# 가위 / 바위 / 보를 입력하시오
# 나: 가위 / 컴: 보 ==> 이김
# r > 0.66 가위 / r > 0.33 바위 / 보
from random import random

rnd = random()
com = ''

if rnd > 0.66 : 
    com = '가위'
elif rnd > 0.33 : 
    com = '바위'
else : 
    com = '보'

# print(com)

user = input('가위||바위||보를 입력하시오.')

print('user:'+user)
print('com:'+com)

# 가독성을 높이기 위해 if문 하나하나 적어주는것도 좋다
if user == com :
    print('비김')
elif (user == '가위' and com == '바위') or (user == '바위' and com == '보') or (user == '보' and com == '가위') :
    print('짐')
else : 
    print('이김')
    
