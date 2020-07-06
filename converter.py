from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

#create a convert function which convert euros to us dollars a also saves data in us_val file
def convert1():
    if not ccall.euro.text() == "" :
        ccall.us.setText(str(float(ccall.euro.text()) * 1.23))
        with open("us_val.txt","a") as u:
            u.write(ccall.us.text()+"\n")
        maintain_history(ccall.us.text())
    else:
        show_msg("Warning!", "Please enter some value for conversion:")

# this function reads data from from file and add it in list_Widget
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



app=QtWidgets.QApplication([])
ccall=uic.loadUi("converter.ui")

recall_data()
ccall.convert_btn.clicked.connect(convert1)

ccall.show()
app.exec()
