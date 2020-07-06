from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

def recall_data():
    with open("us_val.txt", "r",newline="") as u1 :
        rr=u1.readlines()
        for  i in rr:
            ccall.history_lw.addItem(i)

def maintain_history(us_val):
    if not us_val=="":
        ccall.history_lw.addItem(us_val)
        ccall.euro.clear()


def show_msg(title="info",msg="Something went wrong!"):
    QMessageBox.information(None,title,msg)

def convert1():
    if not ccall.euro.text() == "" :
        ccall.us.setText(str(float(ccall.euro.text()) * 1.23))
        with open("us_val.txt","a") as u:
            u.write(ccall.us.text()+"\n")
        maintain_history(ccall.us.text())
    else:
        # QMessageBox.information(None,"Warning", "Please enter some value")
        show_msg("Warning!", "Please enter some value for conversion:")

app=QtWidgets.QApplication([])
ccall=uic.loadUi("converter.ui")

recall_data()

ccall.euro.setFocus()
# ccall.euro.setPaceholderText("Euros")
# ccall.us.setReadOnly(True)
ccall.convert_btn.clicked.connect(convert1)
# ccall.euro.returnPressed.connect(convert(ccall.euro.text()))

ccall.show()
app.exec()
