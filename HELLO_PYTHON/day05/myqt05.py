import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# ui파일 불러오기
form_class = uic.loadUiType("myqt05.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myClick)
    
    #btn이 눌리면 작동할 함수
    def myClick(self) :
        arr = [
               1,  2,  3,  4,  5,  6,  7,  8,  9, 10 
            , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 
            , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 
            , 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 
            , 41, 42, 43, 44, 45 
        ]
        
        for i in range(999) :
            rnd = int(random() * 45)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
        
        for i in range(6) :
            for j in range(6):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        
        self.lcd1.display(arr[0])
        self.lcd2.display(arr[1])
        self.lcd3.display(arr[2])
        self.lcd4.display(arr[3])
        self.lcd5.display(arr[4])
        self.lcd6.display(arr[5])
        


# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
