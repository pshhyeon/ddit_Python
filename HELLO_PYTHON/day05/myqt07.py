import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

# ui파일 불러오기
form_class = uic.loadUiType("myqt07.ui")[0]


# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myClick)
    
    # btn이 눌리면 작동할 함수
    def myClick(self):
        
        rnd = random()
        com = ''
        if rnd > 0.6:
            com = '가위'
        elif rnd > 0.3: 
            com = '바위'
        else:
            com = '보'
        
        print(com)
        
        mine = self.pte_mine.toPlainText();

        result = ''
        if mine == com: result = '비겼습니다'
        elif mine == "가위" and com == "보": result = "이겼습니다" 
        elif mine == "가위" and com == "바위": result = "졌습니다" 
        elif mine == "바위" and com == "가위": result = "이겼습니다" 
        elif mine == "바위" and com == "보": result = "졌습니다" 
        elif mine == "보" and com == "바위": result = "이겼습니다" 
        elif mine == "보" and com == "가위": result = "졌습니다." 
        
        
        self.pte_com.setPlainText(com)
        self.pte_result.setPlainText(result)


# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
