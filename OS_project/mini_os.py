from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime
import os
from zipfile import ZipFile
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt




def show_frame0():
    call.m1_frame.hide() 
    call.m2_frame.hide() 
    call.m3_frame.hide()  
    call.m4_frame.hide() 
    call.m5_frame.hide() 
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m0_frame.show()

def show_frame1():

    call.m2_frame.hide() 
    call.m3_frame.hide()  
    call.m4_frame.hide() 
    call.m5_frame.hide() 
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m1_frame.show()


def show_frame2(): 
    call.m3_frame.hide()  
    call.m4_frame.hide() 
    call.m5_frame.hide() 
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m2_frame.show()


def show_frame3():  
    call.m4_frame.hide() 
    call.m5_frame.hide() 
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m3_frame.show()

def show_frame4():  
    call.m5_frame.hide() 
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m4_frame.show()

def show_frame5():   
    call.m6_frame.hide()  
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m5_frame.show()

def show_frame6():    
    call.m7_frame.hide() 
    call.m8_frame.hide()   
    call.m6_frame.show()

def show_frame7():  
    call.m8_frame.hide()   
    call.m7_frame.show()

def show_frame8():    
    call.m8_frame.show()



# def createFile():
# 	f=open("/home/noman/Downloads/putting.txt","w+")
# 	print("Created File Successfully!")
# createFile()


#########################################
############ File Module ##############
#####################################
def File_modules():
    """
    This funciton returns the value of selected radioButton.
    Only the value of checked radio button will be return otherwise it retruns empty
    """
    #we can also set the radio button to checked or not by default call.create_f.setChecked(True):

    file_name=call.f_name.text()
    file_path=call.f_path.text()

    if (file_name=="" or file_path==""):
        msg_box("Warning", "Please fill out file all field")

    else:
        if call.feat1_m1_rb.isChecked():        ###### create File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    msg_box("Error", "File {0} already Exist".format(file_name))
                else:
                    f=open(fn,"w+")

                    print("\n\n****************")
                    print(file_name+" file created")
                    print("****************\n\n")
                    msg_box("Information", "File "+file_name+" Successfully created")
                
            except Exception as e:
                msg_box("Error", str(e))


        elif call.feat2_m1_rb.isChecked():        ###### Delete File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    os.remove(fn)

                    print("\n\n****************")
                    print(file_name+" file deleted")
                    print("****************\n\n")
                    msg_box("Information", "File "+file_name+" Delete Successfully")
                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
                
            except Exception as e:
                msg_box("Error", str(e))


        elif call.feat3_m1_rb.isChecked():        ###### Read File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    f=open(fn,"r+")
                    contents=f.read()

                    print("\n\n****************")
                    print(file_name+" file Data")
                    print("****************\n\n")
                    print(contents)

                    msg_box(file_name+" Data", contents)
                    msg_box("Information", "File read successfully")

                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
                
            except Exception as e:
                msg_box("Error", str(e))


        elif call.feat4_m1_rb.isChecked():        ###### Edit File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    f=open(fn,"w+")
                    for i in range(10):
                            f.write("This is line %d\r\n"%(i+1))
                    f.close()

                    print("\n\n****************")
                    print("file Editted")
                    print("****************\n\n")

                    msg_box("Information", "File "+file_name+" Edit Successfully")

                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
            
            except Exception as e:
                msg_box("Error", str(e))
            

        elif call.feat5_m1_rb.isChecked():        ###### Rename File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    newName="/"+file_path+"/"+"new.txt"
                    os.rename(fn,newName)

                    print("\n\n****************")
                    print("file Renamed")
                    print("****************\n\n")
        
                    msg_box("Information", "File "+file_name+" Successfully Renamed as "+newName)

                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
            
            except Exception as e:
                msg_box("Error", str(e))


        elif call.feat7_m1_rb.isChecked():        ###### zip File #######
            try:
                fn = "/"+file_path+"/"+file_name
                if(os.path.exists(fn)):
                    #src=path.realpath(file_name)

                    (fileName, extension) = os.path.splitext(file_name)
                    fileName = fileName+".zip"

                    fn = "/"+file_path+"/"+fileName

                    with ZipFile(fn,"w") as newzip:

                        print("\n\n****************")
                        print("file zipped")
                        print("****************\n\n")
            
                        msg_box("Information", "File "+file_name+" Zipped Successfully")
                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
            
            except Exception as e:
                msg_box("Error", str(e))


        elif call.feat8_m1_rb.isChecked():        ###### unzip File #######
            try:
                fn="/"+file_path+"/"+file_name
                if(os.path.exists(fn)):

                    with ZipFile(fn,"r") as newzip:
                        newzip.extractall()

                        print("\n\n****************")
                        print("file Unzipped")
                        print("****************\n\n")
                
                        msg_box("Information", "File "+file_name+" UnZip Successfully")
                        
                else:
                    msg_box("Error", "File {0} not Exist".format(file_name))
            
            except Exception as e:
                msg_box("Error", str(e))


        else:
            msg_box("Warning", "Please select any one option")

        clear_all()



