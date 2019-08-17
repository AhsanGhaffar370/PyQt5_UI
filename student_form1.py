from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import datetime
import calendar
import re


def show_info():

    id1 = call.id_spin.value()
    name = call.name_txt.text()
    age = call.age_spin.value()
    gender = male_female()
    dob = str(call.dob_cal.selectedDate())
    from_time = "FROM: "+ call.from_time.text()
    to_time = " | TO: "+ call.to_time.text()
    diff_time = time_diff(call.from_time.text(), call.to_time.text())
    Class = call.class_co.currentText()
    selected1 = selected_course()

    if Class == "SelectClass" or not selected1 or name == "" or gender == "empty":
        war_msg("Warning", "Please fill out all fields correctly as per given instructions below")
    else:
        if validations(name, diff_time, age, selected1):

            add_item(id1, name, dob, age, gender, from_time, to_time, diff_time, Class,selected1)

            call.id_spin.setValue(id1+1)


def validations(name1,diff_time, age, selected1):

    comp = re.compile(r"^[a-zA-Z\s]{3,}$")

    if comp.search(name1) is None:
        war_msg("Warning", "Format of Name is not compatible (Use only alphabets)")

    if diff_time < 2:
        war_msg("Warning", "The Minimum Time span should have been 2 hours")

    if age < 10:
        war_msg("Warning", "Minimum required age for admission is 10 years")

    if len(selected1) < 2:
        war_msg("Warning", "Select at least two subjects")

    if comp.search(name1) is None or diff_time < 2 or age < 10 or len(selected1) < 2:
        return False
    else:
        return True


def selected_course():
    selected = []
    if call.sci_ck.isChecked():
        selected.append("Science")
    if call.urdu_ck.isChecked():
        selected.append("Urdu")
    if call.phy_ck.isChecked():
        selected.append("Physics")
    if call.math_ck.isChecked():
        selected.append("Math")
    if call.eng_ck.isChecked():
        selected.append("English")
    if call.isl_ck.isChecked():
        selected.append("Islamiat")

    return selected


def male_female():

    if call.gm_rb.isChecked(): #we can also set the radio button to checked or not by default  call.gm_rb.setChecked(True):
         return call.gm_rb.text()
    elif call.gf_rb.isChecked():
         return call.gf_rb.text()
    else:
        return "empty"


def time_diff(From, to):
    from_index = From.find(":")
    to_index = to.find(":")

    to_t=int(to[0:to_index])
    from_t=int(From[0:from_index])

    if to_t == 12:
        to_t = 0
    if from_t == 12:
        from_t = 0

    diff = to_t - from_t

    return diff


def add_item(id1, name, dob, age, gender, from_time, to_time, diff_time, Class,selected1):
    call.stu_info.addItem("************************************")

    call.stu_info.addItem("Click coaching:\n")
    call.stu_info.addItem("Student ID: " + str(id1))
    call.stu_info.addItem("Student name: " + name)
    call.stu_info.addItem("Student Date Of Birth: " + dob)
    call.stu_info.addItem("Student age: " + str(age) + " years")
    call.stu_info.addItem("Student gender: " + gender)
    call.stu_info.addItem("TIMING: " + from_time + to_time)
    call.stu_info.addItem("Total Hours: " + str(diff_time)+ " Hours")
    call.stu_info.addItem("Student Class: " + Class)

    count = 1
    for i in selected1:
        call.stu_info.addItem(f"Subject{count}: {i}")
        count += 1

    call.stu_info.addItem("************************************\n")
    print(name + " Successfully added")


def war_msg(title="info",msg="Something went wrong!"):
    QMessageBox.information(None,title,msg)


app=QtWidgets.QApplication([])
call=uic.loadUi("student_form.ui")

call.submit_btn.clicked.connect(show_info)

call.show()
app.exec()