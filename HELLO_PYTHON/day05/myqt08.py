import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox, Qt

# ui파일 불러오기
form_class = uic.loadUiType("myqt08.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        # self.pb0.clicked.connect(lambda : self.myClick("0")) # ==> def myClick(self, clicked_num) 호출
        self.pb0.clicked.connect(self.myClick)
        self.pb1.clicked.connect(self.myClick)
        self.pb2.clicked.connect(self.myClick)
        self.pb3.clicked.connect(self.myClick)
        self.pb4.clicked.connect(self.myClick)
        self.pb5.clicked.connect(self.myClick)
        self.pb6.clicked.connect(self.myClick)
        self.pb7.clicked.connect(self.myClick)
        self.pb8.clicked.connect(self.myClick)
        self.pb9.clicked.connect(self.myClick)
        self.pb_call.clicked.connect(self.myCall)
    
    def myCall(self):
        str_tel = self.le.text()
        self.le.setAlignment(Qt.AlignRight)
        self.le.setStyleSheet("color : green")
        QMessageBox.about(self,'calling',str_tel)
    
    def myClick(self) :
        str_old = self.le.text()
        str_new = str_old + self.sender().text()
        self.le.setText(str_new)
        
        # str = self.le.text();
        # self.le.setText(str + clicked_num)

# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
