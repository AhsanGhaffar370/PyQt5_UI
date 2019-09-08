from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
####################################################
def zero_disp():
    nums=call.disp_lb.text()+"0"
    call.disp_lb.setText(nums)

def one_disp():
    if equal_flag == True:
        call.disp_lb.clear()
        call.fdisp_lb.clear()
        equal_flag= False
    
    nums=call.disp_lb.text()+"1"
    call.disp_lb.setText(nums)

def add_oper():
    # oper=call.fdisp.text()+call.disp.text()+" + "
    oper=call.disp_lb.text()+" + "
    call.fdisp_lb.setText(oper)
    call.disp_lb.clear()

def equals_oper():
    oper = call.fdisp_lb.text()+call.disp_lb.text()
    call.fdisp_lb.setText(oper)
    val=call.fdisp_lb.text()
    nums=[]

    nums=val.split()

    if nums[1] == "+":
        ans = float(nums[0]) + float(nums[2])
    else:
        ans="undefined equation"

    call.disp_lb.setText(str(ans))

    equal_flag = True
    # call.ans_lb.setText("answer")

####################################################
app=QtWidgets.QApplication([])
call=uic.loadUi("simpleCaculator.ui")
####################################################
equal_flag=False


call.zero_btn.clicked.connect(zero_disp)
call.one_btn.clicked.connect(one_disp)

call.add_btn.clicked.connect(add_oper)

call.equals_btn.clicked.connect(equals_oper)

####################################################
call.show()
app.exec()
