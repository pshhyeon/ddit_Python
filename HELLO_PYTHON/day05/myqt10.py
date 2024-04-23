import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# ui파일 불러오기
form_class = uic.loadUiType("myqt10.ui")[0]

# 윈도우 클래스 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.str = ""
        self.pb.clicked.connect(self.myClick)
    
    def printStar(self, n):
        for i in range(n) :
            self.str += "★"
        self.str += "\n" 
    
    def myClick(self) :
        sNum = int(self.le_first.text())
        eNum = int(self.le_last.text())
        for i in range(sNum,eNum+1) : 
            self.printStar(i)
        self.pte.setPlainText(self.str)
        self.str = ""

# 메인 선언
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
