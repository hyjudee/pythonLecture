import sys
from PyQt5.Qtwidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWidonwTitle("my cool first GUI")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon("pic.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



