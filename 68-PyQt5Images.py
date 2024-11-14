import sys
from PyQt5.Qtwidgets import QApplication, QMainWindow, QLable
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWidonwTitle("my cool first GUI")
        self.setGeometry(0, 0, 500, 500)
        
        label = QLable(self):
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("pic.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                         (self.height() - label.height()) // 2, 
                         label.width(), 
                         label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()