from PyQt5.QtWidgets import *
import sys

class Window(QWidget) :
    def __init__(self) :
        QWidget.__init__(self)

        layout = QGridLayout( )
        self.setLayout(layout)

        self.checkbox1 = QCheckBox("Mango")
        self.checkbox1.setChecked(True)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)

        print(self.checkbox1.text() )

        self.checkbox2 = QCheckBox("Apple")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 0)

        self.checkbox3 = QCheckBox("Banana")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)

        self.checkbox4 = QCheckBox("More Options")
        self.checkbox4.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox4, 3, 0)

        # self.checkbox2.setTristate(True)
        # print(self.checkbox2.isTristate())
        # print(self.checkbox2.checkState())
        # self.checkbox3.setCheckState(0)


    def checkbox_toggled(self):
        selected = []
        if self.checkbox4.isChecked( ) :
            self.checkbox1.setText("Grapes")
            self.checkbox1.setEnabled(False)
            self.checkbox1.setCheckState(0)
            self.checkbox2.setText("Chiku")
            self.checkbox3.setText("Orange")
        else:
            self.checkbox1.setText("Mango")
            self.checkbox1.setEnabled(True)
            self.checkbox2.setText("Apple")
            self.checkbox3.setText("Banana")
        if self.checkbox1.isChecked():
            selected.append(self.checkbox1.text())
        if self.checkbox2.isChecked():
            selected.append(self.checkbox2.text())
        if self.checkbox3.isChecked():
            selected.append(self.checkbox3.text())

        print("Selected:%s" % (" ".join(selected)))


app = QApplication(sys.argv)
screen = Window( )


screen.show( )
sys.exit(app.exec_( ))