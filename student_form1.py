from PyQt5 import QtWidgets, uic

def show_info():

    id1=call.id_spin.text()
    name=call.name_txt.text()
    age=call.age_spin.text()
    from_time = "FROM: "+ call.from_time.text()
    to_time = " | TO: "+ call.to_time.text()

    if call.gm_rb.isChecked(): #we can also set the radio button to checked or not by default  call.gm_rb.setChecked(True):
         gender = call.gm_rb.text()
    elif call.gf_rb.isChecked():
         gender = call.gf_rb.text()
    else:
        gender="TransGender"

    count=1
    selected=[]
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

    # Class = call.class_co.text()

    call.stu_info.addItem("************************************")
    call.stu_info.addItem("Click coatchings:\n")
    call.stu_info.addItem("Student ID: "+id1)
    call.stu_info.addItem("Student name: "+name)
    call.stu_info.addItem("Student age: "+age)
    call.stu_info.addItem("Student gender: "+gender)
    call.stu_info.addItem("TIMING: " + from_time+to_time)
    for i in selected:
        call.stu_info.addItem(f"Subject{count}: {i}")
        count+=1
    # call.stu_info.addItem("Student Class: " + Class)
    call.stu_info.addItem("************************************\n")
    print(name+" Successfully added")


app=QtWidgets.QApplication([])
call=uic.loadUi("student_form.ui")

call.submit_btn.clicked.connect(show_info)

call.show()
app.exec()


