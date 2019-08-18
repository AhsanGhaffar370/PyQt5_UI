from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import datetime
import calendar
import re


def gather_info():
    """
    In this function we take information from form and saves it in a listWidget.
    But before save information from form to list we also validate the form.
    """
    ID = call.id_spin.value()
    name = call.name_txt.text()
    age = call.age_spin.value()
    gender = Gender()
    DOB = str(setDate_format())
    from_time = call.from_time.text()
    to_time = call.to_time.text()
    diff_time = time_diff(call.from_time.text(), call.to_time.text())
    Class = call.class_co.currentText()

    if Class == "SelectClass" or not selected_subjects() or name == "" or gender == "empty":

        warning_msg("Warning", "Please fill out all fields correctly as per given instructions below")
    else:
        if validations(name, diff_time, age, selected_subjects()):

            add_item(ID, name, DOB, age, gender, from_time, to_time, diff_time, Class, selected_subjects())

            clearAll()


def recallData_setCompleter():
    names = []
    with open("names.txt", "r") as r:
        rr = r.readlines()
        for i in rr:
            pos = i.find("\\")
            names.append(i[0:pos])

    completer1 = QCompleter(names)
    completer1.setCaseSensitivity(False)
    call.name_txt.setCompleter(completer1)

    return names


def save_name():
    n = recallData_setCompleter( )
    b = True
    for i in n :
        if i.find(call.name_txt.text()) != -1:
            b = False
            break

    if b is True:
        with open("names.txt", "a") as w :
            w.write(call.name_txt.text() + "\n")
        recallData_setCompleter( )


def Gender():
    """
    This funciton returns the value of male or female radioButton.
    Only the value of checked radio button will be return otherwise it retruns empty
    """
    if call.male_rb.isChecked(): #we can also set the radio button to checked or not by default  call.male_rb.setChecked(True):
         return call.male_rb.text()
    elif call.female_rb.isChecked():
         return call.female_rb.text()
    else:
        return "empty"


def setDate_format():
    d=call.dob_cal.selectedDate().day()
    m = call.dob_cal.selectedDate().month()
    y = call.dob_cal.selectedDate().year()

    date1=datetime.datetime(y,m,d)

    return date1.strftime("%d %b, %Y")


def time_diff(from_time, to_time):
    from_index = from_time.find(":")
    to_index = to_time.find(":")

    to_t=int(to_time[0:to_index])
    from_t=int(from_time[0:from_index])

    if to_t == 12:
        to_t = 0
    if from_t == 12:
        from_t = 0

    diff_t = to_t - from_t

    return diff_t

def selectClass_setSubjects():

    clas = call.class_co.currentText()

    if clas == "SelectClass":
        disable_subjects()
    else:
        unchecked_subjects()
        enable_subjects()

    if clas == "9th":
        call.one_ck.setText("Biology")
        call.two_ck.setText("Islamiat")
        call.three_ck.setText("English")
        call.four_ck.setText("---")
        call.four_ck.setCheckState(0)
        call.four_ck.setEnabled(False)

    if clas == "10th":
        call.one_ck.setText("Physics")
        call.two_ck.setText("Urdu")
        call.three_ck.setText("Chemistry")
        call.four_ck.setText("Math")


def disable_subjects():
    call.one_ck.setText("---")
    call.two_ck.setText("---")
    call.three_ck.setText("---")
    call.four_ck.setText("---")

    call.one_ck.setEnabled(False)
    call.two_ck.setEnabled(False)
    call.three_ck.setEnabled(False)
    call.four_ck.setEnabled(False)

    unchecked_subjects()

def enable_subjects():
    call.one_ck.setEnabled(True)
    call.two_ck.setEnabled(True)
    call.three_ck.setEnabled(True)
    call.four_ck.setEnabled(True)

def unchecked_subjects():
    call.one_ck.setCheckState(0)
    call.two_ck.setCheckState(0)
    call.three_ck.setCheckState(0)
    call.four_ck.setCheckState(0)


