from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.radiobutton1 = QRadioButton("Brazil")
        self.radiobutton1.setChecked(True)
        # self.radiobutton1.toggled.connect(self.on_radio_button_toggled)
        self.radiobutton1.clicked.connect(self.on_radio_button_toggled)
        layout.addWidget(self.radiobutton1, 0, 0)

        self.radiobutton2 = QRadioButton("Argentina")
        self.radiobutton2.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(self.radiobutton2, 0, 1)

        self.radiobutton3 = QRadioButton("Ecuador")
        self.radiobutton3.toggled.connect(self.on_radio_button_toggled)
        layout.addWidget(self.radiobutton3, 0, 2)

        self.button1=QPushButton("unchecked all")
        layout.addWidget(self.button1,1,0)
        self.button1.clicked.connect(self.uncheck)

    def on_radio_button_toggled(self):
        if self.radiobutton1.isChecked():
            print("Selected country is " + self.radiobutton1.text())
        if self.radiobutton2.isChecked():
            print("Selected country is " + self.radiobutton2.text())
        if self.radiobutton3.isChecked():
            print("Selected country is " + self.radiobutton3.text())

    def uncheck(self):
        self.radiobutton1.setAutoExclusive(False)
        self.radiobutton2.setAutoExclusive(False)
        self.radiobutton3.setAutoExclusive(False)

        self.radiobutton1.setChecked(False)
        self.radiobutton2.setChecked(False)
        self.radiobutton3.setChecked(False)

        self.radiobutton1.setAutoExclusive(True)
        self.radiobutton2.setAutoExclusive(True)
        self.radiobutton3.setAutoExclusive(True)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())