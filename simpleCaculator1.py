from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
####################################################

def ret():
    one=call.one_btn.text()
    two=call.two_btn.text()
    three=call.three_btn.text()
    four=call.four_btn.text()
    five=call.five_btn.text()
    six=call.six_btn.text()
    seven=call.seven_btn.text()
    eight=call.eight_btn.text()
    nine=call.nine_btn.text()
    zero=call.zero_btn.text()

    nums=[zero,one,two,three,four,five,six,seven,eight,nine]

    return nums


def clear_ans():
    if call.ans_lb.text() == "answer":
        cler()

def zero_disp():
    clear_ans()
    nums=call.disp_lb.text()+"0"
    call.disp_lb.setText(nums)

def one_disp():
    clear_ans()
    nums=call.disp_lb.text()+"1"
    call.disp_lb.setText(nums)

def two_disp():
    clear_ans()
    nums=call.disp_lb.text()+"2"
    call.disp_lb.setText(nums)

def three_disp():
    clear_ans()
    nums=call.disp_lb.text()+"3"
    call.disp_lb.setText(nums)

def four_disp():
    clear_ans()
    nums=call.disp_lb.text()+"4"
    call.disp_lb.setText(nums)

def five_disp():
    clear_ans()
    nums=call.disp_lb.text()+"5"
    call.disp_lb.setText(nums)

def six_disp():
    clear_ans()
    nums=call.disp_lb.text()+"6"
    call.disp_lb.setText(nums)

def seven_disp():
    clear_ans()
    nums=call.disp_lb.text()+"7"
    call.disp_lb.setText(nums)

def eight_disp():
    clear_ans()
    nums=call.disp_lb.text()+"8"
    call.disp_lb.setText(nums)

def nine_disp():
    clear_ans()
    nums=call.disp_lb.text()+"9"
    call.disp_lb.setText(nums)

def dot_disp():
    clear_ans()
    if call.disp_lb.text().find(".") == -1:
        nums=call.disp_lb.text()+"."
    else:
        nums=call.disp_lb.text()

    call.disp_lb.setText(nums)

def add_oper():
    # oper=call.fdisp.text()+call.disp.text()+" + "
    oper=call.disp_lb.text()+" + "
    call.fdisp_lb.setText(oper)
    call.disp_lb.clear()

def sub_oper():
    oper=call.disp_lb.text()+" - "
    call.fdisp_lb.setText(oper)
    call.disp_lb.clear()

def mul_oper():
    oper=call.disp_lb.text()+" x "
    call.fdisp_lb.setText(oper)
    call.disp_lb.clear()

def div_oper():
    oper=call.disp_lb.text()+" / "
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
    elif nums[1] == "-":
        ans = float(nums[0]) - float(nums[2])
    elif nums[1] == "x":
        ans = float(nums[0]) * float(nums[2])
    elif nums[1] == "/":
        ans = float(nums[0]) / float(nums[2])

    call.disp_lb.setText(str(ans))

    # equal_flag= True
    call.ans_lb.setText("answer")

def cler():
    call.disp_lb.clear()
    call.fdisp_lb.clear()
    call.ans_lb.clear()

def clear_once():
    disp=call.disp_lb.text()

    if len(disp) < 1:
        call.disp_lb.clear()
    else:
        call.disp_lb.setText(disp[0:-1])

####################################################
app=QtWidgets.QApplication([])
call=uic.loadUi("simpleCaculator.ui")
####################################################

ret()
call.zero_btn.clicked.connect(zero_disp)
call.one_btn.clicked.connect(one_disp)
call.two_btn.clicked.connect(two_disp)
call.three_btn.clicked.connect(three_disp)
call.four_btn.clicked.connect(four_disp)
call.five_btn.clicked.connect(five_disp)
call.six_btn.clicked.connect(six_disp)
call.seven_btn.clicked.connect(seven_disp)
call.eight_btn.clicked.connect(eight_disp)
call.nine_btn.clicked.connect(nine_disp)
call.dot_btn.clicked.connect(dot_disp)

call.add_btn.clicked.connect(add_oper)
call.sub_btn.clicked.connect(sub_oper)
call.mul_btn.clicked.connect(mul_oper)
call.div_btn.clicked.connect(div_oper)

call.equals_btn.clicked.connect(equals_oper)

call.clear_btn.clicked.connect(cler)

call.cancel_btn.clicked.connect(clear_once)

call.hclear_btn.clicked.connect(lambda : call.disp_lb.clear())
####################################################
call.show()
app.exec()