def selected_subjects():
    selected = []
    if call.one_ck.isChecked():
        selected.append(call.one_ck.text())
    if call.two_ck.isChecked():
        selected.append(call.two_ck.text())
    if call.three_ck.isChecked():
        selected.append(call.three_ck.text())
    if call.four_ck.isChecked():
        selected.append(call.four_ck.text())

    return selected


def add_item(ID, name, DOB, age, gender, from_time, to_time, diff_time, Class, selected1):

    call.stu_info.clear()
    call.stu_info.addItem("************************************")
    call.stu_info.addItem("Student ID: " + str(ID))
    call.stu_info.addItem("Student name: " + name)
    call.stu_info.addItem("Student Date Of Birth: " + DOB)
    call.stu_info.addItem("Student age: " + str(age) + " years")
    call.stu_info.addItem("Student gender: " + gender)
    call.stu_info.addItem("TIMING: " + from_time + " to " + to_time)
    call.stu_info.addItem("Total Hours: " + str(diff_time)+ " Hours")
    call.stu_info.addItem("Student Class: " + Class)

    count = 1
    for i in selected1:
        call.stu_info.addItem(f"Subject{count}: {i}")
        count += 1

    call.stu_info.addItem("************************************\n")

    count = call.stu_info.count()
    with open("stu_info.txt", "a") as w :
        for i in range(count):
            call.stu_info.setCurrentRow(i)
            item=call.stu_info.currentItem()
            w.write(item.text()+"\n")

    save_name()


def validations(name1,diff_time, age, selected1):

    comp = re.compile(r"^[a-zA-Z\s]{3,}$")

    if comp.search(name1) is None:
        warning_msg("Warning", "Format of Name is not compatible (Use only alphabets)")

    elif age < 10:
        warning_msg("Warning", "Minimum required age for admission is 10 years")

    elif diff_time < 2:
        warning_msg("Warning", "The Minimum Time span should have been 2 hours")

    elif len(selected1) < 2:
        warning_msg("Warning", "Select at least two subjects")

    if comp.search(name1) is None or diff_time < 2 or age < 10 or len(selected1) < 2:
        return False
    else:
        return True


def warning_msg(title="info",msg="Something went wrong!"):
    QMessageBox.information(None,title,msg)


def clearAll():
    call.name_txt.setText("")

    call.age_spin.setValue(10)

    call.male_rb.setAutoExclusive(False)
    call.female_rb.setAutoExclusive(False)
    call.male_rb.setChecked(False)
    call.female_rb.setChecked(False)
    call.male_rb.setAutoExclusive(True)
    call.female_rb.setAutoExclusive(True)

    call.dob_cal.setCurrentPage(2009, 12)

    time = QTime()
    time.setHMS(12, 00, 00)
    call.from_time.setTime(time)
    time.setHMS(14,00,00)
    call.to_time.setTime(time)

    call.class_co.setCurrentText("SelectClass")

    disable_subjects()

def save_info():

    if call.stu_info.count() ==0:
        warning_msg("Information", "Nothing to save")
    else:
        print("Student Successfully added")
        call.id_spin.setValue(call.id_spin.value() + 1)
        call.stu_info.clear()
        warning_msg("Information","Form Submitted Successfully")


def discard():
    if call.stu_info.count() ==0:
        warning_msg("Information", "Nothing to Discard")
    else:
        call.stu_info.clear()
        warning_msg("Information","Form Discarded!")

app=QtWidgets.QApplication([])
call=uic.loadUi("student_form.ui")

recallData_setCompleter()
# print(Gender.__doc__)
call.class_co.currentTextChanged.connect(selectClass_setSubjects)
call.submit_btn.clicked.connect(gather_info)
call.clear_btn.clicked.connect(clearAll)
call.save_btn.clicked.connect(save_info)
call.discard_btn.clicked.connect(discard)

call.show()
app.exec()