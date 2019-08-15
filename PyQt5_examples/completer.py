from PyQt5.QtWidgets import *
import sys

class Window(QWidget) :
    def __init__(self) :
        QWidget.__init__(self)
        layout = QGridLayout( )
        self.setLayout(layout)

        names = ["ahsan","ali","Faraz","osama"]

        completer1 = QCompleter(names)

        # completer1.setMaxVisibleItems(1)
        # completer1.setCaseSensitivity(False)

        self.lineedit = QLineEdit( )
        self.lineedit.setCompleter(completer1)
        layout.addWidget(self.lineedit, 0, 0)


app = QApplication(sys.argv)
screen = Window( )
screen.show( )
sys.exit(app.exec_( ))