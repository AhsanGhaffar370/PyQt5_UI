from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.buttongroup1 = QButtonGroup()
        # self.buttongroup1.setExclusive(True)
        self.buttongroup1.buttonClicked[int].connect(self.on_radio_clicked)

        radiobutton = QRadioButton("Brazil")
        layout.addWidget(radiobutton, 0, 0)
        self.buttongroup1.addButton(radiobutton,1)
        radiobutton = QRadioButton("israel")
        layout.addWidget(radiobutton, 0, 1)
        self.buttongroup1.addButton(radiobutton, 2)

        self.buttongroup2 = QButtonGroup()
        self.buttongroup2.buttonClicked[int].connect(self.on_radio_clicked)

        radiobutton = QRadioButton("pakistan")
        layout.addWidget(radiobutton, 1, 0)
        self.buttongroup2.addButton(radiobutton, 3)
        radiobutton = QRadioButton("palestine")
        layout.addWidget(radiobutton, 1, 1)
        self.buttongroup2.addButton(radiobutton, 4)

        #
        # button1 = QPushButton("Button 1")
        # self.buttongroup.addButton(button1, 1)
        # layout.addWidget(button1)
        #
        # button2 = QPushButton("Button 2")
        # self.buttongroup.addButton(button2, 2)
        # layout.addWidget(button2)
    def on_radio_clicked(self, id1):
        for button1 in self.buttongroup1.buttons():
            if button1 is self.buttongroup1.button(id1):
                print(f"ButtonGroup1 {button1.text( )} was clicked!")

        for button2 in self.buttongroup2.buttons():
            if button2 is self.buttongroup2.button(id1):
                print(f"ButtonGroup2 {button2.text( )} was clicked!")


sizegrip = QSizeGrip(QRadioButton)
sizegrip.setVisible(False)



app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

# from PyQt5.QtWidgets import *
# import sys
# class Window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout( )
#         self.setLayout(layout)
#
#
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())
