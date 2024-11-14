import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGrometry(0, 0, 500, 100)
        label.setStyleSheet("colour: blue;"
                            "background-colour: pink;"
                            "font-weight: bold;"
                            "font-style: ltalic;"
                            "text-decoreation: underline;")
        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) # vertically bottom
        # label.setAlignment(Qt.AlignVcenter) # vertically center

        # label.setAlignment(Qt.AlignRight) # horizontally right
        # label.setAlignment(Qt.AlignHcenter) # horizontally center
        # label.setAlignment(Qt.AlignLeft) # horizontally left

        # label.setAlignment(Qt.AlignHcenter | Qt.AlignTop) # center & top
        # label.setAlignment(Qt.AlignHcenter | Qt.AlignBottom) # center & bottom
        # label.setAlignment(Qt.AlignHcenter | Qt.AlignVcenter) # center & center
        label.setAlignment(Qt.AlignCenter) # center & center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()