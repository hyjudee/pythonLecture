import sys
from PyQt5.Qtwidgets import (QApplication, QMainWindow, QLable,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.initUI()

        def initUI(self):
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            label1 = QLable("#1, self")
            label2 = QLable("#2, self")
            label3 = QLable("#3, self")
            label4 = QLable("#4, self")
            label5 = QLable("#5, self")

            label1.setStyleSheet("background-colour: red;")
            label2.setStyleSheet("background-colour: yellow;")
            label3.setStyleSheet("background-colour: green;")
            label4.setStyleSheet("background-colour: blue;")
            label5.setStyleSheet("background-colour: pink;")

            vbox = QVBoxLayout()

            vbox.addWidget(label1, 0, 0)
            vbox.addWidget(label2, 0, 1)
            vbox.addWidget(label3, 1, 0)
            vbox.addWidget(label4, 1, 1)
            vbox.addWidget(label5, 1, 2)

            central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()