#########################################
############ System Module ##############
#####################################
def system_modules():

    if call.feat1_m2_rb.isChecked():        ###### Cpu information #######
        try:
            info='cat /proc/cpuinfo'
            print("\n\n****************")
            print("Cpu information")
            print("****************\n\n")
            os.system(info)
            msg_box("Cpu info","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat2_m2_rb.isChecked():        ###### Cpu Architecture information #######
        try:
            info='lscpu'
            print("\n\n****************")
            print("Cpu Architecture Info")
            print("****************\n\n")
            os.system(info)
            msg_box("Cpu Architecture info","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat3_m2_rb.isChecked():        ###### Sockets #######
        try:
            info='ss -s'
            print("\n\n****************")
            print("Sockets")
            print("****************\n\n")
            os.system(info)
            msg_box("Sockets","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat4_m2_rb.isChecked():        ###### CPU Family #######
        try:
            info='lscpu | grep "CPU family"'
            print("\n\n****************")
            print("Cpu Family")
            print("****************\n\n")
            os.system(info)
            msg_box("CPU Family","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat5_m2_rb.isChecked():        ###### uptime #######
        try:
            info='uptime'

            print("\n\n****************")
            print("Uptime")
            print("****************\n\n")

            os.system(info)
            msg_box("uptime","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))
            

    elif call.feat6_m2_rb.isChecked():        ###### View user activity in the system #######
        try:
            info='last'

            print("\n\n****************")
            print("User activity in System")
            print("****************\n\n")

            os.system(info)
            msg_box("user activity","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


#########################################
############ Process Module ##############
#####################################
def process_modules():

    if call.feat1_m3_rb.isChecked():        ###### no.of processing unit #######
        try:
            info='nproc'

            print("\n\n****************")
            print("No.of processing unit")
            print("****************\n\n")
            os.system(info)
            msg_box("no.of processing unit","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat2_m3_rb.isChecked():        ###### Processor #######
        try:
            info='cat /proc/cpuinfo | grep "model name"'

            print("\n\n****************")
            print("Processor")
            print("****************\n\n")
            os.system(info)
            msg_box("Processor","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat3_m3_rb.isChecked():        ###### Current process id #######
        try:

            print("\n\n****************")
            print("Current process id")
            print("****************\n\n")
            print(os.getpid())

            msg_box("Current process id",str(os.getpid()))
            msg_box("Information","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat4_m3_rb.isChecked():        ###### parent process id #######
        try:

            print("\n\n****************")
            print("Parent process id")
            print("****************\n\n")
            print(os.getppid())

            msg_box("parent process id",str(os.getppid()))
            msg_box("Information","Command Successfully run")
            
        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat5_m3_rb.isChecked():        ###### vendor process id #######
        try:
            info='lscpu | grep "Vendor ID"'

            print("\n\n****************")
            print("vendor process id")
            print("****************\n\n")
            os.system(info)
            msg_box("vendor process id","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat6_m3_rb.isChecked():        ###### List out the currently process and their processor ids #######
        try:
            info='ps'

            print("\n\n****************")
            print("List of Current process & it's ID's")
            print("****************\n\n")

            os.system(info)
            msg_box("Current process & it's ID's","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m3_rb.isChecked():        ###### To get information about processor #######
        try:
            info='sudo dmidecode -t processor'

            print("\n\n****************")
            print("Processor information")
            print("****************\n\n")
            os.system(info)

            msg_box("Processor info","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat8_m3_rb.isChecked():        ###### To get information about processor frequency #######
        try:
            info='sudo dmidecode -s processor-frequency'

            print("\n\n****************")
            print("Processor frequency information")
            print("****************\n\n")
            os.system(info)
            msg_box("Processor frequency","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


#########################################
############ Storage Module ##############
#####################################
def storage_modules():

    if call.feat1_m4_rb.isChecked():        ###### Check file system Disk space usage #######
        try:
            info='df -h'

            print("\n\n****************")
            print("Disk Space Usage")
            print("****************\n\n")
            os.system(info)
            msg_box("Disk Space Usage","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat2_m4_rb.isChecked():        ###### Same as file system disk space usage but also show dummy file system disk space usage #######
        try:
            info='df -a'

            print("\n\n****************")
            print("Disk+Dummy Space Usage")
            print("****************\n\n")
            os.system(info)
            msg_box("Disk+Dummy Space Usage","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat3_m4_rb.isChecked():        ###### View all disk partition #######
        try:
            info='sudo fdisk -l'

            print("\n\n****************")
            print("View all disk partition")
            print("****************\n\n")
            os.system(info)
            msg_box("Disk Partition","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat4_m4_rb.isChecked():        ###### View partition on a specific disk #######
        try:
            info='sudo fdisk -l /dev/sda1'

            print("\n\n****************")
            print("View partition on a specific disk")
            print("****************\n\n")
            os.system(info)
            msg_box("Specific disk partition","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat5_m4_rb.isChecked():        ###### View the size of your partition #######
        try:
            info='sudo fdisk -s /dev/sda1'

            print("\n\n****************")
            print("View the size of your partition")
            print("****************\n\n")
            os.system(info)
            msg_box("Size of partition","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat6_m4_rb.isChecked():        ###### Create a hard disk partition #######
        try:
            info='sudo fdisk /dev/sda1'

            print("\n\n****************")
            print("HardDisk partition creation")
            print("****************\n\n")
            os.system(info)
            msg_box("HardDisk partition creation","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m4_rb.isChecked():        ###### Delete a hard disk partition #######
        try:
            info='sudo fdisk /dev/sda1'

            print("\n\n****************")
            print("HardDisk partition Deletion")
            print("****************\n\n")
            os.system(info)
            msg_box("HardDisk partition Deletion","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


#########################################
############ User Module ##############
#####################################
def user_modules():

    if call.feat1_m5_rb.isChecked():        ###### user name #######
        try:
            info='users'

            print("\n\n****************")
            print("User Name")
            print("****************\n\n")
            os.system(info)
            msg_box("User Name","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    # elif call.feat2_m5_rb.isChecked():        ###### Version Information #######
    #     try:
    #         info='users --version'
    #         os.system(info)

    #     except Exception as e:
    #         msg_box("Error", str(e))
    #     else:
    #         msg_box("Version Information","Command Successfully run")


    elif call.feat2_m5_rb.isChecked():        ###### Create user #######
        try:
            name=call.u_name.text()

            if(name==""):
                msg_box("Warning", "Please fill out User name field")
            else:
                info='sudo useradd '+name

                print("\n\n****************")
                print("User added successfully")
                print("****************\n\n")
                os.system(info)
                msg_box("Information","User "+name+" created successfully")

        except Exception as e:
            msg_box("Error", str(e))






    elif call.feat3_m5_rb.isChecked():        ###### Create user with expiry date #######
        try:
            exp_date=str(call.u_date.date())
            exp_date=exp_date.replace(",","-")

            c=0
            for i in exp_date:
                c=c+1
                if i=="(":
                    exp_date=exp_date[c:-1]
                    break

            exp_date=exp_date.replace(" ","")  

            name=call.u_name.text()

            if(name=="" or exp_date==""):
                msg_box("Warning", "Please fill out all fields")
            else:
                info='sudo useradd '+name

                info='sudo useradd -e '+exp_date+" "+name
                call.time1.setText(info)
                print("\n\n****************")
                print("User added successfully")
                print("****************\n\n")
                os.system(info)
                msg_box("Information","User"+name+" with Exp_date of "+exp_date+" is created successfully")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat4_m5_rb.isChecked():        ###### Create user with specific id #######
        try:
            u_id=call.u_id.text()
            name=call.u_name.text()

            if(name=="" or u_id==""):
                msg_box("Warning", "Please fill out all fields")
            else:
                info='sudo useradd -u '+u_id+" "+name

                print("\n\n****************")
                print("User added successfully")
                print("****************\n\n")
                os.system(info)

                msg_box("Information","User"+name+" of ID "+u_id+" is created successfully")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat5_m5_rb.isChecked():        ###### Create user with some description #######
        try:
            desc1=call.u_desc.text()
            name=call.u_name.text()

            if(name=="" or desc1==""):
                msg_box("Warning", "Please fill out all fields")
            else:
                info='sudo useradd -c '+desc1+" "+name

                print("\n\n****************")
                print("User added successfully")
                print("****************\n\n")
                os.system(info)
                
                msg_box("Information","User"+name+" with description{ "+desc1+" } is created successfully")

        except Exception as e:
            msg_box("Error", str(e))



    elif call.feat6_m5_rb.isChecked():        ###### Delete user #######
        try:
            name=call.u_name.text()

            if(name==""):
                msg_box("Warning", "Please fill out user Name fields")
            else:
                info='sudo userdel '+name

                print("\n\n****************")
                print("User deleted successfully")
                print("****************\n\n")
                os.system(info)
                
                msg_box("Information","User"+name+"  is deleted successfully")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m5_rb.isChecked():        ###### check user expiry date #######
        try:
            name=call.u_name.text()

            if(name==""):
                msg_box("Warning", "Please fill out user Name fields")
            else:
                info='sudo chage -l '+name

                print("\n\n****************")
                print("User "+name+" expiry date")
                print("****************\n\n")
                os.system(info)
                msg_box("Information","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat8_m5_rb.isChecked():        ###### How to check user id #######
        try:
            name=call.u_name.text()

            if(name==""):
                msg_box("Warning", "Please fill out user Name fields")
            else:
                info='id -u '+name

                print("\n\n****************")
                print("User "+name+" ID")
                print("****************\n\n")
                os.system(info)
                msg_box("Information","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))



def show_ff():
    call.ff1.hide() 
    call.ff2.hide() 
    call.ff3.hide()  
    call.ff4.hide()  

def show_ff1():
    call.ff1.show() 
    call.ff2.hide() 
    call.ff3.hide()  
    call.ff4.hide()  

def show_ff2():
    call.ff3.hide() 
    call.ff4.hide()  
    call.ff2.show()  
    call.ff1.show()  

def show_ff3():
    call.ff4.hide()  
    call.ff3.show()  
    call.ff1.show()  

def show_ff4():  
    call.ff4.show()  
    call.ff1.show()  


#########################################
############ Network Module ##############
#####################################
def network_modules():

    if call.feat1_m6_rb.isChecked():        ###### Find the ip address and Name #######
        try:
            url1='google.com'
            info='nslookup '+url1

            print("\n\n****************")
            print("IP address of "+url1)
            print("****************\n\n")
            os.system(info)
            msg_box(url1+" IP address","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat2_m6_rb.isChecked():        ###### Route trace of packets to take the host #######
        try:
            url1='facebook.com'
            info='traceroute '+url1

            print("\n\n****************")
            print("Route trace of "+url1)
            print("****************\n\n")
            os.system(info)
            msg_box(url1+" Route trace","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat3_m6_rb.isChecked():        ###### To find the ip and subnet mask #######
        try:
            info='ifconfig'

            print("\n\n****************")
            print("ip & subnet mask")
            print("****************\n\n")
            os.system(info)
            msg_box("IP & subnet mask","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat4_m6_rb.isChecked():        ###### Tell about the various network connection,routing table and interface statistics #######
        try:
            info='netstat'

            print("\n\n****************")
            print("various network connection,routing table and interface statistics")
            print("****************\n\n")
            os.system(info)
            msg_box("NetworkCon, RoutingTable etc statistics","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat5_m6_rb.isChecked():        ###### List all tcp ports #######
        try:
            info='netstat -at'

            print("\n\n****************")
            print("List of all tcp ports")
            print("****************\n\n")
            os.system(info)
            msg_box("TCP ports Lists","Command Successfully run")
        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat6_m6_rb.isChecked():        ###### List all udp ports #######
        try:
            info='netstat -au'

            print("\n\n****************")
            print("List of all udp ports")
            print("****************\n\n")
            os.system(info)
            msg_box("UDP ports Lists","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m6_rb.isChecked():        ###### information about user login #######
        try:
            info='w'

            print("\n\n****************")
            print("information about user login")
            print("****************\n\n")
            os.system(info)
            msg_box("User login info","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))



#########################################
############ Memory Module ##############
#####################################
def memory_modules():

    if call.feat1_m7_rb.isChecked():        ###### Cache Information #######
        try:
            info='lscpu | grep "cache"'

            print("\n\n****************")
            print("cache info")
            print("****************\n\n")
            os.system(info)
            msg_box("Cache Info","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat2_m7_rb.isChecked():        ###### Cache Size #######
        try:
            info='cat /proc/cpuinfo | grep "cache size"'

            print("\n\n****************")
            print("cache size")
            print("****************\n\n")
            os.system(info)
            msg_box("Cache Size","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat3_m7_rb.isChecked():        ###### Ram info in kb #######
        try:
            info='free '

            print("\n\n****************")
            print("Ram info in KB's")
            print("****************\n\n")
            os.system(info)
            msg_box("RamInfo (KB's)","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat4_m7_rb.isChecked():        ###### Ram info in mb #######
        try:
            info='free -m'

            print("\n\n****************")
            print("Ram info in MB's")
            print("****************\n\n")
            os.system(info)
            msg_box("RamInfo (MB's)","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))

    elif call.feat5_m7_rb.isChecked():        ###### Ram info in gb #######
        try:
            info='free -g'

            print("\n\n****************")
            print("Ram info in GB's")
            print("****************\n\n")
            os.system(info)
            msg_box("RamInfo (GB's)","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat6_m7_rb.isChecked():        ###### Memory information #######
        try:
            info='hwinfo --memory'

            print("\n\n****************")
            print("Memory info")
            print("****************\n\n")
            os.system(info)
            msg_box("Memory info","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m7_rb.isChecked():        ###### To show virtual memory statistics of the system #######
        try:
            info='vmstat'

            print("\n\n****************")
            print("VirtualMemory Stats")
            print("****************\n\n")
            os.system(info)
            msg_box("VirtualMemory Stats","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


#########################################
############ Date Module ##############
#####################################
def date_modules():

    if call.feat1_m8_rb.isChecked():        ###### date #######
        try:
            info='date'

            print("\n\n****************")
            print("Date")
            print("****************\n\n")
            os.system(info)
            msg_box("Current Date","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    if call.feat2_m8_rb.isChecked():        ###### cal #######
        try:
            info='cal'

            print("\n\n****************")
            print("Calender")
            print("****************\n\n")
            os.system(info)
            msg_box("Calender","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    if call.feat3_m8_rb.isChecked():        ###### To show time gmt or utc #######
        try:
            info='date -u'

            print("\n\n****************")
            print("Time GMT/UTC")
            print("****************\n\n")
            os.system(info)
            msg_box("Time GMT/UTC","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat4_m8_rb.isChecked():        ###### To show date and time previous day #######
        try:
            info='date --date="yesterday"'

            print("\n\n****************")
            print("Yesteday Date")
            print("****************\n\n")
            os.system(info)
            msg_box("Yesteday Date","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat5_m8_rb.isChecked():        ###### show date and time of next day #######
        try:
            info='date --date="tomorrow"'

            print("\n\n****************")
            print("Tomorrow Date")
            print("****************\n\n")
            os.system(info)
            msg_box("Tomorrow Date","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat6_m8_rb.isChecked():        ###### show date and time of upcoming particular week day #######
        try:
            info='date --date="next tue"'

            print("\n\n****************")
            print("Upcoming Week Date")
            print("****************\n\n")
            os.system(info)
            msg_box("Upcoming Week Date","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat7_m8_rb.isChecked():        ###### show date and time after 2 days #######
        try:
            info='date --date="2 day"'

            print("\n\n****************")
            print("Date After 2Days")
            print("****************\n\n")
            os.system(info)
            msg_box("Date After 2Days","Command Successfully run")

        except Exception as e:
            msg_box("Error", str(e))


    elif call.feat8_m8_rb.isChecked():        ###### To show date and time 2 years ago #######
        try:
            info='date --date="2year ago"'

            print("\n\n****************")
            print("Date 2yearsAgo")
            print("****************\n\n")
            os.system(info)
            msg_box("Date 2yearsAgo","Command Successfully run")

            
        except Exception as e:
            msg_box("Error", str(e))

    # elif call.feat3_m8_rb.isChecked():        ###### show date and time 5 seconds ago #######
    #     try:
    #         info='date --date="5 sec ago"'
    #         os.system(info)

    #     except Exception as e:
    #         msg_box("Error", str(e))
    #     else:
    #         msg_box("Date 5Sec Ago","Command Successfully run")


    # elif call.feat5_m8_rb.isChecked():        ###### show date and time 6 months ago #######
    #     try:
    #         info='date --date="6 month ago"'
    #         os.system(info)

    #     except Exception as e:
    #         msg_box("Error", str(e))
    #     else:
    #         msg_box("Date,Time 6Mon Ago","Command Successfully run")



def msg_box(title="info",msg="Something went wrong!"):
    QMessageBox.information(None,title,msg) 


def clear_all():
    call.f_name.setText("")
    call.f_path.setText("")
    call.feat1_m1_rb.setAutoExclusive(False)    
    call.feat2_m1_rb.setAutoExclusive(False)    
    call.feat3_m1_rb.setAutoExclusive(False)    
    call.feat4_m1_rb.setAutoExclusive(False)    
    call.feat5_m1_rb.setAutoExclusive(False)    
    call.feat6_m1_rb.setAutoExclusive(False) 

    call.feat1_m1_rb.setChecked(False)    
    call.feat2_m1_rb.setChecked(False)    
    call.feat3_m1_rb.setChecked(False)    
    call.feat4_m1_rb.setChecked(False)    
    call.feat5_m1_rb.setChecked(False)    
    call.feat6_m1_rb.setChecked(False) 

    call.feat1_m1_rb.setAutoExclusive(True)    
    call.feat2_m1_rb.setAutoExclusive(True)    
    call.feat3_m1_rb.setAutoExclusive(True)    
    call.feat4_m1_rb.setAutoExclusive(True)    
    call.feat5_m1_rb.setAutoExclusive(True)    
    call.feat6_m1_rb.setAutoExclusive(True) 





app=QtWidgets.QApplication([])
call=uic.loadUi("mini_os.ui")

now = QDate.currentDate()
call.date1.setText(now.toString(Qt.DefaultLocaleLongDate))

time = QTime.currentTime()
#call.time1.setText(time.toString(Qt.DefaultLocaleLongDate))

call.time1.setText(str(call.u_date.date()))

show_ff()


call.feat1_m5_rb.toggled.connect(show_ff)
call.feat2_m5_rb.toggled.connect(show_ff1)
call.feat3_m5_rb.toggled.connect(show_ff2)
call.feat4_m5_rb.toggled.connect(show_ff3)
call.feat5_m5_rb.toggled.connect(show_ff4)
call.feat6_m5_rb.toggled.connect(show_ff1)
call.feat7_m5_rb.toggled.connect(show_ff1)
call.feat8_m5_rb.toggled.connect(show_ff1)






show_frame0()

call.submit1_btn.clicked.connect(File_modules)
call.submit2_btn.clicked.connect(system_modules)
call.submit3_btn.clicked.connect(process_modules)
call.submit4_btn.clicked.connect(storage_modules)
call.submit5_btn.clicked.connect(user_modules)
call.submit6_btn.clicked.connect(network_modules)
call.submit7_btn.clicked.connect(memory_modules)
call.submit8_btn.clicked.connect(date_modules)


call.m1_btn.clicked.connect(show_frame1)
call.m2_btn.clicked.connect(show_frame2)
call.m3_btn.clicked.connect(show_frame3)
call.m4_btn.clicked.connect(show_frame4)
call.m5_btn.clicked.connect(show_frame5)
call.m6_btn.clicked.connect(show_frame6)
call.m7_btn.clicked.connect(show_frame7)
call.m8_btn.clicked.connect(show_frame8)

call.show()
app.exec_()

# print(now.toString(Qt.ISODate))
# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
