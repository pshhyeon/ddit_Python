import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# ui파일 불러오기
form_class = uic.loadUiType("myqt03.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myClick)
    
    #btn이 눌리면 작동할 함수
    def myClick(self) :
        le01_text = self.le01.text()
        le02_text = self.le02.text()
        le01_num = int(le01_text)
        le02_num = int(le02_text)
        result = le01_num - le02_num
        self.le03.setText(str(result))
        

# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
