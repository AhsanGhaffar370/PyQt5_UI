from PyQt5 import QtWidgets, uic

def show_info():

    id1=call.id_spin.text()

    name=call.name_txt.text()

    if name=="ahsan":
        name+=" T"
    else:
        name+=" F"

    age=call.age_spin.text()

    # show_list.additem(name)

    # if gm_rb.checked( ) == True :
    #     gender = call.gm_rb.text( )
    #
    # elif gf_rb.checked( ) == True :
    #     gender = call.gf_rb.text( )

    # clas = call.class_co.text()

    #from = "FROM: "+ call.from_time.text()
    #to = "TO: "+ call.to_time.text()
    call.stu_info.addItem("************************************")
    call.stu_info.addItem("Click coatchings:\n")
    call.stu_info.addItem("Student ID: "+id1)
    call.stu_info.addItem("Student name: "+name)
    call.stu_info.addItem("Student age: "+age)
    #print("Student gender: "+gender)
    call.stu_info.addItem("************************************\n")
    print(name+"Successfully added")


app=QtWidgets.QApplication([])
call=uic.loadUi("student_form1.ui")

call.submit_btn.clicked.connect(show_info)

call.show()
app.exec()


