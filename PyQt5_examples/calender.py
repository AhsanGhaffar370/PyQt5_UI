from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import calendar

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.calendar = QCalendarWidget()

        self.calendar.selectionChanged.connect(self.on_click)

        self.calendar.clicked[QDate].connect(self.showDate)

        layout.addWidget(self.calendar)

    def showDate(self,date):
        print(date.toString( ))

    def on_click(self):

        print(self.calendar.showToday())
        print(self.calendar.showSelectedDate( ))
        print(self.calendar.showNextMonth( ))
        print(self.calendar.showNextYear( ))
        print(self.calendar.showPreviousMonth( ))
        print(self.calendar.showPreviousYear( ))
        print(self.calendar.selectedDate( ))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())