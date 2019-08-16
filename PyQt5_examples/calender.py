from PyQt5.QtWidgets import *
import sys
import calendar

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.calendar = QCalendarWidget()

        self.calendar.selectionChanged.connect(self.on_click)

        layout.addWidget(self.calendar)

    def on_click(self):
        print(self.calendar.showToday( ))
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