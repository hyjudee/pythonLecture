import sys
from PyQt5.QtWidgets import QApplication, QMainwindow, QRadioButton, QButtonGroup

class MainWindow(QMainwindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("mastercard", self)
        self.radio3 = QRadioButton("gift card", self)
        self.radio4 = QRadioButton("in-store", self)
        self.radio5 = QRadioButton("online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial;"
                           "padding: 10px:"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)

    def radio_button_change(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())