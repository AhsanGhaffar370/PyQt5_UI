from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os

def show1():

    user= call.user.text()
    pass1= call.pass1.text()

    if(user=="ahsan" and pass1=="12345"):
        call.hide()
        import mini_os
    else:
        call.user.setText("")
        call.pass1.setText("")
        QMessageBox.information(None,"Error","Invalid Username or Password") 


app=QtWidgets.QApplication([])
call=uic.loadUi("login.ui")

call.login.clicked.connect(show1)

call.show()
app.exec_()
