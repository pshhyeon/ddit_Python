import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from PyQt5.Qt import QMessageBox

# ui파일 불러오기
form_class = uic.loadUiType("myqt09.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.com = 0
        self.ranCom()
        
        self.pb.clicked.connect(self.myClick)
    
    def ranCom(self):
        self.com = int(random() * 99) + 1
        print(self.com)
    
    #btn이 눌리면 작동할 함수
    def myClick(self) :
        le_text = self.le.text()
        le_num = int(le_text)
        if le_num > self.com : 
            self.te.append(le_text + "\t[Down↓]\n")
        elif le_num < self.com : 
            self.te.append(le_text + "\t[UP↑]\n")
        else :
            self.te.append(le_text + "\t[★정답★]\n")
            QMessageBox.about(self,'UP&DOWN', le_text + "\t[★정답★]\n")
        
# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
