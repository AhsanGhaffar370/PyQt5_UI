from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import calendar

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        min1 = QTime( )
        min1.setHMS(13, 0, 40)

        max1 = QTime( )
        max1.setHMS(18, 0, 40)

        self.timeedit1 = QTimeEdit()
        # timeedit1.setTime(min1)

        self.timeedit2 = QTimeEdit()

        self.timeedit1.setMinimumTime(min1)
        self.timeedit1.setMaximumTime(max1)

        self.timeedit2.setMinimumTime(min1)
        self.timeedit2.setMaximumTime(max1)

        self.timeedit2.timeChanged.connect(self.click)


        layout.addWidget(self.timeedit1, 0, 0)
        layout.addWidget(self.timeedit2, 0, 1)

    def click(self):

        aft1 = self.timeedit1.text( )
        aft2=self.timeedit2.text()
        after2=aft2[1:]

        before1=int(aft1[0])
        before2 = int(aft2[0])
        diff=str(before2-before1)+" Hour"

        if after2.find("PM")!=-1:
            diff+=" Evening"
        else:
            diff+=" Morning"

        if self.timeedit2.time() > self.timeedit1.time():
            print("time saved: "+diff)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())