from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def onClick1():
    call.frame2.hide()
    call.frame3.hide()
    call.frame1.show()

def onClick2():
    # call.frame1.hide()


    call.frame3.hide()
    call.frame2.show()

def onClick3():
    # call.frame1.hide()
    # call.frame2.hide()


    call.frame3.show()


app=QtWidgets.QApplication([])
call=uic.loadUi("frame_changing.ui")

call.b1.clicked.connect(onClick1)
call.b2.clicked.connect(onClick2)
call.b3.clicked.connect(onClick3)

call.show()
app.exec()