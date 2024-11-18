import sys
from PyQt5.Qtwidgets import (QApplication, QMainWindow, 
                             QPushButton, QWidget, QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setcentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 20px 75px;
                margin: 25px;
                border: 2px solid;
                border-radius: 5px;
            }
            QPushButton#button1{
                background-colour: rgb(255, 71, 71);
            }
            QPushButton#button2{
                background-colour: pink;
            }
            QPushButton#button3{
                background-colour: hsl(122, 100%, 64%);
            }
            QPushButton#button1:hover{
                background-colour: rgb(255, 81, 81);
            }
            QPushButton#button2:hover{
                background-colour: gray;
            }
            QPushButton#button3:hover{
                background-colour: hsl(122, 100%, 84%);
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    