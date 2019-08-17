from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self) :
        QWidget.__init__(self)
        layout = QGridLayout( )
        self.setLayout(layout)

        # simple spin box
        # self.spinbox = QSpinBox()
        # self.spinbox.setValue(5)
        # self.spinbox.setRange(1, 20)
        # self.spinbox.setSuffix(" mph")
        # self.spinbox.setSingleStep(3)

        # Double spin box
        self.doublespinbox = QDoubleSpinBox( )
        self.doublespinbox.setValue(5)
        self.doublespinbox.setRange(1, 20)
        self.doublespinbox.setSuffix(" mph")
        self.doublespinbox.setSingleStep(0.5) # it is only possible in double spin box

        layout.addWidget(self.doublespinbox, 0, 0)

app = QApplication(sys.argv)
screen = Window( )
screen.show( )
sys.exit(app.exec_( ))