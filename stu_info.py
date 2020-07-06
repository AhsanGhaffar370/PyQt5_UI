from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

def show_info():
    id1=call.id_spin.text()
    name=call.name_txt.text()
    age=call.age_txt.text()

    if name!="" and age!="" and id1!="":
        call.info_lw.addItem("*********************")
        call.info_lw.addItem("Student ID: "+id1)
        call.info_lw.addItem("Student name: "+name)
        call.info_lw.addItem("Student age: "+age)
        call.info_lw.addItem("*********************\n")
        print(name+"Successfully added")
        clear_text()
    else:
        QMessageBox.information(None, "Warning", "Please enter some value")

def clear_text():
    call.name_txt.clear()
    call.age_txt.clear()
    call.id_spin.clear()

app=QtWidgets.QApplication([])
call=uic.loadUi("stu_info.ui")

call.save_btn.clicked.connect(show_info)
call.clear_btn.clicked.connect(clear_text)

call.show()
app.exec()