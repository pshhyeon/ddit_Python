import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# ui파일 불러오기
form_class = uic.loadUiType("myqt04.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myClick)
    
    #btn이 눌리면 작동할 함수
    def myClick(self) :
        # le01 ~ le 02 le03 배수 합은 le04
        le01_text = self.le01.text()
        le02_text = self.le02.text()
        le03_text = self.le03.text()
        le01_num = int(le01_text)
        le02_num = int(le02_text)
        le03_num = int(le03_text)
        result = 0
        
        for i in range(le01_num, le02_num+1) :
            if i % le03_num == 0 :
                result += i
        self.le04.setText(str(result))
        

# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
