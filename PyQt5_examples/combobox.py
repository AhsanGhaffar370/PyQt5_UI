from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        list1=["grapes","chiku"]
        self.combobox = QComboBox()

        self.combobox.addItem("apple")
        self.combobox.addItems(list1)
        self.combobox.insertItem(0,"orange")
        self.combobox.insertItems(1,list1)

        self.combobox.insertSeparator(2)

        self.combobox.setCurrentText("grapes")
        # self.combobox.setDuplicatesEnabled(False)

        self.combobox.currentTextChanged.connect(self.combobox_changed)
        layout.addWidget(self.combobox)

    def combobox_changed(self):
        text = self.combobox.currentText()
        index=  self.combobox.currentIndex()
        print(index,text)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())