import sys
from PyQt5.QtWidegets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatebase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("digital clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidet(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.Aligncenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "colour: #26ff00;")
        self.setStyleSheet("background-colour: black;")
        
        font_id = QFontDatebase.addApplication("ds.ttf")
        font_family = QFontDatebase.applicationFontFamilyes(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())